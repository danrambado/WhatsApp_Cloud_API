from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config.config import Dbsettings 


SQLALCHEMY_DATABASE_URL = f"postgresql://{Dbsettings.POSTGRES_USER}:{Dbsettings.POSTGRES_PASSWORD}@{Dbsettings.POSTGRES_HOSTNAME}:{Dbsettings.DATABASE_PORT}/{Dbsettings.POSTGRES_DB}"

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

