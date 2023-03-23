#Python
import requests

#FastAPI
from fastapi import APIRouter, HTTPException

#env
from templates_messges import text_templates


mass_messages_router = APIRouter()

@mass_messages_router.get("/mass_messages")
async def mass_messages():
    print("ayuda")
    payload = {'to': 541133149984,
              'header_text': 'Confirmación de turno | Cardiología',
              'body_text': 'Estimado/a paciente este mensaje _automático_un es para confirmar su turno médico programado para el día *jaja* a las *jajahs*. Le recomendamos llegar con 10 minutos de anticipación. Por favor seleccione la opcion deseada.',
              'footer_text': 'Cardiología IAF',
              'reply_buttons': {'button_1': 'Confirmar turno',
                'button_2': 'Cancelar turno',
                'button_3': 'Reprogramar turno'}
                }
    url= 'http://localhost:8000/interactive_button_message'
    headers = {
    'accept': 'application/json',
    'Content-Type': 'application/json'
    }
    text = text_templates.ButtonMessages(541133149984)
    payload = text.confirmation_message("jaja", "jaja")
    response = requests.post(url, headers=headers, json=payload)

