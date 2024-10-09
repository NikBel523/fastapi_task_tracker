from sqlalchemy.orm import Session
from models import Task
from schemas import TaskCreate


def get_tasks(db: Session):
    return db.query(Task).all()


def create_task(db: Session, task: TaskCreate):
    db_task = Task(title=task.title, description=task.description)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task
