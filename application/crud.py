from sqlalchemy.orm import Session

from . import models, schemas

tags = {
    "banner": models.MainPageBanner,
    "blog": models.Blog,
    "vacancies": models.Vacancies,
    "phone": models.Phones,
    "addresses": models.Addresses,
    "objects": models.Objects
}


# Получить все данные из таблицы из словаря tags
def get_all(db: Session, key: str):
    return db.query(tags[key]).all()


# Получить определенную строку из таблицы по id
def get_by_id(db: Session, key: str, item_id: int):
    return db.query(tags[key]).filter(tags[key].id == item_id).first()

