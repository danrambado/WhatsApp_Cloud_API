#Python
from datetime import datetime, timedelta
import json

#FastAPI
from fastapi import APIRouter, HTTPException, Depends

# aioredis
from aioredis import Redis

# env
import services.iaf_api_utils as iaf_api_utils
from services.redis_utils import get_redis_pool, set_token, get_token
from services.iaf_api_utils import preproces_appoinment_data
from services.crud_utils import create_appointment


get_data_iaf_router = APIRouter()

async def get_and_check_token(redis: Redis = Depends(get_redis_pool)) -> str:
    token = await get_token(redis)
    if token is None:
        token = iaf_api_utils.authentication()
        # The token expires in 30 minutes, so we store it in Redis with an expiration time of 29 minutes.
        expire = 29 * 60
        await set_token(redis, token, expire)
    return token

@get_data_iaf_router.post("/get_appointment_data")
async def get_appointment_data(redis: Redis = Depends(get_redis_pool), token: str = Depends(get_and_check_token)):
    date = (datetime.today() + timedelta(days=2)).strftime("%Y-%m-%d")
    appointment_list = iaf_api_utils.get_appointment_list(date, token)
    appointment_list = preproces_appoinment_data(appointment_list)
    print(appointment_list)
    await redis.set("appointment_list", json.dumps(appointment_list))

    return {"message": "Data saved successfully!"}