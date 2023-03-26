from sqlalchemy import Column, Integer, String, ForeignKey, Date, Time, create_engine, DateTime, BigInteger
from sqlalchemy.orm import relationship
from database import Base

class appointments(Base):
    __tablename__ = "appointments"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    idpersona = Column(Integer)
    OsId = Column(Integer)
    date_only = Column(Date)
    time_only = Column(Time)
    last_name = Column(String)
    first_name = Column(String)
    rrhhid = Column(Integer)
    
class patient_contact_info(Base):
    __tablename__ = 'patient_contact_info'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    idpersona = Column(Integer)
    persCelular = Column(BigInteger)
    persmail = Column(String)


class confirmations(Base):
    __tablename__ = "confirmations"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    idpersona = Column(Integer)
    first_name = Column(String)
    last_name= Column(String)
    date_only= Column(Date)
    time_only= Column(Time)
    persCelular = Column(BigInteger)
    status = Column(String, default="Pendiente")

class forms_send(Base):
    __tablename__ = "forms_send"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    idpersona = Column(Integer)
    persCelular = Column(BigInteger)
