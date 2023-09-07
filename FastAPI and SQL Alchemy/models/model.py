from core.configs import settings

from sqlalchemy import Column, Integer, String

from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass

# Create table with base sqlalchemy (similar to gorm)
class Curso(Base):
    __tablename__ = 'curso'
    
    id: int =  Column(Integer, primary_key=True, autoincrement=True)
    titulo: str = Column(String(100))
    aulas: int = Column(Integer)
    horas: int = Column(Integer)

