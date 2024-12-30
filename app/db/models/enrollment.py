# app/db/models/enrollment.py
from sqlalchemy import Column, Integer, ForeignKey
# from app.db.base_class import Base
from ..base import Base


class Enrollment(Base):
    __tablename__ = "enrollments"

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("students.id"), nullable=False)
    class_id = Column(Integer, ForeignKey("classrooms.id"), nullable=False)
