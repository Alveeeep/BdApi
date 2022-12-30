from sqlalchemy import Column, Integer, String, Text, TIMESTAMP, BIGINT
from enum import Enum
from database import Base


class MainPageBanner(Base):
    __tablename__ = "banner"

    id = Column(Integer, primary_key=True)
    title = Column(String(255))
    description = Column(Text)
    image_left = Column(String(255))
    image_right = Column(String(255))


class Blog(Base):
    __tablename__ = "blog"

    id = Column(Integer, primary_key=True)
    title = Column(String(255))
    description = Column(Text)
    image = Column(String(255))
    date = Column(TIMESTAMP)


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


class Promotions(Base):
    __tablename__ = "current_promotions"

    id = Column(Integer, primary_key=True)
    title = Column(String(255))
    description = Column(Text)
    image = Column(String(255))
    date = Column(TIMESTAMP)


class PickUpPoints(Base):
    __tablename__ = "pick_up_points"

    id = Column(Integer, primary_key=True)
    phone1 = Column(Text)
    phone2 = Column(Text)
    email = Column(Text)
    pick_up_points_time_id = Column(BIGINT)


class PickUpPointsTimes(Base):
    __tablename__ = "pick_up_points_times"

    id = Column(Integer, primary_key=True)
    mon = Column(Text)
    tue = Column(Text)
    wen = Column(Text)
    thu = Column(Text)
    fri = Column(Text)
    sat = Column(Text)
    sun = Column(Text)


class TableName(str, Enum):
    banner = "banner"
    blog = "blog"
    vacancies = "vacancies"
    phones = "phone"
    address = "addresses"
    object = "objects"
    promotions = "promotions"
