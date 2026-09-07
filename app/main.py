from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from app.database import Base, engine, SessionLocal
from app.schemas.user import UserCreate, UserUpdate
from app.models.user import User
from app.models.task import Task

from app.schemas.user import UserCreate
from app.schemas.task import TaskCreate

from app.services.user_service import create_user
from app.services.task_service import create_task
from app.services.task_service import create_task, get_all_tasks
from app.schemas.task import TaskCreate, TaskUpdate
from app.services.user_service import create_user, get_all_users
from app.services.task_service import (
    create_task,
    get_all_tasks,
    get_task_by_id,
    update_task
)

from app.services.user_service import (
    create_user,
    get_all_users,
    get_user_by_id,
    update_user
)

from app.services.task_service import (
    create_task,
    get_all_tasks,
    get_task_by_id
)

from app.services.user_service import (
    create_user,
    get_all_users,
    get_user_by_id,
    update_user,
    delete_user
)

from app.services.task_service import (
    create_task,
    get_all_tasks,
    get_task_by_id,
    update_task,
    delete_task
)
from app.services.user_service import (
    create_user,
    get_all_users,
    get_user_by_id
)
# Create database tables
Base.metadata.create_all(bind=engine)


# Create FastAPI application
app = FastAPI(title="Task Management API")


# Database connection
def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


# Home API
@app.get("/")
def home():
    return {"message": "Task Management API is running"}


# Create User API
@app.post("/users")
def create_new_user(
    user: UserCreate,
    db: Session = Depends(get_db)
):
    return create_user(db, user)


# Create Task API
@app.post("/tasks")
def create_new_task(
    task: TaskCreate,
    db: Session = Depends(get_db)
):
    return create_task(db, task)

@app.get("/tasks")
def get_tasks(db: Session = Depends(get_db)):
    return get_all_tasks(db)

@app.get("/tasks/{task_id}")
def get_task(task_id: int, db: Session = Depends(get_db)):
    return get_task_by_id(db, task_id)

@app.put("/tasks/{task_id}")
def update_existing_task(
    task_id: int,
    task_data: TaskUpdate,
    db: Session = Depends(get_db)
):
    return update_task(db, task_id, task_data)

@app.delete("/tasks/{task_id}")
def delete_existing_task(
    task_id: int,
    db: Session = Depends(get_db)
):
    return delete_task(db, task_id)

@app.get("/users")
def get_users(db: Session = Depends(get_db)):
    return get_all_users(db) 
@app.get("/users/{user_id}")
def get_user(user_id: int, db: Session = Depends(get_db)):
    return get_user_by_id(db, user_id)

@app.put("/users/{user_id}")
def update_existing_user(
    user_id: int,
    user_data: UserUpdate,
    db: Session = Depends(get_db)
):
    return update_user(db, user_id, user_data)

@app.delete("/users/{user_id}")
def delete_existing_user(
    user_id: int,
    db: Session = Depends(get_db)
):
    return delete_user(db, user_id)