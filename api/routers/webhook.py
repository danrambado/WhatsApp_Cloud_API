#Python
import json

#FastAPI
from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse

#Open the json configuration parameters
with open('api/config/config.json') as f:
    config = json.load(f)

#Define the config parameters that will be used.
verify_token = config["VERIFY_TOKEN"]

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
        if request.query_params.get('hub.verify_token') == config["VERIFY_TOKEN"]:
            return int(request.query_params.get('hub.challenge'))
        return JSONResponse(content={"error": "Authentication failed. Invalid Token."}, status_code=400)

@webhook_router.post("/webhook/")
async def handle_webhooks(request: Request):
    print(await request.json())
    res = await request.json()
    print(type(res))
