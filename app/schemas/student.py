from pydantic import BaseModel
from datetime import date
from typing import Optional

class StudentBase(BaseModel):
    first_name: str
    last_name: str
    date_of_birth: date
    address: Optional[str] = None

class StudentCreate(StudentBase):
    user_id: int

class StudentUpdate(StudentBase):
    pass

class Student(StudentBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True
