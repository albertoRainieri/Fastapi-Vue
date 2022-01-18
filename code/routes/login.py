from email.header import Header
import sys, os
from urllib.request import Request

from pydantic.typing import NoneType
sys.path.insert(1, os.path.join(sys.path[0], '..'))

from fastapi_login.exceptions import InvalidCredentialsException #Exception class
from fastapi import APIRouter, Depends, HTTPException
from db import SessionLocal
from models.UserModel import  TokenSchema, UserTable, LoginSchema, RegisterSchema
from crud import crud
from fastapi import Depends, HTTPException, Request, status
from form.Users import UserCreateForm

from datetime import timedelta, datetime
from typing import Optional

from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext

SECRET = "secret-key"
# To obtain a suitable secret key you can run | import os; print(os.urandom(24).hex())
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

router = APIRouter(
)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# to get a string like this run:
# openssl rand -hex 32
SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

@router.post('/login')
def login(request: LoginSchema, db: SessionLocal = Depends(get_db)):
    email = request.email
    hashed_password = request.hashed_password
    query = db.query(UserTable).filter(UserTable.email == email).first()
    token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    if query is not None:
        if not verify_password(hashed_password, query.hashed_password):
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail='User or Password wrong')
        else:
            token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
            token = create_access_token(
                data={"sub": query.email}, expires_delta=token_expires
            )

            return {'ack': 1, 'Message': 'Login Succesfull', 'token': token}
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail='User or Password wrong')
        

@router.post('/register', status_code=status.HTTP_201_CREATED)
async def register(request: RegisterSchema, db: SessionLocal = Depends(get_db)):
    if request.hashed_password != request.hashed_password:
        raise HTTPException(status_code=401, detail='These are two different passwords!')
    if isNewEmail(request.email, db):
        form = UserCreateForm(request)
        await form.load_data()
        if await form.is_valid():
            request.hashed_password = pwd_context.hash(request.hashed_password)
            crud.create_user(request, db)
            return {'ack': 1, 'Message': 'User Succesfully created'}
        else:
            raise HTTPException(status_code=401, detail=form.errors)
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail='Email is already used')

def isNewEmail(email: str, db: SessionLocal = Depends(get_db)):
    query = db.query(UserTable).\
        filter(UserTable.email == email).first()
    if query is None:
        return True
    else:
        return False    

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=1)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


@router.post('/isSubscribed')
async def isSubscribed(token: TokenSchema, db: SessionLocal = Depends(get_db)):
    try: 
        payload = jwt.decode(token.token, SECRET_KEY, algorithms=[ALGORITHM])
    except:
        return False
    email: str = payload.get("sub")
    return crud.isSubscribed(email, db)

@router.get("/getCurrentUser/{token}")
async def currentUser(token: str, db: SessionLocal = Depends(get_db)):
    try: 
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    except:
        return {'message': 'Error in decoding'}
    email = payload.get("sub")
    return crud.getCurrentUser(email, db)











    






