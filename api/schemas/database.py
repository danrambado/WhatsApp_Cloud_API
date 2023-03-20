from datetime import datetime
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