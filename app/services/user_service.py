from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models.user import User
from app.schemas.user import UserCreate
from app.utils.validators import validate_email


def create_user(db: Session, user: UserCreate):

    if not validate_email(user.email):
        raise HTTPException(
            status_code=400,
            detail="Invalid email address"
        )

    new_user = User(
        name=user.name,
        email=user.email
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user