#Python
import asyncio
import requests

#FastAPI
from fastapi import FastAPI, Depends, Request, HTTPException

#env
from services import redis_state
from database import get_db, get_db_async
from services.redis_utils import get_redis_pool, close_redis_pool
from routers.db_manage import load_appointment_data
from templates_messges import text_templates

# routers
from routers.unit_messages import messages_router
from routers.webhook import webhook_router
from routers.get_data_iaf import get_data_iaf_router
from routers.db_manage import db_manage_router
from routers.mass_messages import mass_messages_router


#Create the FastAPI app and ad the routers
app = FastAPI()
app.include_router(messages_router)
app.include_router(webhook_router)
app.include_router(get_data_iaf_router)
app.include_router(db_manage_router)
app.include_router(mass_messages_router)

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



















@app.post("/test")
def send_multiple_mesages():
    data = [
        {
            "idpersona": 220354,
            "date_only": "2023-03-22",
            "time_only": "11:00:00",
            "persCelular": 541133149984
        },
    ]

    url= 'http://localhost:8000/interactive_button_message'
    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json'
    }

    for info in data:

        idpersona = info["idpersona"]
        date_only = info["date_only"]
        time_only = info["time_only"]
        persCelular = info["persCelular"]
        
        payload = text = text_templates.ButtonMessages(persCelular)
        payload = text.confirmation_message(date_only, time_only)

        response = requests.post(url, headers=headers, json=payload)



# @app.post("/test_create_appoinmetn")
# def test(appoinment: database.appoinmentTEST, db: Session = Depends(get_db)):
#     return crud_utils.create_appointment(db=db, appoinment=appoinment)
    
    





# @app.post("/webhook/")
# async def handle_webhooks(request: Request):

#     print(await request.json())
#     res = await request.json()

    

#     if "contacts" in res["entry"][0]["changes"][0]["value"]:

#         number = res['entry'][0]['changes'][0]['value']['contacts'][0]['wa_id']
#         status = res["entry"][0]["changes"][0]["value"]["messages"][0]["interactive"]["button_reply"]["title"]

#         number = number[:2] + number[3:]
#         try:
#             if status == 'Confirmar turno':
#                 data = {
#                         "number": number,
#                         "text": "Gracias por confirmar su turno. Para mejorar nuestra atencion le pedimos que nos cuente brevemente el motivo de su consulta con el siguiente formato:"
#                     }
#                 message = schema.simple_message(**data)
            
            
#                 a = await send_simple_message(message)

#                 data = {
#                         "number": number,
#                         "text": "Motivo de consulta: Me duele la cabeza y tengo fiebre"
#                     }
#                 message = schema.simple_message(**data)
            
#                 a = await send_simple_message(message)

#             elif status == "Cancelar turno":
#                 data = {
#                         "number": number,
#                         "text": "Lamentamos que no pueda asistir. Ante cualquier duda, contactenos"
#                     }
#                 message = schema.simple_message(**data)
            
            
#                 a = await send_simple_message(message)

#             elif status == "Reprogramar turno":
#                 data = {
#                         "number": number,
#                         "text": "Nos contactaremos a la brevedad para reprogramar su turno"
#                     }
#                 message = schema.simple_message(**data)
            
            
#                 a = await send_simple_message(message)
        
#         except:
#             print("algo anda mal")
    
#     return {"message": "200 OK HTTPS"}
