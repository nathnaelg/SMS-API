from pydantic import BaseModel

class SubjectBase(BaseModel):
    name: str

class SubjectCreate(SubjectBase):
    class_id: int

class SubjectUpdate(SubjectBase):
    pass

class Subject(SubjectBase):
    id: int
    class_id: int

    class Config:
        orm_mode = True
