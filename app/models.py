from pydantic import BaseModel


class pacient_info(BaseModel):
    number: int 
    date: str
    time: str




class MessageBase(BaseModel):
    messaging_product: str = "whatsapp"
    recipient_type: str = "individual"
    to: str
    type: str

class TextMessage(MessageBase):
    type: str = "text"
    text: dict = { 
        "preview_url": False,
        "body": "MESSAGE_CONTENT"
    }

class InteractiveMessage(MessageBase):
    type: str = "interactive"
    interactive: dict = {
            "type": "button",
            "body": {
                "text": "Text"
            },
            "action": {
                "buttons": [
                    {
                        "type": "reply",
                        "reply": {
                            "id": "UNIQUE_BUTTON_ID_1",
                            "title": "BUTTON_TITLE_1"
                        }
                    },
                    {
                        "type": "reply",
                        "reply": {
                            "id": "UNIQUE_BUTTON_ID_2",
                            "title": "BUTTON_TITLE_2"
                        }
                    }
                ]
            }
        }
    



class TemplateMessage(MessageBase):
    type = "template"
    template_data: dict