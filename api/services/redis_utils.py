# Python
import aioredis
import json

async def get_redis_pool() -> aioredis.Redis:
    return aioredis.from_url("redis://redis:6379/0", encoding="utf-8", decode_responses=True)

async def close_redis_pool(redis: aioredis.Redis):
    await redis.close()

async def set_token(redis: aioredis.Redis, token: str, expire: int):
    await redis.set("token", token, ex=expire)

async def get_token(redis: aioredis.Redis) -> str:
    token = await redis.get("token")
    return token