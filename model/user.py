from sqlalchemy import Column, String
from data.database import Base

class User(Base):
    __tablename__ = "users"

    name = Column(String, primary_key=True, nullable=False)  # Поле name (первичный ключ)
    hash = Column(String, nullable=True)

