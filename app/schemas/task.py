from typing import List
from pydantic import BaseModel, Field
from datetime import datetime

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
