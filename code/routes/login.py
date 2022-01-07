import sys, os

from pydantic.typing import NoneType
from sqlalchemy.sql.elements import Null
from sqlalchemy.sql.expression import false
sys.path.insert(1, os.path.join(sys.path[0], '..'))

from fastapi import Request
from fastapi.responses import RedirectResponse,HTMLResponse
from fastapi.security import OAuth2PasswordRequestForm
from fastapi_login import LoginManager #Loginmanager Class
from fastapi_login.exceptions import InvalidCredentialsException #Exception class
from fastapi import APIRouter, Depends, FastAPI, HTTPException
from db import SessionLocal, ENGINE
from models.UserModel import UserSchema, UserTable
from crud import crud
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from form.Users import UserCreateForm

SECRET = "secret-key"
# To obtain a suitable secret key you can run | import os; print(os.urandom(24).hex())

manager = LoginManager(SECRET, token_url="/auth/login", use_cookie=True)
manager.cookie_name = "some-name"

router = APIRouter(
)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# @manager.user_loader()
# def load_user(email: str):  # could also be an asynchronous function
#     user = DB.get(email)
#     return user


# @router.post('/auth/token')
# def login(data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
#     email = data.username
#     password = data.password

#     query = db.query(UserTable).\
#         filter(UserTable.email == email).first()  # we are using the same function to retrieve the user
#     query_email = query.email
#     query_password = query.hashed_password
#     if not query_email:
#         raise InvalidCredentialsException  # you can also use your own HTTPException
#     elif password != query_password:
#         raise InvalidCredentialsException

#     access_token = manager.create_access_token(
#         data=dict(sub=email)
#     )
#     return {'access_token': access_token, 'token_type': 'bearer'}

# @router.post('/register')
# async def register(user: UserSchema, db: SessionLocal = Depends(get_db)):
#     # form = UserCreateForm(user)
#     # await form.load_data()
#     # if await form.is_valid():
#     #     user = UserCreate(
#     #         username=form.username, email=form.email, password=form.password
#     #     )
#     #     try:
#     #         return responses.RedirectResponse(
#     #             "/?msg=Successfully-Registered", status_code=status.HTTP_302_FOUND
#     #         )  # default is post request, to use get request added status code 302
#     #     except IntegrityError:
#     #         form.__dict__.get("errors").append("Duplicate username or email")
#     #         return templates.TemplateResponse("users/register.html", form.__dict__)
#     # return templates.TemplateResponse("users/register.html", form.__dict__)
#     return crud.create_user(user, db)


from datetime import datetime, time, timedelta
from typing import DefaultDict, Optional

from fastapi import Depends, FastAPI, HTTPException, status, Response
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext
from pydantic import BaseModel

# to get a string like this run:
# openssl rand -hex 32
SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

@router.post('/login')
def login(request: UserSchema, db: SessionLocal = Depends(get_db)):
    email = request.email
    hashed_password = request.hashed_password
    query = db.query(UserTable).filter(UserTable.email == email).first()
    if query is not None:
        if not verify_password(hashed_password, query.hashed_password):
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail='User or Password wrong')
        else:
            return {'Message': 'Login Succesfull'}
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail='User or Password wrong')
        

@router.post('/register', status_code=status.HTTP_201_CREATED)
async def register(request: UserSchema, db: SessionLocal = Depends(get_db)):
    if isNewEmail(request.email, db):
        form = UserCreateForm(request)
        await form.load_data()
        if await form.is_valid():
            request.hashed_password = pwd_context.hash(request.hashed_password)
            crud.create_user(request, db)
            return {'Message': 'User Succesfully created'}
        else:
            raise HTTPException(status_code=401, detail=form.errors)
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail='Email is already used')

def isNewEmail(email: str, db: SessionLocal = Depends(get_db)):
    query = db.query(UserTable).\
        filter(UserTable.email == email).select().first()
    if query is None:
        return True
    else:
        return False    

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)






    






