from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship
# from app.db.base_class import Base
from ..base import Base


class Teacher(Base):
    __tablename__ = "teachers"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    qualification = Column(String, nullable=True)

    user = relationship("User", back_populates="teachers")
    classes = relationship("Class", back_populates="teacher")
