from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
import os

user_name = os.getenv('MYSQL_USERNAME')
password = os.getenv('MYSQL_PASSWORD')
host = os.getenv('MYSQL_HOST')
database_name = os.getenv('MYSQL_DATABASE')

DATABASE = 'mysql://%s:%s@%s/%s?' % (
    user_name,
    password,
    host,
    database_name,
)


ENGINE = create_engine(
    DATABASE,
    echo=True,
)

SessionLocal = sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=ENGINE)


Base = declarative_base()

