# -*- coding: utf-8 -*-
# 
# @File    : models.py
# @Date    : 2021-03-24
# @Author  : yuruhao
from datetime import datetime

from sqlalchemy import Integer, Column, String, Float, DateTime

from db.mysql import Base


class Books(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(10))
    new_percent = Column(Float)
    author = Column(String(30))
    pub_com = Column(String(100))
    pub_time = Column(DateTime, onupdate=datetime.now)
    update_time = Column(DateTime, onupdate=datetime.now, default=datetime.now)
