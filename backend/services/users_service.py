from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from backend.models import User as UserModel
from backend.schemas import UserCreate, User
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

async def create_user(user: UserCreate, db: Session):
    hashed_password = pwd_context.hash(user.password)
    new_user = UserModel(username=user.username, password=hashed_password, role=user.role)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return User.from_orm(new_user)

async def get_user(user_id: int, db: Session):
    user = db.query(UserModel).filter(UserModel.id == user_id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return User.from_orm(user)
