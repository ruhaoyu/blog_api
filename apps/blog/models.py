# -*- coding: utf-8 -*-
# 博客
# @File    : models.py
# @Date    : 2021-03-24
# @Author  : yuruhao
from datetime import datetime

from sqlalchemy import Column, Integer, String, Float, DateTime, Text, Enum, Boolean, ForeignKey, Table
from sqlalchemy.dialects.mysql import LONGTEXT
from sqlalchemy.orm import relationship, backref

from db.mysql import Base

article_tag = Table('article_like',
                    Base.metadata,
                    Column('article_id', Integer, ForeignKey('article.id'), primary_key=True),
                    Column('user_id', Integer, ForeignKey('user.id'), primary_key=True))


class Article(Base):
    __tablename__ = 'article'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(10), nullable=False)
    detail = Column(LONGTEXT, nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'), comment='创建用户')
    user = relationship('User')
    type = Column(Enum('public', 'private'), default='public')
    free = Column(Boolean, default=True)
    like_num = Column(Integer, default=0)
    dislike_num = Column(Integer, default=0)
    read_num = Column(Integer, default=0)
    status = Column(Enum('draft', 'normal', 'delete'), default='draft')
    comments = relationship('Comment')
    likes = relationship('User', secondary=article_tag, backref=backref('likes'))
    pub_time = Column(DateTime, default=datetime.now)
    update_time = Column(DateTime, onupdate=datetime.now, default=datetime.now)


class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True, autoincrement=True)
    detail = Column(String(200), nullable=False)
    img_url = Column(String(100))
    pub_time = Column(DateTime, default=datetime.now)
    article_id = Column(Integer, ForeignKey('article.id'))
    user_id = Column(Integer, ForeignKey('user.id'))
