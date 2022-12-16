from sqlalchemy import Column, Integer, String
from enum import Enum
from application.database import Base


class MainPageBanner(Base):
    __tablename__ = "banner"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    image_left = Column(String)
    image_right = Column(String)
    background_color = Column(String)


class Blog(Base):
    __tablename__ = "blog"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    image = Column(String)


class Vacancies(Base):
    __tablename__ = "vacancies"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    phone = Column(String)
    email = Column(String)


class Phones(Base):
    __tablename__ = "footer_phones"

    id = Column(Integer, primary_key=True)
    phone = Column(String)


class Addresses(Base):
    __tablename__ = "footer_addresses"

    id = Column(Integer, primary_key=True)
    address = Column(String)


class Objects(Base):
    __tablename__ = "footer_objects"

    id = Column(Integer, primary_key=True)
    object = Column(String)


class TableName(str, Enum):
    banner = "banner"
    blog = "blog"
    vacancies = "vacancies"
    phones = "phone"
    address = "addresses"
    object = "objects"
