from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config.config import dbsettings 


SQLALCHEMY_DATABASE_URL = f"postgresql://{dbsettings.POSTGRES_USER}:{dbsettings.POSTGRES_PASSWORD}@{dbsettings.POSTGRES_HOSTNAME}:{dbsettings.DATABASE_PORT}/{dbsettings.POSTGRES_DB}"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    echo= True
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
def get_db_async():
    db = SessionLocal()
    return db


