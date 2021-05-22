from sqlalchemy import Column, String, create_engine, Integer, Float
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

db_url = 'mysql+pymysql://root:qq123456@127.0.0.1:3306/fastapi'
engine = create_engine(db_url)

DBSession = sessionmaker(bind=engine)
Base = declarative_base()
session = DBSession()

# alembic revision --autogenerate -m "文章"
# alembic upgrade head



