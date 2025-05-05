import grpc
import logging
import asyncio
import signal
from grpc_reflection.v1alpha import reflection
from controller.generated import authorization_pb2
from controller.generated.authorization_pb2_grpc import AuthorizationServicer, add_AuthorizationServicer_to_server
from service.redis_service import TokenService


class InitiateAuthentication(AuthorizationServicer):
    initiated_token_service = TokenService()

    async def GetTokens(self, request, context):
        logging.info(f'Request for {request.user_id} tokens')
        access_token, refresh_token = await self.initiated_token_service.generate_tokens(user_id=request.user_id)
        return authorization_pb2.ReturnTokens(access=access_token, refresh=refresh_token)

    async def GetAccess(self, request, context):
        logging.info(f'Request for access')
        access_token = await self.initiated_token_service.generate_access_using_refresh(request.token)
        return authorization_pb2.ReturnAccess(access=access_token)

    async def GetRefresh(self, request, context):
        logging.info(f'Request for {request.user_id} refresh')
        refresh_token = await self.initiated_token_service.get_refresh(request.user_id)
        return authorization_pb2.ReturnRefresh(refresh=refresh_token)

    async def GetUserId(self, request, context):
        logging.info(f'Request for user ID')
        user_id = await self.initiated_token_service.check_user_id(request.token)
        return authorization_pb2.ReturnUserId(user_id=user_id)

    async def LogOut(self, request, context):
        logging.info(f'Log out user {request.user_id}')
        result = await self.initiated_token_service.delete_refresh(request.user_id)
        if result:
            message = 'logged_out'
        else:
            message = 'logout_failed'
        return authorization_pb2.ReturnLogoutState(message=message)

async def server_graceful_shutdown(server: grpc.aio.Server):
    logging.info('Starting graceful shutdown...')
    await server.stop(10)
    logging.info('Server shutdown complete.')


async def serve():
    server = grpc.aio.server()
    add_AuthorizationServicer_to_server(InitiateAuthentication(), server)
    service_names = (
        authorization_pb2.DESCRIPTOR.services_by_name['Authorization'].full_name,
        reflection.SERVICE_NAME
    )
    reflection.enable_server_reflection(service_names, server)
    server_address = '[::]:50051'
    server.add_insecure_port(server_address)

    logging.info(f'Starting server on {server_address}')
    await server.start()

    loop = asyncio.get_running_loop()
    for sig in (signal.SIGINT, signal.SIGTERM):
        loop.add_signal_handler(sig, lambda :asyncio.create_task(server_graceful_shutdown(server)))

    await server.wait_for_termination()


def async_serve_wrapper():
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(serve())
    except KeyboardInterrupt:
        pass