# Python
import json
from datetime import date
import asyncio
from contextlib import closing


# FastAPI
from fastapi import APIRouter, Depends

# SQLAlchemy
from sqlalchemy.orm import Session

# aioredis
from aioredis import Redis

# env
from database import SessionLocal, engine, Base, get_db
from schemas import database
from services.redis_utils import get_redis_pool
from services.crud_utils import  filter_appointments, update_status_confirmation
from routers.get_data_iaf import get_pacient_data
from services import crud_utils


db_manage_router = APIRouter()

            

async def filter_and_save_appointments(date: date, db: Session = Depends(get_db)):
    """
    Filter the appointments using the filter_appointments() function and 
    then save them in the confirmations table with the save_confirmations() function.

    Args:
        date (date): _description_
        db (Session, optional): _description_. Defaults to Depends(get_db).
    """

    confirmations_list = crud_utils.filter_appointments(db, date)
    crud_utils.save_confirmations(db,confirmations_list)

    return {"message": "Appointmet confirmation saved successfully!"}

async def load_appointment_data(redis: Redis, get_db_function):
    """
    Listen in "appointment_list" of redis to get information and load it if it exists, then saves 
    the data with the create_appointme() function 
    imported from services --> crud_py and iterates over the appointment list to see if the patient's 
    contact data is in the contact database. If not, it fetches the data with the get_pacient_data().

    Args:
        redis (Redis, optional): _description_. Defaults to Depends(get_redis_pool).
        db (Session, optional): _description_. Defaults to Depends(get_db).

    Returns:
        dict: message
    """
    
    while True:
        appointment_list = await redis.get("appointment_list")
        if appointment_list:
            appointment_list = json.loads(appointment_list)

            db = get_db_function()
            try:
                crud_utils.create_appointment(db, appointment_list)

                for item in appointment_list:
                    idpersona = item['idpersona']
                    exists = crud_utils.read_idpersona(db, idpersona)

                    if not exists:
                        patient_data = await get_pacient_data(idpersona, redis)
                        if patient_data:
                            crud_utils.create_patient_info(db, patient_data)

            finally:
                db.close()

            await redis.delete("appointment_list")

        await asyncio.sleep(60)

@db_manage_router.get('/filter_and_save_appointments')
async def filter_and_save_appointments_endpoint(date: date, db: Session = Depends(get_db)):
    await filter_and_save_appointments(date, db )


# # @db_manage_router.get('/load_appointment_data')
# async def load_appointment_data_endpoint(redis: Redis = Depends(get_redis_pool), db: Session = Depends(get_db)):
#     response = await load_appointment_data(redis, db)
#     return response





        
# @db_manage_router.get('/get_filtered_appointments')
# async def get_filtered_appointments(db: Session = Depends(get_db)):
#     return fetch_filtered_appointments(db)


# @db_manage_router.get('/get_confirmation_by_date/{date}')
# async def get_confirmation_by_date(db: Session = Depends(get_db), date: date = Path):
#     return crud_utils.consult_confirmations(db, date)
