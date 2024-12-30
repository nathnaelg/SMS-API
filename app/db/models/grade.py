from sqlalchemy import Column, Integer, ForeignKey, Float
from sqlalchemy.orm import relationship
# from app.db.base_class import Base
from ..base import Base


class Grade(Base):
    __tablename__ = "grades"

    id = Column(Integer, primary_key=True, index=True)
    assignment_id = Column(Integer, ForeignKey("assignments.id"), nullable=False)
    student_id = Column(Integer, ForeignKey("students.id"), nullable=False)
    score = Column(Float, nullable=False)

    student = relationship("Student", back_populates="grades")
