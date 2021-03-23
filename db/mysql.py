from sqlalchemy import Column, String, create_engine, Integer, Float
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

db_url = 'mysql+pymysql://root:123456@200.201.184.202:3306/test'
engine = create_engine(db_url)

DBSession = sessionmaker(bind=engine)
Base = declarative_base()
session = DBSession()


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, autoincrement=True)
    login_name = Column(String(20))
    cn_name = Column(String(20))
    en_name = Column(String(20))
    password = Column(String(20))


class Books(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(100))
    new_percent = Column(String(10))
    author = Column(String(30))
    pub_com = Column(String(100))
