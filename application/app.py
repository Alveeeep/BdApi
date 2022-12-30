from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from models import Base
from database import engine
from routers import router
import uvicorn

from tags import description, tags_metadata

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="BdAPIApp",
    description=description,
    version="0.1",
    openapi_tags=tags_metadata
)

origins = [
    "http://localhost:3000",
    "https://sparep-parts-store-alexwebdev-coder.vercel.app"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)


if __name__ == "__main__":
    uvicorn.run(app, port=8002)