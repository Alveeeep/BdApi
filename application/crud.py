from sqlalchemy.orm import Session

from . import dto

tags = {
    "banner": dto.MainPageBanner,
    "blog": dto.Blog,
    "vacancies": dto.Vacancies,
    "phone": dto.Phones,
    "addresses": dto.Addresses,
    "objects": dto.Objects
}


# Получить все данные из таблицы из словаря tags
def get_all(db: Session, key: str):
    return db.query(tags[key]).all()


# Получить определенную строку из таблицы по id
def get_by_id(db: Session, key: str, item_id: int):
    return db.query(tags[key]).filter(tags[key].id == item_id).first()

