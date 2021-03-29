# -*- coding: utf-8 -*-
# 用户
# @File    : models.py
# @Date    : 2021-03-24
# @Author  : yuruhao
from datetime import datetime

from sqlalchemy import Column, Integer, String, Date, DateTime
from sqlalchemy.orm import relationship

from db.mysql import Base


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    login_name = Column(String(20))
    cn_name = Column(String(20))
    en_name = Column(String(20))
    password = Column(String(50))
    gender = Column(String(5))
    nick_name = Column(String(20))
    birth = Column(Date())
    location = Column(String(100))
    desc = Column(String(100))
    main_page = Column(String(50))
    company = Column(String(30))
    school = Column(String(30), nullable=True)
    update_time = Column(DateTime, onupdate=datetime.now, default=datetime.now)
    create_time = Column(DateTime, default=datetime.now)
    comments = relationship('Comment')
