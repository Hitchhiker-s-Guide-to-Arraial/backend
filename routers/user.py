from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.database import get_db
from schemas.user import UserCreate, UserLogin
from services.userService import create_user, authenticate_user
import jwt

router = APIRouter(tags=["User"])

@router.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):
    db_user = create_user(user, db)
    return {"id": db_user.id, "name": db_user.name, "email": db_user.email}

@router.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):
    db_user = authenticate_user(user, db)
    if not db_user:
        raise HTTPException(status_code=400, detail="Invalid credentials")
    token = jwt.encode({"sub": user.email}, "secret", algorithm="HS256")

    return {"id": db_user.id, "name": db_user.name, "email": db_user.email, "token": token}
