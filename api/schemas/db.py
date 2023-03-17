from pydantic import BaseModel

class appoinments(BaseModel):
    id: int
    date: str
    time: int
    patien_name: str
    phone_number: int
    rrhh:  str
    status: str