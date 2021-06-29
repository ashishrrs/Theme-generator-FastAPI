from fastapi import FastAPI
import models
from routers import banner
from database import engine

app = FastAPI()

models.Base.metadata.create_all(engine)

app.include_router(banner.router)
