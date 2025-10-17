# routers/user.py (or wherever your existing router lives)

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.database import get_db
from schemas.user import UserCreate, UserLogin
from services.userService import create_user, authenticate_user

# NEW imports
import jwt
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
import datetime, os
from models.user import User

router = APIRouter(tags=["User"])

# NEW: OAuth2 setup
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")
JWT_SECRET = os.getenv("JWT_SECRET", "change-me")
JWT_ALG = "HS256"

@router.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):
    db_user = create_user(user, db)
    return {"id": db_user.id, "name": db_user.name, "email": db_user.email}

# NEW: Standards-compliant token endpoint (form fields: username, password)
@router.post("/token")
def issue_token(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db),
):
    # OAuth2PasswordRequestForm uses "username" for the identifier
    db_user = authenticate_user(
        UserLogin(email=form_data.username, password=form_data.password), db
    )
    if not db_user:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    exp = datetime.datetime.now() + datetime.timedelta(hours=12)
    access_token = jwt.encode(
        {"sub": db_user.email, "uid": db_user.id, "exp": exp},
        JWT_SECRET,
        algorithm=JWT_ALG,
    )
    # Standard OAuth2 shape (you can add extra fields if you want)
    return {"access_token": access_token, "token_type": "bearer"}

# NEW: Minimal "who am I?" endpoint requiring Bearer token
@router.get("/me")
def read_me(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALG])
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")

    email = payload.get("sub")
    user = db.query(User).filter_by(email=email).first()
    if not user:
        raise HTTPException(status_code=401, detail="User not found")

    return {"id": user.id, "name": user.name, "email": user.email}
