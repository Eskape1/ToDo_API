from fastapi import FastAPI
from database import engine, Base

from routers import tasks, auth

#our app
app = FastAPI()

#making database if it not exist yet
Base.metadata.create_all(bind=engine)

#our routers
app.include_router(tasks.router)
app.include_router(auth.router)

#temporarily
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app="main:app", port=5000, reload=True)
