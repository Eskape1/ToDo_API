from fastapi import APIRouter, HTTPException, Query
from typing import Annotated, List
from models import Task, TaskModel
from storage import get_tasks, add_task, put_task, remove_task

router = APIRouter(prefix='/tasks', tags=['Tasks'])



@router.post("/", response_model=Task)
async def create_task(task: TaskModel):
    return add_task(task.title, task.txt, task.tags)


@router.get("/", response_model=list[Task])
def read_tasks(tag: str | None = None, 
               sort: Annotated[str | None, Query(description="Sort by 'newest' or 'latest'")] = None, 
               limit: Annotated[int | None, Query(description='Amount of output data at a time', gt=0)] = None):
    filtered: List[Task] = get_tasks()
    if tag:
        filtered = [n for n in filtered if tag in n.tags]
    if sort == 'newest':
        filtered.sort(key=lambda n: n.created, reverse=True)
    elif sort == 'latest':
        filtered.sort(key=lambda n: n.created)
    elif sort:
        raise HTTPException(status_code=400, detail='invalid request')
    if limit:
        filtered = filtered[:limit]
        
    return filtered

@router.put("/{task_id}", response_model=Task)
def change_task(task_id: int, task: TaskModel):
    return put_task(task_id, task.title, task.txt, task.tags)

@router.delete("/{task_id}")
def delete_task(task_id: int):
    remove_task(task_id)
    return {'operation':"deleted"}
