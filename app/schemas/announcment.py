from pydantic import BaseModel
from datetime import datetime

class AnnouncementBase(BaseModel):
    title: str
    content: str
    date: datetime

class AnnouncementCreate(AnnouncementBase):
    user_id: int

class AnnouncementUpdate(AnnouncementBase):
    pass

class Announcement(AnnouncementBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True
