from fastapi import APIRouter, Depends
from . import models, schemas
from application import crud
from application.database import SessionLocal, engine, get_db
from sqlalchemy.orm import Session

router = APIRouter()

get_db()
path = "/api"


@router.get(path + "/banner", tags=["Get all"], response_model=list[schemas.MainPageBanner])
def get_all_banner(db: Session = Depends(get_db)):
    return crud.get_all(db, models.MainPageBanner)


@router.get(path + "/blog", tags=["Get all"], response_model=list[schemas.Blog])
def get_all_blogs(db: Session = Depends(get_db)):
    return crud.get_all(db, models.Blog)


@router.get(path + "/footer_phones", tags=["Get all"], response_model=list[schemas.Phones])
def get_all_phones(db: Session = Depends(get_db)):
    return crud.get_all(db, models.Phones)


@router.get(path + "/footer_addresses", tags=["Get all"], response_model=list[schemas.Addresses])
def get_all_addresses(db: Session = Depends(get_db)):
    return crud.get_all(db, models.Addresses)


@router.get(path + "/footer_objects", tags=["Get all"], response_model=list[schemas.Objects])
def get_all_objects(db: Session = Depends(get_db)):
    return crud.get_all(db, models.Objects)


@router.get(path + "/vacancies", tags=["Get all"], response_model=list[schemas.Vacancies])
def get_all_vacancies(db: Session = Depends(get_db)):
    return crud.get_all(db, models.Vacancies)


@router.get(path + "/banner/{id}", tags=["Get by id"], response_model=schemas.MainPageBanner)
def get_id_banner(id: int, db: Session = Depends(get_db)):
    return crud.get_by_id(db, models.MainPageBanner, id)


@router.get(path + "/blog/{id}", tags=["Get by id"], response_model=schemas.Blog)
def get_id_blog(id: int, db: Session = Depends(get_db)):
    return crud.get_by_id(db, models.Blog, id)


@router.get(path + "/vacancies/{id}", tags=["Get by id"], response_model=schemas.Vacancies)
def get_id_vacancies(id: int, db: Session = Depends(get_db)):
    return crud.get_by_id(db, models.Vacancies, id)


@router.get(path + "/footer_phones/{id}", tags=["Get by id"], response_model=schemas.Phones)
def get_id_phones(id: int, db: Session = Depends(get_db)):
    return crud.get_by_id(db, models.Phones, id)


@router.get(path + "/footer_addresses/{id}", tags=["Get by id"], response_model=schemas.Addresses)
def get_id_addresses(id: int, db: Session = Depends(get_db)):
    return crud.get_by_id(db, models.Addresses, id)


@router.get(path + "/footer_objects/{id}", tags=["Get by id"], response_model=schemas.Objects)
def get_id_objects(id: int, db: Session = Depends(get_db)):
    return crud.get_by_id(db, models.Objects, id)
