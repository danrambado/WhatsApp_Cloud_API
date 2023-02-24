# Here are the templates of the messages to be sent 


# The json data to send message must have the following structure according to 
# the WhatsApp Business Platform Cloud API documentation (https://developers.facebook.com/docs/whatsapp/cloud-api/guides/send-messages)
# None values are to be considered variables that need to be filled in when using the template.

from typing import List, Dict, Any

class BaseMessage:
    """Base class for WhatsApp messages"""
    def __init__(self, messaging_product: str, recipient_type: str, to: int, message_type: str):
        """
        Parameters:
        messaging_product (str): The messaging product (e.g. 'whatsapp').
        recipient_type (str): The type of recipient (e.g. 'individual').
        to (int): The phone number of the recipient.
        message_type (str): The type of message (e.g. 'text', 'interactive', etc.).
        """
        self.messaging_product = messaging_product
        self.recipient_type = recipient_type
        self.to = to
        self.message_type = message_type

    def to_dict(self) -> dict:
        """Returns the message as a dictionary."""
        return {
            "messaging_product": self.messaging_product,
            "recipient_type": self.recipient_type,
            "to": self.to,
            "type": self.message_type
        }
    
class SimpleMessage(BaseMessage):
    """Class for simple text messages"""
    def __init__(self, to, body):
        """
        Parameters:
        to (int): The phone number of the recipient.
        body_text (str): The text for the body of the message.
        """
        super().__init__(
            messaging_product="whatsapp",
            recipient_type="individual",
            to=to,
            message_type="text"
        )
        self.text = { 
            "preview_url": False,
            "body": body
        }

    def to_dict(self):
        message = super().to_dict()
        message["text"] = self.text
        return message

class InteractiveButtonMessage(BaseMessage):
    """Class for interactive messages with buttons"""

    def __init__(self, to: int, header_text: str, body_text: str, footer_text: str, reply_buttons: Dict[str, str]):
        """
        Parameters:
        to (int): The phone number of the recipient.
        header_text (str): The text for the header of the message.
        body_text (str): The text for the body of the message.
        footer_text (str): The text for the footer of the message.
        reply_buttons (Dict[str, str]): A dictionary of reply button titles.
        """
        super().__init__(
            messaging_product="whatsapp",
            recipient_type="individual",
            to=to,
            message_type="interactive"
        )
        if len(reply_buttons) not in [1, 2, 3]:
            raise ValueError("reply_buttons must contain 1, 2 or 3 buttons")

        self.interactive = {
            "type": "button",
            "header": {
                "type": "text",
                "text": header_text
            },
            "body": {
                "text": body_text
            },
            "footer": {
                "text": footer_text
            },
            "action": {
                "buttons": [
                    {
                        "type": "reply",
                        "reply": {
                            "id": str(button_title) + "id",
                            "title": button_title
                        }
                    } for button_title in reply_buttons.values()
                ]
            }
        }

    def to_dict(self) -> Dict[str, Any]:
        message_dict = super().to_dict()
        message_dict["interactive"] = self.interactive
        return message_dict