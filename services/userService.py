from sqlalchemy.orm import Session
from models.user import User
from schemas.user import UserCreate, UserLogin

# Register user
def create_user(user: UserCreate, db: Session):
    db_user = User(name=user.name, email=user.email, password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# Login user
def authenticate_user(user: UserLogin, db: Session):
    db_user = db.query(User).filter(User.email == user.email, User.password == user.password).first()
    return db_user
