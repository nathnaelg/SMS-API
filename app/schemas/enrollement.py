from pydantic import BaseModel

class EnrollmentBase(BaseModel):
    pass

class EnrollmentCreate(EnrollmentBase):
    student_id: int
    class_id: int

class EnrollmentUpdate(EnrollmentBase):
    pass

class Enrollment(EnrollmentBase):
    id: int
    student_id: int
    class_id: int

    class Config:
        orm_mode = True
