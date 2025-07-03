from pydantic import BaseModel
from datetime import datetime
#from typing import Optional, List

class Task(BaseModel):
    id: int
    title: str
    txt: str
    created: datetime

class TaskModel(BaseModel):
    title: str = "Your title"
    txt: str = "lorem ipsum"