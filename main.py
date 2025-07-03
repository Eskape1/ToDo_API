from fastapi import FastAPI
from pydantic import BaseModel
from models import Task, TaskModel
from storage import add_task, get_tasks, put_task, remove_task

app = FastAPI()




@app.post("/tasks/new")
async def create_task(task: TaskModel):
    return {"created": add_task(task)}


@app.get("/tasks", response_model=list[Task])
def read_tasks():
    return get_tasks()

@app.put("/tasks/change/{task_id}")
def change_task(task_id: int, task: TaskModel):
    return put_task(task_id, task.title, task.txt)

@app.delete("/tasks/delete/{task_id}")
def delete_task(task_id: int):
    remove_task(task_id)
    return {'operation':"deleted"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app="main:app", reload=True)
