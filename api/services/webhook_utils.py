from typing import Dict, Union, Tuple

def process_patient_response(webhook_data: Dict) -> Union[Tuple[str, str], None]:

    """Iterate over the whatapp json response and search if there is an 
    interactive response of type button, if found it returns the id of 
    the button and the number of the person who answered. If not return the status of messages

    Args:
        webhook_data (dict): Dictionary representing the WhatsApp webhook data.

    Returns:
        button_reply.id: type of reply
        wa_id: whatsapp id of the sender
    """
    
    # print(webhook_data)
    entries = webhook_data.get("entry", [])

    for entry in entries:
        changes = entry.get("changes", [])

        for change in changes:
            value = change.get("value", {})
            statuses = value.get("statuses", [])
            messages = value.get("messages", [])

            if statuses:
                for status in statuses:
                    wa_id = status.get("recipient_id")
                    mensaje_status = status.get("status")

                    if wa_id and mensaje_status:
                        print(f"El mensaje {mensaje_status} a {wa_id}")
                    else:
                        print("No se pudo extraer la información de status o wa_id")
            
            elif messages:
                for message in messages:
                    button = message.get("button", {})
                    button_payload = button.get("payload")
                    wa_id = message.get("from")

                    if button_payload and wa_id:
                        return button_payload, wa_id
                        # print(f"button payload: {button_payload}, wa_id: {wa_id}")
                    else:
                        print("No se pudo extraer la información de button payload o wa_id")
            else:
                print("No se encontraron mensajes válidos")
