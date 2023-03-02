#Python
import requests
import json

#FastAPI
from fastapi import APIRouter, HTTPException

#env 
from schemas import schema
from templates_messges import json_templates

#Open the json configuration parameters
with open('app/config/config.json') as f:
    config = json.load(f)

#Define the config parameters that will be used.
api_url = config["API_URL"]
acces_token = config["ACCESS_TOKEN"]
headers = {'Authorization': f'Bearer {acces_token}'}
verify_token = config["VERIFY_TOKEN"]

"""
API router to send messages
"""
messages_router = APIRouter()

#Endpoint to send a simple messages.
@messages_router.post("/simple_message")
async def send_simple_message(message: schema.simple_message):

    """
    Create a intance of the class SimpleMessage to create the structure of the json_response for a simple menssage.
    The variables that the class is going to take come from a dict/json that has the structure defined in schema.py

    Parameters:
    ----------
    message: dict
        a dict with the structure "simple_message" defined in schema.py

    Returns:
    -------
    renponse: json response
    """
    # Intance the SimpleMessage class and use the method to_dict() to create the data for the htpp request.
    data = json_templates.SimpleMessage(**message.dict()).to_dict()

    # Send the request
    try:
        response = requests.post(api_url, headers=headers, json=data)
        response.raise_for_status()

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error sending message: {str(e)}")
    return response.json()


@messages_router.post("/interactive_button_message")
async def send_interactive_button_message(message: schema.button_message):

    """
    Create a intance of the class InteractiveButtonMessage to create the structure of the json_response for a simple menssage.
    The variables that the class is going to take come from a dict/json that has the structure defined in schema.py
    
    Parameters:
    ----------
    message: dict
        a dict with the structure "simple_message" defined in schema.py

    Returns:
    -------
    renponse: json response
    """
    # Intance the SimpleMessage class and use the method to_dict() to create the data for the htpp request.
    data = json_templates.InteractiveButtonMessage(**message.dict()).to_dict()

    # Send the request
    try:
        response = requests.post(api_url, headers=headers, json=data)
        response.raise_for_status()

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error sending message: {str(e)}")
    return response.json()

