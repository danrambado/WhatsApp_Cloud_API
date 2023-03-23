from datetime import datetime, date, time
from pydantic import BaseModel

class appointments(BaseModel):
    idpersona: int
    OsId: int
    date_only: datetime
    time_only: datetime
    last_name: str
    first_name: str
    rrhhid: int
    status: str = "Pendiente"

class patient_contact_info(BaseModel):
    idpersona: int
    persmail: str
    persCelular: str


class FilteredAppointment(BaseModel):
    idpersona: int
    first_name: str
    last_name= str
    date_only: date
    time_only: time
    persCelular: int
