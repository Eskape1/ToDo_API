from fastapi import FastAPI
from routers import tasks


app = FastAPI()
app.include_router(tasks.router)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app="main:app", reload=True)
