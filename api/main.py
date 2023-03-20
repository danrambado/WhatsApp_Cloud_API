#Python
import asyncio
#FastAPI
from fastapi import FastAPI, Depends, Request, HTTPException

#env
from services import redis_state
from services.redis_utils import get_redis_pool, close_redis_pool

# routers
from routers.messages import messages_router
from routers.webhook import webhook_router
from routers.get_data_iaf import get_data_iaf_router
from routers.db_manage import db_manage_router


#Create the FastAPI app and ad the routers
app = FastAPI()
app.include_router(messages_router)
app.include_router(webhook_router)
app.include_router(get_data_iaf_router)
app.include_router(db_manage_router)


@app.on_event("startup")
async def on_startup():
    redis_state.redis_pool = await get_redis_pool()

@app.on_event("shutdown")
async def on_shutdown():
    await close_redis_pool(redis_state.redis_pool)

@app.on_event("shutdown")
async def on_shutdown():
    await close_redis_pool(redis_state.redis_pool)


# Endpoints
@app.get("/")
def start():
    return "Welcome to the API of automatic replies in WhatsApp"

@app.get("/appointments")
def get_appointments():
    return [
        {
            "fecha": "2023-03-17",
            "nombre": "Juan"
        }
    ]



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
