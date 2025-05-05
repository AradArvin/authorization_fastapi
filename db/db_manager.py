from redis import asyncio as aioredis
from core.settings import REDIS_HOST_ADDRESS


class RedisDB:
    HOST_ADDRESS: str = REDIS_HOST_ADDRESS

    def __init__(self):
        self.async_redis_db = aioredis.from_url(self.HOST_ADDRESS, decode_responses=True)

    async def close_db_connection(self):
        await self.async_redis_db.close()