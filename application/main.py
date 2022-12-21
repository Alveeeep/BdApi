from sqlalchemy.orm import Session
from fastapi import Depends, FastAPI, Body

from . import models, schemas
from application import crud
from application.database import SessionLocal, engine, get_db

from . import tags

models.Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="BdAPIApp",
    description=tags.description,
    version="0.1",
    openapi_tags=tags.tags_metadata
)


get_db()


@app.get("/api/{table_name}", tags=["Get all"])
def get_all_from_table(table_name: models.TableName, db: Session = Depends(get_db)):
    tables = crud.get_all(db, key=table_name.value)
    return tables


@app.get("/api/{table_name}/{id}", tags=["Get by id"])
def get_by_id(table_name: models.TableName, id, db: Session = Depends(get_db)):
    table = crud.get_by_id(db, key=table_name.value, item_id=id)
    return table


