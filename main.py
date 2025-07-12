from fastapi import FastAPI
from app import engine, Base, tasks

#our app
app = FastAPI(title='ToDo', version='1.0', description='Todo list with tasks',)

#making database if it not exist yet
Base.metadata.create_all(bind=engine)

#our routers
app.include_router(tasks.router)


#temporarily
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app="main:app", port=5000, reload=True)
