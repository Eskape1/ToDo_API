from models import Task, TaskModel
from datetime import datetime
from fastapi import HTTPException


tasks = []
ln = len(tasks)
global_id = ln

#get
def get_tasks() -> list[Task]:
    return tasks

#post
def add_task(task: TaskModel ) -> Task:
    global global_id
    n_task = Task(id=global_id, title=task.title, txt=task.txt, created=datetime.now())
    tasks.append(n_task)
    global_id += 1
    return n_task

#put
def put_task(task_id: int, n_title, n_txt) -> Task: 
    for i, el in enumerate(tasks):
        if el.id == task_id:
            task: Task = tasks[i]
            task.title = n_title
            task.txt = n_txt
            return task 
    raise HTTPException(status_code=404, detail="Task not found")

#delete
def remove_task(task_id: int) -> None: 
    for i, el in enumerate(tasks):
        if el.id == task_id:
            del tasks[i]
            return
    raise HTTPException(status_code=404, detail="Task not found")
