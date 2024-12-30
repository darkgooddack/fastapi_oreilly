from sqlalchemy import Column, String
from data.database import Base

class SExplorer(Base):
    __tablename__ = "explorers"
    name = Column(String, primary_key=True, nullable=False)
    country = Column(String, nullable=True)
    description = Column(String, nullable=True)

from pydantic import BaseModel

class Explorer(BaseModel):
    name: str
    country: str | None
    description: str | None

    class Config:
        from_attributes  = True