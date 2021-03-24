# -*- coding: utf-8 -*-
# 博客
# @File    : models.py
# @Date    : 2021-03-24
# @Author  : yuruhao
from sqlalchemy import Column, Integer, String

from db.mysql import Base


class Books(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(100))
    new_percent = Column(String(10))
    author = Column(String(30))
    pub_com = Column(String(100))
