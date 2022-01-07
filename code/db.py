# -*- coding: utf-8 -*-
# DBへの接続設定
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
import os

# 接続したいDBの基本情報を設定
user_name = os.getenv('MYSQL_USER')
password = os.getenv('MYSQL_PASSWORD')
host = os.getenv('MYSQL_HOST')
database_name = os.getenv('MYSQL_DATABASE')

DATABASE = 'mysql://%s:%s@%s/%s?' % (
    user_name,
    password,
    host,
    database_name,
)

DATABASEURL = 'mysql://root:password@mysql_v2/Experiment_Server'

# DBとの接続
ENGINE = create_engine(
    DATABASEURL,
    echo=True,
)

SessionLocal = sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=ENGINE)


Base = declarative_base()

