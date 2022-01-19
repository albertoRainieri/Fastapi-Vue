import sys, os
sys.path.insert(1, os.path.join(sys.path[0], '..'))

from fastapi import APIRouter
from typing import List
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from models.UserModel import UserTable, UserSchema
from models import UserModel

from crud import UserCrud
from db import SessionLocal, ENGINE

UserModel.Base.metadata.create_all(bind=ENGINE)

router = APIRouter(
)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/users")
async def read_users(db: Session = Depends(get_db)):
    return UserCrud.read_users(db)

@router.get("/users/{user_id}")
async def read_user(user_id: int, db: Session = Depends(get_db)):
    return UserCrud.read_user(user_id, db)

@router.put("/users")
async def update_users(users: List[UserSchema]):
    return UserCrud.update_users(users)

@router.delete("/users")
async def delete_users(db: Session = Depends(get_db)):
    return UserCrud.delete_users(db)

@router.delete("/user/{id}")
async def delete_user(id: str, db: Session = Depends(get_db)):
    return UserCrud.delete_user(id, db)





