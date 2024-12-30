from pydantic import BaseModel
from datetime import date

class AssignmentBase(BaseModel):
    name: str
    due_date: date

class AssignmentCreate(AssignmentBase):
    class_id: int

class AssignmentUpdate(AssignmentBase):
    pass

class Assignment(AssignmentBase):
    id: int
    class_id: int

    class Config:
        orm_mode = True
