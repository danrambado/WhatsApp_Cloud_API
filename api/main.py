#Python
import asyncio
import requests

#FastAPI
from fastapi import FastAPI, Depends, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware


#env
from services import redis_state
from database import get_db, get_db_async
from services.redis_utils import get_redis_pool, close_redis_pool
from routers.db_manage import load_appointment_data
from templates_messges import text_templates

# routers
from routers.send_messages import messages_router
from routers.webhook import webhook_router
from routers.get_data_iaf import get_data_iaf_router
from routers.db_manage import db_manage_router


#Create the FastAPI app and ad the routers
app = FastAPI()
app.include_router(messages_router)
app.include_router(webhook_router)
app.include_router(get_data_iaf_router)
app.include_router(db_manage_router)

# CORS CONFIG
origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def on_startup():
    redis_state.redis_pool = await get_redis_pool()
    asyncio.create_task(load_appointment_data(redis_state.redis_pool, get_db_async))
    


@app.on_event("shutdown")
async def on_shutdown():
    await close_redis_pool(redis_state.redis_pool)


# Endpoints
@app.get("/")
def start():
    return "Welcome to the API of automatic replies in WhatsApp"

