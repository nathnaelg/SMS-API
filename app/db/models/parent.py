from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship
# from app.db.base_class import Base
from ..base import Base


class Parent(Base):
    __tablename__ = "parents"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, nullable=True)
    phone_number = Column(String, nullable=True)

    user = relationship("User", back_populates="parents")
    children = relationship("Student", back_populates="parent")
