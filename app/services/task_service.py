from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models.task import Task
from app.schemas.task import TaskCreate
from app.utils.validators import validate_task_status

from app.schemas.task import TaskCreate, TaskUpdate
def create_task(db: Session, task: TaskCreate):

    if not validate_task_status(task.status):
        raise HTTPException(
            status_code=400,
            detail="Invalid task status. Use pending, in_progress, or completed."
        )

    new_task = Task(
        title=task.title,
        description=task.description,
        status=task.status,
        user_id=task.user_id
    )

    db.add(new_task)
    db.commit()
    db.refresh(new_task)

    return new_task


def get_all_tasks(db: Session):
    return db.query(Task).all()

def get_task_by_id(db: Session, task_id: int):
    task = db.query(Task).filter(Task.id == task_id).first()

    if not task:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    return task
def update_task(db: Session, task_id: int, task_data: TaskUpdate):
    task = db.query(Task).filter(Task.id == task_id).first()

    if not task:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    if not validate_task_status(task_data.status):
        raise HTTPException(
            status_code=400,
            detail="Invalid task status. Use pending, in_progress, or completed."
        )

    task.title = task_data.title
    task.description = task_data.description
    task.status = task_data.status

    db.commit()
    db.refresh(task)

    return task

def delete_task(db: Session, task_id: int):
    task = db.query(Task).filter(Task.id == task_id).first()

    if not task:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    db.delete(task)
    db.commit()

    return {"message": "Task deleted successfully"}