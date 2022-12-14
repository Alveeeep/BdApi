from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

from . import tags

db_data = tags.get_db_data()

SQLALCHEMY_DATABASE_URL = "postgresql://{0}:{1}@{2}/{3}".format(db_data["login"], db_data["password"],
                                                                db_data["ip"], db_data["name"])
engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)

Base = declarative_base()

SessionLocal = sessionmaker(autoflush=False, bind=engine)
