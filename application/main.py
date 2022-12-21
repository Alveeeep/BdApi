from fastapi import FastAPI

from . import models
from application.database import engine
from . import routers

from . import tags

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="BdAPIApp",
    description=tags.description,
    version="0.1",
    openapi_tags=tags.tags_metadata
)

app.include_router(routers.router)
