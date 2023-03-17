from sqlalchemy.orm import Session
from models import models
from schemas import db

def create_appointment():
    




def get_patien_name(db: Session, user_id: int):
    return db.query(models.patien_name).filter(models.User.id == user_id).first()