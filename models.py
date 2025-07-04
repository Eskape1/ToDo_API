from pydantic import BaseModel
from datetime import datetime
from typing import List

class Task(BaseModel):
    id: int
    title: str
    txt: str
    created: datetime
    tags: List[str] | None = []

class TaskModel(BaseModel):
    title: str = "Your title"
    txt: str = "lorem ipsum"
    tags: List[str] | None = ['lorem', 'ipsum']