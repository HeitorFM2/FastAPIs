from models.model import Base
from core.database import engine

def create_table() -> None:
    print("Creating tables in the database...")

    Base.metadata.drop_all
    # Creating neu tables
    Base.metadata.create_all(engine)

    print("Tables created successfully!")