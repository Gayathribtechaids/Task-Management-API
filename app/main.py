from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from app.database import Base, engine, SessionLocal
from app.models.user import User
from app.schemas.user import UserCreate
from app.services.user_service import create_user


Base.metadata.create_all(bind=engine)

app = FastAPI(title="Task Management API")


def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


@app.get("/")
def home():
    return {"message": "Task Management API is running"}


@app.post("/users")
def create_new_user(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db, user)