from fastapi import FastAPI
from pydantic import BaseModel
from models import Task
from storage import add_task, get_tasks

app = FastAPI()

class TaskModel(BaseModel):
    title: str = "Your title"
    txt: str = "lorem ipsum"


@app.post("/tasks", response_model=Task)
def create_task(task: TaskModel):
    return add_task(task.title, task.txt)


@app.get("/tasks", response_model=list[Task])
def read_tasks():
    return get_tasks()



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app="main:app", reload=True)
