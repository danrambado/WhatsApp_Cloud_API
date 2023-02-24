# Python
from typing import Optional, List

# Pydantic
from pydantic import BaseModel, constr, validator


class simple_message(BaseModel):
    to: int 
    body: str

class buttons(BaseModel):
    button1: str = None
    button2: Optional[str] = None
    button3: Optional[str] = None


class button_message(BaseModel):
    to: int
    header_text: str
    body_text: str
    footer_text: str
    reply_buttons: dict