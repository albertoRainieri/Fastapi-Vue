import sys, os

sys.path.insert(1, os.path.join(sys.path[0], '..'))

from typing import List
from models.UserModel import UserTable, UserSchema
from sqlalchemy.orm import Session




def read_users(db: Session):
    users = db.query(UserTable).with_entities(UserTable.email).all()
    return users

def read_user(user_id: int, db: Session):
    user = db.query(UserTable).\
        filter(UserTable.id == user_id).first()
    return user

def create_user(User: UserSchema, db: Session):
    user = UserTable()
    user.name = User.name
    user.age = User.age
    user.email = User.email
    user.hashed_password = User.hashed_password
    db.add(user)
    db.commit()

def update_users(users: List[UserSchema], db: Session):
    for new_user in users:
        user = db.query(UserTable).\
            filter(UserTable.id == new_user.id).first()
        user.name = new_user.name
        user.age = new_user.age
        db.commit()

def delete_users(db: Session):
    db.query(UserTable).delete()
    db.commit()

def delete_user(id: str, db: Session):
    db.query(UserTable).filter(UserTable.id == id).delete()
    db.commit()

def isSubscribed(email: str, db:Session):
    results = db.query(UserTable).with_entities(UserTable.email).all()
    if results is None:
        return False
    for result in results:
        if result.email == email:
            return True
        else:
            return False

def getCurrentUser(email: str, db:Session):
    results = db.query(UserTable).with_entities(UserTable.email, UserTable.name).all()
    if results is None:
        return False
    for result in results:
        if result.email == email:
            return result.name
    return {'message': 'Name not found'}

