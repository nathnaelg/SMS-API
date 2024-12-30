from sqlalchemy import Column, Integer, ForeignKey, String, Date
from sqlalchemy.orm import relationship
from ...db.base import Base

class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    date_of_birth = Column(Date, nullable=False)
    address = Column(String, nullable=True)
    # class_id = Column(Integer, ForeignKey("classerooms.id"))

    user = relationship("User", back_populates="students")
    enrollments = relationship("Enrollment", back_populates="student")
    attendances = relationship("Attendance", back_populates="student")
    grades = relationship("Grade", back_populates="student")
    fee = relationship("Fee", uselist=False, back_populates="student")
