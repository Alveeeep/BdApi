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


# Добавление в таблицу
def create_new(db: Session, key: str, item):
    model = tags[key]
    db_item = model(**item)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def update_current(db: Session, key: str, item):
    db_item = db.query(tags[key]).filter(tags[key].id == item["id"]).first()
    for el in item.keys():
        setattr(db_item, el, item[el])
    db.commit()
    db.refresh(db_item)
    return db_item


def delete_by_id(db: Session, key: str, item_id: int):
    db_item = db.query(tags[key]).filter(tags[key].id == item_id).first()
    db.delete(db_item)
    db.commit()
    return db_item
