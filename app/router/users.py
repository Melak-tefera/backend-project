from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.model import User
from app.schema import Usercreate, Userread

router = APIRouter(prefix='/users', tags=['users'])

@router.get("", response_model=list[Userread])
def get_users(db:Session=Depends(get_db)):
    users = db.query(User).all()
    return [{"id": u.id, "name": u.name} for u in users]


@router.post("", response_model=Usercreate,status_code=201)
def add_user(name: str, db: Session=Depends(get_db)):
    user = User(name=name)
    db.add(user)
    db.commit()
    db.refresh(user)
    return {"id": user.id, "name": user.name}

@router.get("/{id}", response_model=Userread)
def get_user_by_id(id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == id).first()

    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    return user