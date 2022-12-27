from sqlalchemy import Column, Integer, String, Text, Date
from enum import Enum
from application.database import Base


class MainPageBanner(Base):
    __tablename__ = "banner"

    id = Column(Integer, primary_key=True)
    title = Column(String(255))
    description = Column(String(255))
    image_left = Column(String(255))
    image_right = Column(String(255))
    background_color = Column(String(20))


class Blog(Base):
    __tablename__ = "blog"

    id = Column(Integer, primary_key=True)
    title = Column(String(255))
    description = Column(String(255))
    image = Column(String(255))
    date = Column(Date)
    timezone = Column(String(120))


class Vacancies(Base):
    __tablename__ = "vacancies"

    id = Column(Integer, primary_key=True)
    title = Column(String(255))
    phone_one = Column(String(20))
    phone_two = Column(String(20))
    email = Column(String(255))


class Phones(Base):
    __tablename__ = "footer_phones"

    id = Column(Integer, primary_key=True)
    phone = Column(String(20))


class Addresses(Base):
    __tablename__ = "footer_addresses"

    id = Column(Integer, primary_key=True)
    address = Column(Text)


class Objects(Base):
    __tablename__ = "footer_objects"

    id = Column(Integer, primary_key=True)
    icon = Column(String(255))
    link = Column(String(255))


class TableName(str, Enum):
    banner = "banner"
    blog = "blog"
    vacancies = "vacancies"
    phones = "phone"
    address = "addresses"
    object = "objects"
