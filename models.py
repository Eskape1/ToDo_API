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


#users input
class UserIn(BaseModel):
    username: str = Field(description='Write your name', min_length=3, max_length=12, default='User4069')
    password: str = Field(description='Write a good password', min_length=8, default='secret_pass')

#users output
class UserOut(BaseModel):
    username: str
    model_config = {'from_attributes': True}

#users in database
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False, index=True)
    password = Column(String, nullable=False, index=True)     

