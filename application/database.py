from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from . import tags
# Ту шнягу с готовой db_data добавлять не буду, гит не одобряет

db_data = tags.get_db_data()

SQLALCHEMY_DATABASE_URL = "postgresql://{0}:{1}@{2}/{3}".format(db_data["login"], db_data["password"],
                                                                db_data["ip"], db_data["name"])
engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)

Base = declarative_base()

SessionLocal = sessionmaker(autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
