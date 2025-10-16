from pydantic import BaseModel

class UserCreate(BaseModel):
    name: str
    email: str
    password: str  # already hashed

class UserLogin(BaseModel):
    email: str
    password: str  # already hashed
