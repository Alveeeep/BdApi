from sqlalchemy.orm import Session
from fastapi import Depends, FastAPI, Body

from . import models, schemas
from application import crud
from application.database import SessionLocal, engine

from . import tags

models.Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="BdAPIApp",
    description=tags.description,
    version="0.1",
    openapi_tags=tags.tags_metadata
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/api/{table_name}", tags=["Get all"])
def get_all_from_table(table_name: models.TableName, db: Session = Depends(get_db)):
    tables = crud.get_all(db, key=table_name.value)
    return tables


@app.get("/api/{table_name}/{id}", tags=["Get by id"])
def get_by_id(table_name: models.TableName, id, db: Session = Depends(get_db)):
    table = crud.get_by_id(db, key=table_name.value, item_id=id)
    return table


@app.post("/api/{table_name}", tags=["Post"])
def create_in_table(table_name: models.TableName, data=Body(), db: Session = Depends(get_db)):
    new_string = crud.create_new(db, key=table_name.value, item=data)
    return new_string


@app.put("/api/{table_name}", tags=["Update"])
def edit_in_table(table_name: models.TableName, data=Body(), db: Session = Depends(get_db)):
    updated_string = crud.update_current(db, key=table_name.value, item=data)
    return updated_string


@app.delete("/api/{table_name}/{id}", tags=["Delete"])
def delete_from_table(table_name: models.TableName, id, db: Session = Depends(get_db)):
    deleted = crud.delete_by_id(db, key=table_name.value, item_id=id)
    return deleted

