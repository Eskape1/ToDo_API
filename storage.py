from models import Task
from datetime import datetime


tasks = []
task_id = 1


def add_task(title: str, txt: str ) -> Task:
    global task_id
    task = Task(id=task_id, title=title, txt=txt, created=datetime.now())
    task_id += 1
    tasks.append(task)
    return task

def get_tasks() -> list[Task]:
    return tasks