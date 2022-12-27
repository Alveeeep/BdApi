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
def get_all(db: Session, key):
    return db.query(key).all()


# Получить определенную строку из таблицы по id
def get_by_id(db: Session, key, item_id: int):
    res = db.query(key).filter(key.id == item_id).first()
    if res is None:
        return []
    return res

