from sqlalchemy import Boolean, Column,  ForeignKey, Integer, String, Enum
from sqlalchemy.orm import relationship
import enum

from ..base import Base



class UserRole(enum.Enum):
    STUDENT = "student"
    TEACHER = "teacher"
    PARENT = "parent"
    ADMIN = "admin"



class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)
    role = Column(Enum(UserRole), nullable=False)
    
    students = relationship("Student", back_populates="user")
    teachers = relationship("Teacher", back_populates="user")
    parents = relationship("Parent", back_populates="user")

