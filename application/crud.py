from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import declarative_base
from fastapi import HTTPException


# Получить все данные из таблицы из словаря tags
def get_all(db: Session, key: declarative_base):
    return db.query(key).all()


# Получить определенную строку из таблицы по id
def get_by_id(db: Session, key: declarative_base, item_id: int):
    res = db.query(key).filter(key.id == item_id).first()
    if res is None:
        raise HTTPException(status_code=404, detail="Not found")
    return res
