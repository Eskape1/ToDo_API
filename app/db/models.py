from datetime import datetime
from sqlalchemy import Column, String, Integer, DateTime
from .database import Base

#our Schema nut in the database
class Task(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True)
    txt = Column(String, nullable=False)
    created = Column(DateTime, default=datetime.now())
    tags = Column(String, default='')
