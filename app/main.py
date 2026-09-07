from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from app.database import Base, engine, SessionLocal

from app.models.user import User
from app.models.task import Task

from app.schemas.user import UserCreate
from app.schemas.task import TaskCreate

from app.services.user_service import create_user
from app.services.task_service import create_task


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