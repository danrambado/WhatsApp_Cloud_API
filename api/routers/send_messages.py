#Python
import requests
import json
import datetime
from datetime import date
from typing import Callable
import httpx
from httpx import AsyncClient


#FastAPI
from fastapi import APIRouter, HTTPException, Request

#env
from config.config import whatsappcloudapi
from schemas import messages
from routers import db_manage
from services import message_utils
from templates_messges import json_templates

#Define the config parameters that will be used.
api_url = whatsappcloudapi.API_URL
acces_token = whatsappcloudapi.ACCESS_TOKEN
headers = {'Authorization': f'Bearer {acces_token}'}

"""
API router to send messages
"""
messages_router = APIRouter()

# send_messages.py
@messages_router.get("/send_template_message_confirmation")
async def send_template_message_confirmation(date: date, request: Request):
    """
    Sends confirmation messages through WhatsApp using a predefined template for a specific date and time. 
    Retrieves a list of confirmations from the database based on the given date and request. It then iterates 
    over each item in the confirmation list and extracts necessary information such as the person's ID, mobile phone number, 
    name, date, and time. Uses an external function "message_utils.send_template_message_confirmation" to 
    send the confirmation message using the extracted information and the predefined message template. If the message is sent 
    successfully, the function updates the confirmation status in the database as "Sent," and if there is an error, the status is 
    updated as "Error - Check Number."

    Args:
        date (date): _description_
        request (Request): _description_

    Returns:
        _type_: _description_
    """

    # Get list of confirmations based on date
    confirmations = await db_manage.get_confirmations(date=date, request=request)

    # Iterate over the list and send the template message "confirmation".
    for confirmation in confirmations:
        idpersona = confirmation.idpersona
        time_only = confirmation.time_only.strftime('%H:%M')
        first_name = confirmation.first_name
        date_only = confirmation.date_only.strftime('%d-%m-%Y')
        persCelular = confirmation.persCelular

        # If the message was sent, you get the "wa_id" otherwise it returns none.
        wa_id = message_utils.send_template_message_confirmation(
            url=whatsappcloudapi.API_URL,
            access_token= whatsappcloudapi.ACCESS_TOKEN,
            number= persCelular,
            date=date_only,
            time=time_only,
            name=first_name
        )
        # Important: In the IAF database the numbers have different formats. 
        # So I simply let WhatsApp take care of verifying that it is a valid number. 
        # If the number is valid the message will be sent and I can get the "wa_id", which is the 
        # identifier that WhatsApp uses internally.

        if wa_id:
            status= "Enviado"
            # Update "perCelular" in the confirmations table to be able to filter a response later.
            await db_manage.update_percelular_confirmation(idpersona=idpersona, wa_id=wa_id, request=request)
            # Update "status" == Enviado in the confirmations table.
            await db_manage.update_status_confirmation(idpersona=idpersona, status=status, request=request)
        else:
            status= "Error - Revisar numero"
            # Update "status" == Error - Revisar numero in the confirmations table.
            await db_manage.update_status_confirmation(idpersona=idpersona, status=status, request=request)

    return confirmations


#Endpoint to send a simple messages.
@messages_router.post("/simple_message")
async def send_simple_message(message: messages.simple_message):

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
    # Intance the SimpleMessage class and use the method to_dict() to create the data for the http request.
    if isinstance(message, messages.simple_message):
        if hasattr(message, 'to') and hasattr(message, 'body'):  # Revisa si message tiene los atributos 'to' y 'body'
            data = json_templates.SimpleMessage(
                to=message.to,  # Usa 'message.to'
                body=message.body   # Usa 'message.body'
            ).to_dict()
        else:
            raise AttributeError('message object is missing to or body attribute')
    elif isinstance(message, dict):
        data = json_templates.SimpleMessage(**message).to_dict()
    else:
        raise TypeError('message must be either a messages.simple_message instance or a dict')




    # Send the request
    try:
        async with AsyncClient() as client:
            response = await client.post(api_url, headers=headers, json=data)
        response.raise_for_status()

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error sending message: {str(e)}")
    return response.json()
