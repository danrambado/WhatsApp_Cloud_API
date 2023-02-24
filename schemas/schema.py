# Python
from typing import Optional, List

# Pydantic
from pydantic import BaseModel

class simple_message(BaseModel):
    to: int 
    body: str

class button_message(BaseModel):
    to: int
    header_text: str
    body_text: str
    footer_text: str
    reply_buttons: dict