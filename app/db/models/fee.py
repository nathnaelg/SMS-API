# app/db/models/fee.py
from sqlalchemy import Column, Integer, ForeignKey, Float, Date, String, Enum
from sqlalchemy.orm import relationship
# from app.db.base_class import Base
from ..base import Base

import enum


class PaymentStatus(enum.Enum):
    PAID = "paid"
    UNPAID = "unpaid"
class Fee(Base):
    __tablename__ = "fees"

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("students.id"), nullable=False)
    amount = Column(Float, nullable=False)
    due_date = Column(Date, nullable=False) 
    status = Column(Enum(PaymentStatus), nullable=False)  

    student = relationship("Student", back_populates="fee")
