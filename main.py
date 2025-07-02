from fastapi import FastAPI
from pydantic import BaseModel
from typing import Annotated

app = FastAPI()

tasks = []

class TaskModel(BaseModel):
    theme: str
    author: str = 'Anonym'
    task: str

@app.get("/")
def func():
    return "Hello world!"

@app.get("/tasks")
def get_tasks() -> list[TaskModel]:
    return tasks

@app.post("/tasks")
def post_task(task: TaskModel) -> dict:
    tasks.append(task)
    return {"new task": task}



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app="main:app", reload=True)
