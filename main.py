import multiprocessing
from fastapi import FastAPI
from contextlib import asynccontextmanager
from controller.grpc_server import async_serve_wrapper
from db.db_manager import RedisDB


@asynccontextmanager
async def lifespan(application: FastAPI):
    grpc_server_process = multiprocessing.Process(
        target=async_serve_wrapper,
        daemon=True
    )
    grpc_server_process.start()
    application.grpc_server_process = grpc_server_process

    yield

    grpc_server_process.terminate()
    grpc_server_process.join()

    redis = RedisDB()
    await redis.close_db_connection()


app = FastAPI(lifespan=lifespan)