from sqlalchemy import Column, String
from data.database import Base

class Creature(Base):
    __tablename__ = "creatures"

    name = Column(String, primary_key=True, nullable=False)
    country = Column(String, nullable=True)
    area = Column(String, nullable=True)
    description = Column(String, nullable=True)
    aka = Column(String, nullable=True)
