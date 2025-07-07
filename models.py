from pydantic import BaseModel, Field
from datetime import datetime
from typing import List
from sqlalchemy import Column, String, Integer, DateTime

from database import Base

#model which user fills
class TaskIn(BaseModel):
    txt: str = Field()
    tags: List[str] | None =Field(default_factory=list)

#how our Schema look out
class TaskOut(TaskIn):
    id: int = Field()
    created: datetime = Field()
    class Config:
        from_attributes = True

#our Schema nut in the database
class Task(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True)
    txt = Column(String, nullable=False)
    created = Column(DateTime, default=datetime.now())
    tags = Column(String, default='')
