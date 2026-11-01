from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app.database import engine, sessionlocal, Base
from app.model import User
Base.metadata.create_all(engine)
app = FastAPI()

def get_db():
    db = sessionlocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/users")
def get_users(db:Session=Depends(get_db)):
    users = db.query(User).all()
    return [{"id": u.id, "name": u.name} for u in users]


@app.post("/users")
def add_user(name: str, db: Session=Depends(get_db)):
    user = User(name=name)
    db.add(user)
    db.commit()
    db.refresh(user)
    return {"id": user.id, "name": user.name}