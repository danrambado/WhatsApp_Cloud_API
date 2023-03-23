#Python
import json, os

#FastAPI
from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse

#env
from config.config import whatsappcloudapi
from services.webhook_utils import process_patient_response


#Define the config parameters that will be used.
verify_token = whatsappcloudapi.VERIFY_TOKEN

"""
API router to handle the WhatsApp webhook 
"""
webhook_router = APIRouter()

@webhook_router.get("/webhook/")
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
        if request.query_params.get('hub.verify_token') == verify_token:
            return int(request.query_params.get('hub.challenge'))
        return JSONResponse(content={"error": "Authentication failed. Invalid Token."}, status_code=400)

@webhook_router.post("/webhook/")
async def handle_webhooks(request: Request):
    res = await request.json()

    status = process_patient_response(res)

    



   






