#Python


#FastAPI
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
#env
# from routers.messages import messages_router
# from routers.webhook import webhook_router
# from database import SessionLocal, engine, Base
# from models.models import Patient, Doctor, Appointment

# Base.metadata.create_all(bind=engine)


#Create the FastAPI app.
app = FastAPI()
# app.include_router(messages_router)
# app.include_router(webhook_router)


# # Dependency
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

@app.get("/")
def start():
    return "Welcome to the API of automatic replies in WhatsApp"



app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite cualquier origen
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos los métodos
    allow_headers=["*"],  # Permite todas las cabeceras
)

@app.get("/appointments")
def get_appointments():
    return [
        {
            "fecha": "2023-03-17",
            "nombre": "Juan"
        }
    ]


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
