from datetime import timedelta
from db.db_manager import RedisDB
from jwtoken.jwt_process import (
    generate_access_token,
    generate_refresh_token,
    generate_jti,
    jwt_decoder,
    REFRESH_TOKEN_EXPIRE_DAYS
)


class TokenService(RedisDB):
    def __init__(self):
        super().__init__()
        self.jti = generate_jti()

    async def generate_tokens(self, user_id):
        access = await generate_access_token(self.jti, user_id)
        refresh = await generate_refresh_token(self.jti, user_id)
        await self.save_refresh_token(refresh, user_id)
        return access, refresh

    async def save_refresh_token(self, refresh_token, user_id):
        await self.async_redis_db.setex(
            f"user:{user_id}:device:{None}",
            timedelta(days=REFRESH_TOKEN_EXPIRE_DAYS),
            value=f"jwt:refresh:{refresh_token}"
        )

    async def generate_access_using_refresh(self, refresh_token):
        try:
            payload = jwt_decoder(refresh_token)
            user_data = await self.async_redis_db.get(f"user:{payload['sub']}:device:{None}")
            if not user_data:
                return 'invalid_token'

            saved_refresh = user_data.split(':')[-1]
            saved_refresh_payload = jwt_decoder(saved_refresh)

            if payload != saved_refresh_payload:
                return 'invalid_token'

            access = await generate_access_token(saved_refresh_payload['jti'], saved_refresh_payload['sub'])
            return access
        except:
            return 'invalid_token'

    async def delete_refresh(self, user_id):
        try:
            result = await self.async_redis_db.delete(f"user:{user_id}:device:{None}")
            if result == 1:
                return True
            else:
                return False
        except:
            return False

    async def get_refresh(self, user_id):
        try:
            user_data = await self.async_redis_db.get(f"user:{user_id}:device:{None}")
            saved_refresh = user_data.split(':')[-1]
            return saved_refresh
        except:
            return None

    async def check_user_id(self, token):
        try:
            payload = jwt_decoder(token)
            user_data = await self.async_redis_db.get(f"user:{payload['sub']}:device:{None}")
            if not user_data:
                return 'invalid_token'

            saved_refresh = user_data.split(':')[-1]
            saved_refresh_payload = jwt_decoder(saved_refresh)

            if payload['sub'] == saved_refresh_payload['sub'] and payload['jti'] == saved_refresh_payload['jti']:
                return saved_refresh_payload['sub']
            else:
                return 'invalid_token'
        except Exception as ex:
            print(ex)
            return 'invalid_token'