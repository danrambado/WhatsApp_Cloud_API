#Python
import requests
import json

#FastAPI
from fastapi import APIRouter, HTTPException

# env
from services.utils import get_appointment_list

get_appointment_data_router = APIRouter()

@get_appointment_data_router.post("/get_appointment_data")
async def get_appointment_data():
    appointment_list = get_appointment_list()
     
