#Python
from datetime import date, datetime, timedelta
import json
import httpx

#FastAPI
from fastapi import APIRouter, HTTPException, Depends
from fastapi import Path
from fastapi.responses import JSONResponse

# aioredis
from aioredis import Redis

# env
import services.iaf_api_utils as iaf_api_utils
from services import redis_utils
from services import iaf_api_utils

get_data_iaf_router = APIRouter()

async def get_and_check_token(redis: Redis = Depends(redis_utils.get_redis_pool)) -> str:
    token = await redis_utils.get_token(redis)
    if token is None:
        token = iaf_api_utils.authentication()
        expire = 29 * 60
        await redis_utils.set_token(redis, token, expire)
    return token

async def get_appointment_data(date: date, redis: Redis =  Depends(redis_utils.get_redis_pool), token: str = Depends(get_and_check_token)):
    """
    Searches for shifts by date and stores them temporarily in redis with the set() method.

    Args:
        date (date): _description_
        redis (Redis, optional): _description_. Defaults to Depends(redis_utils.get_redis_pool).
        token (str, optional): _description_. Defaults to Depends(get_and_check_token).

    Returns:
        dict: message
    """
    date = date.strftime("%Y-%m-%d")
    appointment_list = iaf_api_utils.get_appointment_list(date, token)
    appointment_list = iaf_api_utils.preproces_appoinment_data(appointment_list)
    await redis.set("appointment_list", json.dumps(appointment_list))
    
    return {"message": "Data successfully obtained and saved to redis"}

async def get_pacient_data(idpersona: int, redis: Redis = Depends(redis_utils.get_redis_pool)):
    token = await get_and_check_token(redis)
    patient_info = iaf_api_utils.get_pacient_data(idpersona, token)
    patient_info = iaf_api_utils.preproces_patient_contact_info(patient_info)
    return patient_info


@get_data_iaf_router.get("/get_appointment_data")
async def get_appointment_data_enpoint(date: date, redis: Redis = Depends(redis_utils.get_redis_pool), token: str = Depends(get_and_check_token)):
    response = await get_appointment_data(date=date,redis=redis, token=token)
    return response
