from sqlalchemy import Column, Integer, ForeignKey, String, Date
from sqlalchemy.orm import relationship
# from app.db.base_class import Base
from ..base import Base


class Assignment(Base):
    __tablename__ = "assignments"

    id = Column(Integer, primary_key=True, index=True)
    class_id = Column(Integer, ForeignKey("classrooms.id"), nullable=False)
    name = Column(String, nullable=False)
    due_date = Column(Date, nullable=False)

    class_room = relationship("ClassRoom", back_populates="assignments")
