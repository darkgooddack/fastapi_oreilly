from sqlalchemy import Column, String
from data.database import Base

class Explorer(Base):
    __tablename__ = "explorers"
    name = Column(String, primary_key=True, nullable=False)
    country = Column(String, nullable=True)
    description = Column(String, nullable=True)