#Python
import requests
import json
#Pydantic
from pydantic import BaseModel
#FastAPI
from fastapi import FastAPI, HTTPException, Request, Response, Body
from fastapi.responses import JSONResponse


#Open the json configuration parameters
with open('config.json') as f:
    config = json.load(f)

app = FastAPI()

@app.get("/")
def hello_world():
    return "Hello World!"

class Message_Template(BaseModel):
    messaging_product: str
    recipient_type: str
    to: str
    type: str
    template: dict

@app.post("/send_message_template/")
async def send_message_template(Message: Message_Template):
    API_URL = config["API_URL"]
    ACCESS_TOKEN = config["ACCESS_TOKEN"]
    HEADERS = {
        'Authorization': f'Bearer {ACCESS_TOKEN}',
        'Content-Type': 'application/json'
    }
    DATA = Message.dict()

    response = requests.post(API_URL, headers=HEADERS, json=DATA)

    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.json())

    return {"message": "Message sent successfully"}


class Message(BaseModel):
    messaging_product: str
    recipient_type: str
    to: str
    type: str
    text: dict

@app.post("/send_message/")
async def send_message(Message: Message):
    API_URL = config["API_URL"]
    ACCESS_TOKEN = config["ACCESS_TOKEN"]
    HEADERS = {
        'Authorization': f'Bearer {ACCESS_TOKEN}',
    }
    DATA = Message.dict()

    response = requests.post(API_URL, headers=HEADERS, json=DATA)

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


