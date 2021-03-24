from sqlalchemy import Column, String, create_engine, Integer, Float
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

db_url = 'mysql+pymysql://root:123456@200.201.184.202:3306/test'
engine = create_engine(db_url)

DBSession = sessionmaker(bind=engine)
Base = declarative_base()
session = DBSession()

