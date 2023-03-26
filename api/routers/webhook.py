#Python
import json, os

#FastAPI
from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse

#env
from config.config import whatsappcloudapi
from services import webhook_utils
from routers import db_manage 
from routers import send_messages
from templates_messges import text_templates

#Define the config parameters that will be used.
verify_token = whatsappcloudapi.VERIFY_TOKEN

"""
API router to handle the WhatsApp webhook 
"""
webhook_router = APIRouter()

@webhook_router.get("/webhook/")
async def verify_token_webhook(request: Request):
    """
    Endpoint [GET] to verify the webhook token

    Parameters:
    ----------
    request: Request
        Request structure from fastAPI.
    
    Returns:
    -------
    JSONResponse
    """

    if request.method == "GET":
        if request.query_params.get('hub.verify_token') == verify_token:
            return int(request.query_params.get('hub.challenge'))
        return JSONResponse(content={"error": "Authentication failed. Invalid Token."}, status_code=400)

@webhook_router.post("/webhook/")
async def handle_webhooks(request: Request):
    res = await request.json()

    result = webhook_utils.process_patient_response(res)

    if result is not None:
        button_payload, wa_id = result

        await db_manage.update_status_confirmation_by_wa_id(wa_id=wa_id, status=button_payload, request=request)

        button_payload_map = {
            "Reprogramar": text_templates.TextMessages(wa_id).reschedule_bye,
            "Cancelar": text_templates.TextMessages(wa_id).cancellation_bye,
        }

        if button_payload == "Confirmar":
            exists = await db_manage.check_form_send(wa_id=wa_id, request=request)

            if not exists:
                await send_messages.send_simple_message(text_templates.TextMessages(wa_id).form())
                await db_manage.create_form_send(wa_id=wa_id, request=request)

            await send_messages.send_simple_message(text_templates.TextMessages(wa_id).confirmation_bye())

        elif button_payload in button_payload_map:
            await send_messages.send_simple_message(button_payload_map[button_payload]())

    



   






