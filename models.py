from pydantic import BaseModel
from datetime import datetime


class Task(BaseModel):
    id: int
    title: str
    txt: str
    created: datetime