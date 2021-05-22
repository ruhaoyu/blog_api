# -*- coding: utf-8 -*-
# 博客
# @File    : models.py
# @Date    : 2021-03-24
# @Author  : yuruhao
import enum
from datetime import datetime

from sqlalchemy import Column, Integer, String, Float, DateTime, Text, Enum, Boolean, ForeignKey, Table
from sqlalchemy.dialects.mysql import LONGTEXT
from sqlalchemy.orm import relationship, backref

from db.mysql import Base


class StatusEnum(str, enum.Enum):
    draft = 'draft'
    normal = 'normal'
    delete = 'delete'


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
    user = relationship('User', backref=backref("article", lazy="dynamic"))
    type = Column(Enum('public', 'private'), default='public')
    status = Column(Enum('draft', 'normal', 'delete', 'test', 'doing'), default='draft')
    free = Column(Boolean, default=True)
    like_num = Column(Integer, default=0)
    dislike_num = Column(Integer, default=0)
    read_num = Column(Integer, default=0)
    pub_time = Column(DateTime, default=datetime.now)
    update_time = Column(DateTime, onupdate=datetime.now, default=datetime.now)


class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True, autoincrement=True)
    detail = Column(String(200), nullable=False)
    img_url = Column(String(100))
    pub_time = Column(DateTime, default=datetime.now)
    article_id = Column(Integer, ForeignKey('article.id'))
    article = relationship('Article', backref=backref("comments", lazy="joined"))

    user_id = Column(Integer, ForeignKey('user.id'), nullable=True)
    status = Column(Enum('draft', 'normal', 'delete'), default='draft')


class CommentOperate(Base):
    __tablename__ = 'comment_operate'
    id = Column(Integer, primary_key=True, autoincrement=True)
    type = Column(Enum('like', 'dislike', 'collect', 'report'), default='like')
    extra = Column(String(200), nullable=False, comment="备注信息")
    comment_id = Column(Integer, ForeignKey('comment.id'), nullable=True, comment='评论')
    comment = relationship('Comment', backref=backref("operates", lazy="joined"))

