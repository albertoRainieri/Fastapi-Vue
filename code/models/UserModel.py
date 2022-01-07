
from sqlalchemy import Column, Integer, String
#from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel
from db import Base
from db import ENGINE


#Base = declarative_base()
# userテーブルのモデルUserTableを定義
class UserTable(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(30), nullable=False)
    email = Column(String(100), nullable=False)
    hashed_password = Column(String(100), nullable=False)
    age = Column(Integer)

class UserSchema(BaseModel):
    id: int
    name: str
    age: int
    email: str
    hashed_password: str

def main():
    # テーブルが存在しなければ、テーブルを作成
    Base.metadata.create_all(bind=ENGINE)

if __name__ == "__main__":
    main()
