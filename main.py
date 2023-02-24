#Python
import requests
import json

#FastAPI
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse

#env
from schemas import schema
from templates_messges import json_templates
from routers.messages import messages_router


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
app.include_router(messages_router)


@app.get("/")
def start():
    return "Welcome to the API of automatic replies in WhatsApp"



@app.get("/webhook/")
async def verify_token_webhook(request: Request):
    """
    Endpoint to verify the webhook token

    Parameters:
    ----------
    request: Request
        Request structure from fastAPI.
    
    Returns:
    -------
    JSONResponse
    """

    if request.method == "GET":
        if request.query_params.get('hub.verify_token') == config["VERIFY_TOKEN"]:
            return int(request.query_params.get('hub.challenge'))
        return JSONResponse(content={"error": "Authentication failed. Invalid Token."}, status_code=400)

@app.post("/webhook/")
async def handle_webhooks(request: Request):

    print(await request.json())
    res = await request.json()

    

    if "contacts" in res["entry"][0]["changes"][0]["value"]:

        number = res['entry'][0]['changes'][0]['value']['contacts'][0]['wa_id']
        status = res["entry"][0]["changes"][0]["value"]["messages"][0]["interactive"]["button_reply"]["title"]

        number = number[:2] + number[3:]
        try:
            if status == 'Confirmar turno':
                data = {
                        "number": number,
                        "text": "Gracias por confirmar su turno. Para mejorar nuestra atencion le pedimos que nos cuente brevemente el motivo de su consulta con el siguiente formato:"
                    }
                message = schema.simple_message(**data)
            
            
                a = await send_simple_message(message)

                data = {
                        "number": number,
                        "text": "Motivo de consulta: Me duele la cabeza y tengo fiebre"
                    }
                message = schema.simple_message(**data)
            
                a = await send_simple_message(message)

            elif status == "Cancelar turno":
                data = {
                        "number": number,
                        "text": "Lamentamos que no pueda asistir. Ante cualquier duda, contactenos"
                    }
                message = schema.simple_message(**data)
            
            
                a = await send_simple_message(message)

            elif status == "Reprogramar turno":
                data = {
                        "number": number,
                        "text": "Nos contactaremos a la brevedad para reprogramar su turno"
                    }
                message = schema.simple_message(**data)
            
            
                a = await send_simple_message(message)
        
        except:
            print("algo anda mal")
    
    return {"message": "200 OK HTTPS"}
