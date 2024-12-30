from pydantic_settings import BaseSettings
from dotenv import load_dotenv
import os


load_dotenv()
class Settings(BaseSettings):
    PROJECT_NAME:str = os.getenv("PROJECT_NAME")
    API_V1_STR:str = os.getenv("API_V1_STR")
    DATABASE_URL:str = os.getenv("DATABASE_URL")

    class Config:
        case_sensetive = True

settings = Settings()
