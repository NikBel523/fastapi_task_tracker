from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from crud import get_tasks, create_task
from models import Base
from schemas import Task, TaskCreate
from database import SessionLocal, engine

app = FastAPI()

# Создание таблиц в базе данных
Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/tasks/", response_model=list[Task])
def read_tasks(db: Session = Depends(get_db)):
    """Возвращает список задач."""
    tasks = get_tasks(db)
    return tasks


@app.post("/add_task/", response_model=Task)
def create_task_endpoint(task: TaskCreate, db: Session = Depends(get_db)):
    """Добавляет новую задачу."""
    return create_task(db=db, task=task)
