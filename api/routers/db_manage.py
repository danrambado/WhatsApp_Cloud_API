# Python
import asyncio
import json
# FastAPI
from fastapi import APIRouter, HTTPException, Depends
from fastapi.responses import StreamingResponse


# SQLAlchemy
from sqlalchemy.orm import Session

# aioredis
from aioredis import Redis

# env
from database import SessionLocal, engine, Base
from schemas import database
from services.redis_utils import get_redis_pool
from services.crud_utils import create_appointment


Base.metadata.create_all(bind=engine)

db_manage_router = APIRouter()

# Dependencies
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@db_manage_router.get('/load_appointment_data')
async def load_appointment_data(redis: Redis = Depends(get_redis_pool), db: Session = Depends(get_db)):
    appointment_list = await redis.get("appointment_list")
    appointment_list = json.loads(appointment_list)
    create_appointment(db, appointment_list)

    return {"message": "Data saved successfully!"}