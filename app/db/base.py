from sqlalchemy.ext.declarative import declarative_base



Base = declarative_base()

from app.db.models.teacher import Teacher
from app.db.models.subject import Subject
from app.db.models.attendance import Attendance
from app.db.models.assignment import Assignment
from app.db.models.grade import Grade
from app.db.models.parent import Parent
from app.db.models.announcement import Announcement
from app.db.models.fee import Fee
from app.db.models.classroom import ClassRoom

from app.db.models.user import User
from app.db.models.student import Student
