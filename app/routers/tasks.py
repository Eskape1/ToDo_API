from fastapi import APIRouter, HTTPException, Query, Depends
from sqlalchemy.orm import Session
from typing import Annotated
from schemas.task import TaskIn, TaskOut
from db.database import get_db
from .storage import get_tasks, add_task, put_task, remove_task

router = APIRouter(prefix='/tasks', tags=['Tasks'])

@router.get("/", response_model=list[TaskOut])
async def read_tasks(tag: str | None = None, 
               sort: Annotated[str | None, Query(description="Sort by 'newest' or 'latest'")] = None, 
               limit: Annotated[int | None, Query(description='Amount of output data at a time', gt=0)] = None,
               db: Session = Depends(get_db)):
    filtered = get_tasks(db)
    for task in filtered:
        task.tags = task.tags.split(",") if task.tags else []
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


@router.post("/")
async def create_task(task: TaskIn, db: Session = Depends(get_db)):
    return add_task(db, task.txt, task.tags)


@router.put("/{task_id}")
async def change_task(task_id: int, task: TaskIn, db: Session = Depends(get_db)):
    new_task = put_task(db, task_id, task.txt, task.tags)
    if not new_task:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"changed": new_task}


@router.delete("/{task_id}")
async def delete_task(task_id: int, db: Session = Depends(get_db)):
    deleted = remove_task(db, task_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Task not found")
    return deleted