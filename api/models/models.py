from sqlalchemy import Column, Integer, String, ForeignKey, Date, Time, create_engine, DateTime
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
    status = Column(String, default="Pendiente")



# # Define the Patient model
# class Patient(Base):
#     __tablename__ = "patients"

#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String, nullable=False)
#     phone = Column(String, nullable=False)
#     email = Column(String, unique=True, nullable=False)
#     full_name = Column(String,unique=True, nullable=False)

# # Define the Doctor model
# class Doctor(Base):
#     __tablename__ = "doctors"

#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String, nullable=False)

# class appointments(Base):
#     __tablename__ = "appointments"

#     id = Column(Integer, primary_key=True, index=True)
#     idpersona = Column(Integer)
#     OsId = Column(Integer)
#     date_only = Column(Date)
#     time_only = Column(Time)
#     last_name = Column(String)
#     first_name = Column(String)
#     rrhhid = Column(Integer)
