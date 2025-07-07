from models import Task
from datetime import datetime
from sqlalchemy.orm import Session

#get
def get_tasks(db: Session):
    return db.query(Task).all()

#post
def add_task(db: Session, txt: str, tags: list[str] | None ):
    now = datetime.now()
    n_task = Task(txt=txt, tags=", ".join(tags), created=now)
    db.add(n_task)
    db.commit()
    db.refresh(n_task)
    return n_task

#put
def put_task(db: Session, task_id: int, new_txt: str, new_tags: list[str] | None): 
    task = db.query(Task).filter(Task.id == task_id).first()
    if task is None:
        return None
    task.txt = new_txt
    task.tags = ", ".join(new_tags)
    db.commit()
    return task 

#delete
def remove_task(db: Session, task_id: int): 
    task = db.query(Task).filter(Task.id == task_id).first()
    if task is None:
        return None
    db.delete(task)
    db.commit()
    return {"deleted": task}

