from datetime import date, timedelta
from typing import List
from datetime import datetime, time
from sqlalchemy import func, asc, and_
from sqlalchemy.orm import Session, aliased
from sqlalchemy.sql.expression import select
from fastapi import FastAPI, HTTPException
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
        )
        db.add(db_item)
    db.commit()
    return 


def read_idpersona(db: Session, idpersona):
    paciente = db.query(models.patient_contact_info).filter(models.patient_contact_info.idpersona == idpersona).first()
    if paciente is None:
        return False
    return True

def create_patient_info(db: Session, patien_info):
    db_item = models.patient_contact_info(**patien_info)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def filter_appointments(db: Session, date: date):
    subquery = (
        db.query(
            models.appointments.idpersona,
            models.appointments.date_only,
            models.appointments.first_name,
            models.appointments.last_name,
            func.min(models.appointments.time_only).label("min_time_only"),
        )
        .filter(models.appointments.date_only == date)
        .group_by(
            models.appointments.idpersona, 
            models.appointments.date_only,
            models.appointments.first_name,
            models.appointments.last_name,
        )
        .subquery()
    )

    subquery_alias = aliased(models.appointments, subquery)

    results = (
    db.query(
        models.appointments.idpersona.distinct(),
        models.appointments.first_name,
        models.appointments.last_name,
        subquery.c.date_only,
        subquery.c.min_time_only,
        models.patient_contact_info.persCelular,
    )
    .join(models.patient_contact_info, models.appointments.idpersona == models.patient_contact_info.idpersona)
    .join(subquery_alias, and_(models.appointments.idpersona == subquery_alias.idpersona, models.appointments.time_only == subquery.c.min_time_only))
    .all()
    )

    # Devolver los resultados en una lista de objetos FilteredAppointment
    appointments = []
    for resultado in results:
        appointment = {
            'idpersona': resultado[0],
            'first_name': resultado[1],
            'last_name': resultado[2],
            'date_only': resultado[3],
            'time_only': resultado[4],
            'persCelular': resultado[5],
        }
        appointments.append(appointment)
    return appointments

def save_confirmations(db: Session, confirmations_list):
    for confirmation in confirmations_list:
        confirmation_record = models.confirmations(
            idpersona=confirmation["idpersona"],
            first_name=confirmation["first_name"],
            last_name=confirmation["last_name"],
            date_only=confirmation["date_only"],
            time_only=confirmation["time_only"],
            persCelular=confirmation["persCelular"]
        )
        db.add(confirmation_record)
    db.commit()
    db.refresh

    return "confirmation saved"

def consult_confirmations(db: Session, date):
    result = db.query(models.confirmations).filter(models.confirmations.date_only == date).all()
    return result

def update_status_confirmation(db: Session, id, status):

    confirmation = db.query(models.confirmations).filter(models.confirmations.persCelular == id).first()
    confirmation.status = status
    db.commit()
