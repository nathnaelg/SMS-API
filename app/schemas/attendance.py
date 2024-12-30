from pydantic import BaseModel
from datetime import date

class AttendanceBase(BaseModel):
    date: date
    status: str

class AttendanceCreate(AttendanceBase):
    class_id: int
    student_id: int

class AttendanceUpdate(AttendanceBase):
    pass

class Attendance(AttendanceBase):
    id: int
    class_id: int
    student_id: int

    class Config:
        orm_mode = True
