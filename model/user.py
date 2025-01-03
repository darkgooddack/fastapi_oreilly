from sqlalchemy import Column, String
from data.database import Base

class SUser(Base):
    __tablename__ = "users"

    name = Column(String, primary_key=True, nullable=False)  # Поле name (первичный ключ)
    hash = Column(String, nullable=True)

from pydantic import BaseModel

class User(BaseModel):
    name: str
    hash: str | None

    model_config = {
        "from_attributes": True
    }