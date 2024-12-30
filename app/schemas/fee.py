from pydantic import BaseModel
from datetime import date
from typing import Optional

class FeeBase(BaseModel):
    amount: float
    due_date: date
    status: str

class FeeCreate(FeeBase):
    student_id: int

class FeeUpdate(FeeBase):
    pass

class Fee(FeeBase):
    id: int
    student_id: int

    class Config:
        orm_mode = True
