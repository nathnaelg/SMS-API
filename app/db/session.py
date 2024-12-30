from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from ..core.config import settings

SQLALCHEMY_DATABASE_URL = "sqlite:///./SMS.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,  connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

