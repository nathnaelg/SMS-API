from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship
# from app.db.base_class import Base
from ..base import Base


class Subject(Base):
    __tablename__ = "subjects"

    id = Column(Integer, primary_key=True, index=True)
    class_id = Column(Integer, ForeignKey("classrooms.id"), nullable=False)
    name = Column(String, nullable=False)

    class_ = relationship("Class", back_populates="subjects")
