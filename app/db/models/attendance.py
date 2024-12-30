from sqlalchemy import Column, Integer, ForeignKey, Date, String
from sqlalchemy.orm import relationship
# from app.db.base_class import Base
from ..base import Base


class Attendance(Base):
    __tablename__ = "attendances"

    id = Column(Integer, primary_key=True, index=True)
    class_id = Column(Integer, ForeignKey("classrooms.id"), nullable=False)
    student_id = Column(Integer, ForeignKey("students.id"), nullable=False)
    date = Column(Date, nullable=False)
    status = Column(String, nullable=False)  # e.g., "Present", "Absent"

    student = relationship("Student", back_populates="attendances")
