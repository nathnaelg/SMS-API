from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship
# from app.db.base_class import Base
from ..base import Base


class ClassRoom(Base):
    __tablename__ = "classrooms"

    id = Column(Integer, primary_key=True, index=True)
    teacher_id = Column(Integer, ForeignKey("teachers.id"), nullable=False)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)

    teacher = relationship("Teacher", back_populates="classerooms")
    students = relationship("Student", secondary="enrollments", back_populates="classerooms")
