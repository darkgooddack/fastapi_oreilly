from sqlalchemy import Column, String
from data.database import Base

class SCreature(Base):
    __tablename__ = "creatures"

    name = Column(String, primary_key=True, nullable=False)
    country = Column(String, nullable=True)
    area = Column(String, nullable=True)
    description = Column(String, nullable=True)
    aka = Column(String, nullable=True)

from pydantic import BaseModel

class Creature(BaseModel):
    name: str
    country: str | None
    area: str | None
    description: str | None
    aka: str | None

    model_config = {
        "from_attributes": True
    }