

from fastapi import FastAPI
from app.database import engine, Base
from app.model import User
from app.router import users



Base.metadata.create_all(engine)
app = FastAPI()
app.include_router(users.router)



