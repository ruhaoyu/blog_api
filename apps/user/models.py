# -*- coding: utf-8 -*-
# 用户
# @File    : models.py
# @Date    : 2021-03-24
# @Author  : yuruhao
from sqlalchemy import Column, Integer, String

from db.mysql import Base


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, autoincrement=True)
    login_name = Column(String(20))
    cn_name = Column(String(20))
    en_name = Column(String(20))
    password = Column(String(20))

