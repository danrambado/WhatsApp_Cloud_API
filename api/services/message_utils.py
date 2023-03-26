import requests
import json

def send_template_message_confirmation(url, access_token, number, date, time, name):
    # Definir los datos de la petición en formato JSON
    data = {
        "messaging_product": "whatsapp", 
        "to": number,
        "type": "template", 
         "template": {
            "name": "confirmation",
            "language": {
                "code": "es_AR"
            },
            "components": [
                {
                    "type": "body",
                    "parameters": [
                       {
                            "type": "text",
                            "text": date,
                        },
                        {
                            "type": "text",
                            "text": time
                        },
                        {
                            "type": "text",
                            "text": name
                        }
                    ]
                }
            ]
        }
    }
    
    # Convertir los datos a formato JSON y enviar la petición POST
    response = requests.post(
        url= url,
        headers={
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json"
        },
        data=json.dumps(data)
    )
    
    # Procesar la respuesta para obtener el valor de wa_id
    if response.status_code == 200:
        response_data = json.loads(response.content)
        wa_id = response_data["contacts"][0]["wa_id"]
        print(f"Mensaje enviado con éxito. wa_id: {wa_id}")
        return wa_id
    else:
        print(f"Error al enviar mensaje: {response.content}")
        return None
    