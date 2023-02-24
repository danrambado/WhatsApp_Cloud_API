#Python
import requests
import json

#FastAPI
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse

#env
import models
import template_message


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
def start():
    return "Welcome to the API of automatic replies in WhatsApp"

#Endpoint to send a simple messages.
@app.post("/simple_message")
async def send_simple_message(message: models.simple_message):
    """
    Create a intance of the class SimpleMessage to create the structure of the json_response for a simple menssage.
    The variables that the class is going to take come from a dict/json that has the structure defined in models.py
    
    Parameters:
    ----------
    message: dict
        a dict with the structure "simple_message" defined in models.py

    Returns:
    -------
    renponse: json response
    """
    # Intance the SimpleMessage class and use the method to_dict() to create the data for the htpp request.
    data = template_message.SimpleMessage(**message.dict()).to_dict()

    # Send the request
    try:
        response = requests.post(api_url, headers=headers, json=data)
        response.raise_for_status()

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error sending message: {str(e)}")
    return response.json()


@app.post("/interactive_button_message")
async def send_interactive_button_message(message: models.button_message):
    """
    Create a intance of the class InteractiveButtonMessage to create the structure of the json_response for a simple menssage.
    The variables that the class is going to take come from a dict/json that has the structure defined in models.py
    
    Parameters:
    ----------
    message: dict
        a dict with the structure "simple_message" defined in models.py

    Returns:
    -------
    renponse: json response
    """
    # Intance the SimpleMessage class and use the method to_dict() to create the data for the htpp request.
    data = template_message.InteractiveButtonMessage(**message.dict()).to_dict()

    # Send the request
    try:
        response = requests.post(api_url, headers=headers, json=data)
        response.raise_for_status()

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error sending message: {str(e)}")
    return response.json()



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
                message = models.simple_message(**data)
            
                a = await send_simple_message(message)

                data = {
                        "number": number,
                        "text": "Motivo de consulta: Me duele la cabeza y tengo fiebre"
                    }
                message = models.simple_message(**data)
                a = await send_simple_message(message)

            elif status == "Cancelar turno":
                data = {
                        "number": number,
                        "text": "Lamentamos que no pueda asistir. Ante cualquier duda, contactenos"
                    }
                message = models.simple_message(**data)
            
                a = await send_simple_message(message)

            elif status == "Reprogramar turno":
                data = {
                        "number": number,
                        "text": "Nos contactaremos a la brevedad para reprogramar su turno"
                    }
                message = models.simple_message(**data)
            
                a = await send_simple_message(message)
        
        except:
            print("algo anda mal")
    
    return {"message": "200 OK HTTPS"}
