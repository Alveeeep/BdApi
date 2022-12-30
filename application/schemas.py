from typing import Optional
from pydantic import BaseModel


class MainModel(BaseModel):
    id: int
    title: Optional[str]

    class Config:
        orm_mode = True


class MainPageBannerDTO(MainModel):
    description: Optional[str]
    image_left: Optional[str]
    image_right: Optional[str]


class BlogDTO(MainModel):
    description: Optional[str]
    image: Optional[str]
    date: Optional[str]


class VacanciesDTO(MainModel):
    phone_one: Optional[str]
    phone_two: Optional[str]
    email: Optional[str]


class PromotionsDTO(MainModel):
    description: Optional[str]
    image: Optional[str]
    date: Optional[str]


class Footer(BaseModel):
    id: int

    class Config:
        orm_mode = True


class PhonesDTO(Footer):
    phone: Optional[str]


class AddressesDTO(Footer):
    address: Optional[str]


class ObjectsDTO(Footer):
    icon: Optional[str]
    link: Optional[str]


class PickUpPointsDTO(Footer):
    phone1: Optional[str]
    phone2: Optional[str]
    email: Optional[str]
    pick_up_points_time_id: Optional[int]


class PickUpPointsTimesDTO(Footer):
    mon: Optional[str]
    tue: Optional[str]
    wen: Optional[str]
    thu: Optional[str]
    fri: Optional[str]
    sat: Optional[str]
    sun: Optional[str]
