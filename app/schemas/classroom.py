from pydantic import BaseModel
from typing import List
from .student import Student
class ClassRoomBase(BaseModel):
    name: str
    description: str

class ClassRoomCreate(ClassRoomBase):
    teacher_id: int

class ClassRoomUpdate(ClassRoomBase):
    pass

class ClassRoom(ClassRoomBase):
    id: int
    teacher_id: int
    students: List[Student]

    class Config:
        orm_mode = True
