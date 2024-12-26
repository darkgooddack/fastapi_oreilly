from data.database import Base
from sqlalchemy import Column, String

class Creature(Base):
    __tablename__ = 'creatures'

    name = Column(String, primary_key=True)
    country = Column(String)
    area = Column(String)
    description = Column(String)
    aka = Column(String)