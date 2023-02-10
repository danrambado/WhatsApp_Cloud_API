#Python
import requests
import json
from typing import Union

#Pydantic
from pydantic import BaseModel
#FastAPI

from fastapi import FastAPI, HTTPException, Request, Response, Body, Header
from fastapi.responses import JSONResponse

#env
import models


#Open the json configuration parameters
with open('config.json') as f:
    config = json.load(f)

#Define the config parameters that will be used.
api_url = config["API_URL"]
acces_token = config["ACCESS_TOKEN"]
headers = {'Authorization': f'Bearer {acces_token}'}
verify_token = config["VERIFY_TOKEN"]


#Create the FastAPI app.
app = FastAPI()
@app.get("/")
def hello_world():
    return "Hello World!"

#Endpoint to send messages.
@app.post("/send_messagse/")
async def send_message(message: Union[models.TextMessage, models.InteractiveMessage]):
    data = message.dict()

    if message.type == "text":
        response = requests.post(api_url, headers=headers, json=data)
    elif message.type == "interactive":
        response = requests.post(api_url, headers=headers, json=data)

    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.json())

    return {"message": "Message sent successfully"}


@app.get("/webhook/")
async def webhook_whatsapp_api(request: Request):

    if request.method == "GET":
        if request.query_params.get('hub.verify_token') == config["VERIFY_TOKEN"]:
            return int(request.query_params.get('hub.challenge'))
        return JSONResponse(content={"error": "Authentication failed. Invalid Token."}, status_code=400)

@app.post("/webhook/")
async def handle_webhooks(request: Request):

    print(await request.json())
    res = await request.json()
    try:
        if res['entry'][0]['changes'][0]['value']['messages'][0]['id']:
            pass
    except:
        pass
    
    return {"message": "200 OK HTTPS"}


@app.post("/send_message/")
def send_message(info: models.pacient_info):


    data = {
        "messaging_product": "whatsapp",
        "recipient_type": "individual",
        "to": info.number,
        "type": "interactive",
        "interactive": {
            "type": "button",
            "header": {
                "type": "text",
                "text": "Confirmación de turno médico"
            },
            "body": {
                "text": f"Estimado/a paciente es un placer confirmar su turno médico programado para el día *{info.date}* a las *{info.time}hs*. Le recomendamos llegar con 10 minutos de anticipación. Este mensaje es para confirmar su asistencia. Por favor, háganos saber si necesita cancelar o reprogramar su turno."
            },
            "footer": {
                "text": "IAF | Instituto Alexander Fleming"
            },
            "action": {
                "buttons": [
                    {
                        "type": "reply",
                        "reply": {
                            "id": "UNIQUE_BUTTON_ID_1",
                            "title": "Confirmar turno"
                        }
                    },
                    {
                        "type": "reply",
                        "reply": {
                            "id": "UNIQUE_BUTTON_ID_2",
                            "title": "Cancelar turno"
                        }
                    },
                    {
                        "type": "reply",
                        "reply": {
                            "id": "UNIQUE_BUTTON_ID_3",
                            "title": "Reprogramar turno"
                        }
                    }
                ]
            }
        }
    }
    response = requests.post(api_url, headers=headers, json=data)

    return response.json()