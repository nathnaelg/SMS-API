from pydantic import BaseModel
from typing import Optional

class TeacherBase(BaseModel):
    first_name: str
    last_name: str
    qualification: Optional[str] = None

class TeacherCreate(TeacherBase):
    user_id: int

class TeacherUpdate(TeacherBase):
    pass

class Teacher(TeacherBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True
