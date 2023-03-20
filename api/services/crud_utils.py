from typing import List
from datetime import datetime, time
from sqlalchemy.orm import Session
from models import models
from schemas import database

def create_appointment(db: Session, appointment_list: List[dict]):
    for item in appointment_list:
        date_only = datetime.strptime(item['date_only'], '%Y-%m-%d').date()
        time_only = datetime.strptime(item['time_only'], '%H:%M').time()
        datetime_obj = datetime.combine(date_only, time_only)
        db_item = models.appointments(
            idpersona=item['idpersona'],
            OsId=item['OsId'],
            date_only=date_only,
            time_only=time_only,
            last_name=item['last_name'],
            first_name=item['first_name'],
            rrhhid=item['rrhhid'],
            status=item.get('status', 'Pendiente')
        )
        db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


# def read_idpersona(db: Session, idpersona):









# # def get_patien_name(db: Session, user_id: int):
#     return db.query(models.patien_name).filter(models.User.id == user_id).first()
    