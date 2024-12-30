from pydantic import BaseModel

class GradeBase(BaseModel):
    score: float

class GradeCreate(GradeBase):
    assignment_id: int
    student_id: int

class GradeUpdate(GradeBase):
    pass

class Grade(GradeBase):
    id: int
    assignment_id: int
    student_id: int

    class Config:
        orm_mode = True
