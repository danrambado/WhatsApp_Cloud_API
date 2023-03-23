from pydantic import BaseModel
# Schemes to deserialize the incoming JSON in the request coming from WhatsApp.

# Examples of incoming JSON's from WhatsApp:
# {"object": "whatsapp_business_account", "entry": [{"id": "101265856256120", "changes": [{"value": {"messaging_product": "whatsapp", "metadata": {"display_phone_number": "5491136521909", "phone_number_id": "115128754859970"}, "contacts": [{"profile": {"name": "Dan"}, "wa_id": "5491133149984"}], "messages": [{"context": {"from": "5491136521909", "id": "wamid.HBgNNTQ5MTEzMzE0OTk4NBUCABEYEkQ4MzhFNDk1NjIyOUY5QTcxQQA="}, "from": "5491133149984", "id": "wamid.HBgNNTQ5MTEzMzE0OTk4NBUCABIYIDI2NTk0QjhCREMzRTBCQzRBNjVBOTVDNDlFQ0U2ODk4AA==", "timestamp": "1679409466", "type": "interactive", "interactive": {"type": "button_reply", "button_reply": {"id": "Confirmar turnoid", "title": "Confirmar turno"}}}]}, "field": "messages"}]}]}
# {"object": "whatsapp_business_account", "entry": [{"id": "101265856256120", "changes": [{"value": {"messaging_product": "whatsapp", "metadata": {"display_phone_number": "5491136521909", "phone_number_id": "115128754859970"}, "statuses": [{"id": "wamid.HBgNNTQ5MTEzMzE0OTk4NBUCABEYEkUwMkI3RUY2RDkwQ0UxNzA0NgA=", "status": "delivered", "timestamp": "1679319561", "recipient_id": "5491133149984", "conversation": {"id": "e4061081ec92af53fa701a2dabccd185", "origin": {"type": "business_initiated"}}, "pricing": {"billable": true, "pricing_model": "CBP", "category": "business_initiated"}}]}, "field": "messages"}]}]}


class ButtonReply(BaseModel):
    id: str
    title: str

class Interactive(BaseModel):
    type: str
    button_reply: ButtonReply

class Message(BaseModel):
    type: str
    interactive: Interactive

class Value(BaseModel):
    messaging_product: str
    metadata: dict
    contacts: list
    messages: list[Message]

class Change(BaseModel):
    value: Value
    field: str

class Entry(BaseModel):
    id: str
    changes: list[Change]

class WhatsAppWebhook(BaseModel):
    object: str
    entry: list[Entry]