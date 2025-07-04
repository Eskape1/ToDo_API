from fastapi import FastAPI, Query, HTTPException
from models import Task, TaskModel
from storage import add_task, get_tasks, put_task, remove_task
from typing import List, Annotated

from storage import tasks

app = FastAPI()




@app.post("/tasks/new")
async def create_task(task: TaskModel):
    return {"created": add_task(task)}


@app.get("/tasks", response_model=list[Task])
def read_tasks(tag: str | None = None, 
               sort: Annotated[str | None, Query(description="Sort by 'newest' or 'latest'")] = None, 
               limit: Annotated[int | None, Query(description='Amount of output data at a time', gt=0)] = None):
    filtered: List[Task] = tasks
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

@app.put("/tasks/change/{task_id}")
def change_task(task_id: int, task: TaskModel):
    return put_task(task_id, task.title, task.txt, task.tags)

@app.delete("/tasks/delete/{task_id}")
def delete_task(task_id: int):
    remove_task(task_id)
    return {'operation':"deleted"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app="main:app", reload=True)
