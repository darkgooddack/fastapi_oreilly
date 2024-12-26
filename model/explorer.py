from sqlalchemy import Column, String
from data.database import Base

class Explorer(Base):
    __tablename__ = 'explorers'

    name = Column(String, primary_key=True)
    country = Column(String)
    description = Column(String)
