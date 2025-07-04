from models import Task, TaskModel
from datetime import datetime
from fastapi import HTTPException
from typing import List

tasks = []
ln = len(tasks)
global_id = ln

#get
def get_tasks() -> list[Task]:
    return tasks

#post
def add_task(task: TaskModel ) -> Task:
    global global_id
    n_task = Task(id=global_id, title=task.title, txt=task.txt, created=datetime.now(), tags=task.tags)
    tasks.append(n_task)
    global_id += 1
    return n_task

#put
def put_task(task_id: int, n_title: str, n_txt: str, n_tags: List[str] | None = None) -> Task: 
    for i, el in enumerate(tasks):
        if el.id == task_id:
            task: Task = tasks[i]
            task.title = n_title
            task.txt = n_txt
            task.tags = n_tags
            task.created = datetime.now()
            return task 
    raise HTTPException(status_code=404, detail="Task not found")

#delete
def remove_task(task_id: int) -> None: 
    for i, el in enumerate(tasks):
        if el.id == task_id:
            del tasks[i]
            return
    raise HTTPException(status_code=404, detail="Task not found")
