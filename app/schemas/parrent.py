from pydantic import BaseModel
from typing import Optional

class ParentBase(BaseModel):
    first_name: str
    last_name: str
    email: Optional[str] = None
    phone_number: Optional[str] = None

class ParentCreate(ParentBase):
    user_id: int

class ParentUpdate(ParentBase):
    pass

class Parent(ParentBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True
