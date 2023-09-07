from pydantic_settings import BaseSettings
from sqlalchemy.orm import DeclarativeBase 

class Base(DeclarativeBase):
    pass

class Settings(BaseSettings):
    """
    Configurações gerais usadas na aplicação
    """
    API_V1_STR: str = '/api/v1'
    DB_URL: str = "postgresql+asyncpg://postgres:root@localhost:5432/fastapi"

    class Config:
        case_sensitive = True


settings = Settings()
