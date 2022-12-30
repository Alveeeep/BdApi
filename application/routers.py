from fastapi import APIRouter, Depends
from models import MainPageBanner, Blog, Phones, Addresses, Objects, Vacancies, Promotions, PickUpPoints, \
    PickUpPointsTimes
from schemas import MainPageBannerDTO, BlogDTO, PhonesDTO, AddressesDTO, ObjectsDTO, VacanciesDTO, PromotionsDTO, \
    PickUpPointsDTO, PickUpPointsTimesDTO
from crud import get_all, get_by_id
from database import get_db
from sqlalchemy.orm import Session

router = APIRouter()

get_db()
path = "/api"


@router.get(path + "/banner", tags=["Get all"], response_model=list[MainPageBannerDTO])
def get_all_banner(db: Session = Depends(get_db)):
    return get_all(db, MainPageBanner)


@router.get(path + "/blog", tags=["Get all"], response_model=list[BlogDTO])
def get_all_blogs(db: Session = Depends(get_db)):
    return get_all(db, Blog)


@router.get(path + "/footer_phones", tags=["Get all"], response_model=list[PhonesDTO])
def get_all_phones(db: Session = Depends(get_db)):
    return get_all(db, Phones)


@router.get(path + "/footer_addresses", tags=["Get all"], response_model=list[AddressesDTO])
def get_all_addresses(db: Session = Depends(get_db)):
    return get_all(db, Addresses)


@router.get(path + "/footer_objects", tags=["Get all"], response_model=list[ObjectsDTO])
def get_all_objects(db: Session = Depends(get_db)):
    return get_all(db, Objects)


@router.get(path + "/vacancies", tags=["Get all"], response_model=list[VacanciesDTO])
def get_all_vacancies(db: Session = Depends(get_db)):
    return get_all(db, Vacancies)


@router.get(path + "/promotions", tags=["Get all"], response_model=list[PromotionsDTO])
def get_all_promotions(db: Session = Depends(get_db)):
    return get_all(db, Promotions)


@router.get(path + "/pick_up_points", tags=["Get all"], response_model=list[PickUpPointsDTO])
def get_all_pick_up_points(db: Session = Depends(get_db)):
    return get_all(db, PickUpPoints)


@router.get(path + "/pick_up_points_times", tags=["Get all"], response_model=list[PickUpPointsTimesDTO])
def get_all_pick_up_points_times(db: Session = Depends(get_db)):
    return get_all(db, PickUpPointsTimes)


@router.get(path + "/banner/{id}", tags=["Get by id"], response_model=MainPageBannerDTO)
def get_id_banner(id: int, db: Session = Depends(get_db)):
    return get_by_id(db, MainPageBanner, id)


@router.get(path + "/blog/{id}", tags=["Get by id"], response_model=BlogDTO)
def get_id_blog(id: int, db: Session = Depends(get_db)):
    return get_by_id(db, Blog, id)


@router.get(path + "/vacancies/{id}", tags=["Get by id"], response_model=VacanciesDTO)
def get_id_vacancies(id: int, db: Session = Depends(get_db)):
    return get_by_id(db, Vacancies, id)


@router.get(path + "/footer_phones/{id}", tags=["Get by id"], response_model=PhonesDTO)
def get_id_phones(id: int, db: Session = Depends(get_db)):
    return get_by_id(db, Phones, id)


@router.get(path + "/footer_addresses/{id}", tags=["Get by id"], response_model=AddressesDTO)
def get_id_addresses(id: int, db: Session = Depends(get_db)):
    return get_by_id(db, Addresses, id)


@router.get(path + "/footer_objects/{id}", tags=["Get by id"], response_model=ObjectsDTO)
def get_id_objects(id: int, db: Session = Depends(get_db)):
    return get_by_id(db, Objects, id)


@router.get(path + "/promotions/{id}", tags=["Get by id"], response_model=PromotionsDTO)
def get_id_promotions(id: int, db: Session = Depends(get_db)):
    return get_by_id(db, Promotions, id)


@router.get(path + "/pick_up_points", tags=["Get all"], response_model=PickUpPointsDTO)
def get_id_pick_up_points(db: Session = Depends(get_db)):
    return get_by_id(db, PickUpPoints)


@router.get(path + "/pick_up_points_times", tags=["Get all"], response_model=PickUpPointsTimesDTO)
def get_id_pick_up_points_times(db: Session = Depends(get_db)):
    return get_by_id(db, PickUpPointsTimes)
