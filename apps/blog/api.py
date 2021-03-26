# -*- coding: utf-8 -*-
# 
# @File    : api.py
# @Date    : 2021-03-24
# @Author  : yuruhao
from typing import List

from sqlalchemy import Enum, and_

from apps.blog.blog_enum import ArticleStatusEnum
from apps.blog.items import ArticleItem, AddCommentItem
from apps.blog.models import Article, Comment
from base.parsedata import return_data
from db.mysql import session
from routers import router


@router.post('/pub/article/')
async def public_article(article: ArticleItem):
    article_obj = Article(title=article.title, detail=article.detail)
    session.add(article_obj)
    session.commit()
    return return_data()


@router.get('/article/{article_id}')
async def article_detail(article_id: int):
    article_obj = session.query(Article).get(article_id)
    comments = article_obj.comments
    return return_data(data=article_obj)


@router.get('/like/article/{article_id')
async def like_article(article_id: int):
    article_obj = session.query(Article).get(article_id)
    article_obj.like_num += 1
    session.commit()
    # todo 生成一条谁点赞谁的文章记录
    return return_data()


@router.get('/article/list/')
def get_article_list(status: ArticleStatusEnum, article_type: str = 'public', free: bool = True,
                     user_id: int = 0):
    article_obj_list = session.query(Article).filter_by(status=status.value, type=article_type, free=free)
    if user_id:
        article_obj_list = article_obj_list.filter(Article.user_id == user_id)
    return return_data(data_list=article_obj_list.all())


@router.post('/add/comment/{article_id}')
async def add_comment(article_id: int, comment: AddCommentItem):
    comment_obj = Comment(detail=comment.detail, img_url=comment.img_url, article_id=article_id)
    session.add(comment_obj)
    session.commit()
    return return_data()


@router.post('/delete/article')
async def delete_article(article_ids: List[int]):
    return return_data(data_list=article_ids)
