from typing import Optional
from pydantic import BaseModel


class MainModel(BaseModel):
    id: int
    title: Optional[str]

    class Config:
        orm_mode = True


class MainPageBanner(MainModel):
    description: Optional[str]
    image_left: Optional[str]
    image_right: Optional[str]
    background_color: Optional[str]


class Blog(MainModel):
    description: Optional[str]
    image: Optional[str]
    date: Optional[str]


class Vacancies(MainModel):
    phone_one: Optional[str]
    phone_two: Optional[str]
    email: Optional[str]


class Footer(BaseModel):
    id: int

    class Config:
        orm_mode = True


class Phones(Footer):
    phone: Optional[str]


class Addresses(Footer):
    address: Optional[str]


class Objects(Footer):
    icon: Optional[str]
    link: Optional[str]
