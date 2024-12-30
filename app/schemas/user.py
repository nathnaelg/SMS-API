from pydantic import BaseModel, EmailStr
from typing import List, Optional
from enum import Enum

class UserRole(str, Enum):
    admin = "admin"
    teacher = "teacher"
    student = "student"
    parent = "parent"

class UserBase(BaseModel):
    username: str
    email: EmailStr
    role: UserRole

class UserCreate(UserBase):
    password: str

class UserUpdate(UserBase):
    password: Optional[str] = None

class User(UserBase):
    id: int

    class Config:
        orm_mode = True
