# -*- coding: utf-8 -*-
# 
# @File    : api.py
# @Date    : 2021-03-24
# @Author  : yuruhao
from typing import List

from fastapi import Cookie
from sqlalchemy import Enum, and_
from sqlalchemy.testing import in_

from apps.blog.blog_enum import ArticleStatusEnum
from apps.blog.items import ArticleItem, AddCommentItem
from apps.blog.models import Article, Comment, CommentOperate
from base.parsedata import return_data
from db.mysql import session

from fastapi import APIRouter, Query

blog_router = APIRouter()


@blog_router.post('/pub/article/')
async def public_article(article: ArticleItem):
    article_obj = Article(**article.dict())
    session.add(article_obj)
    session.commit()
    return return_data()


@blog_router.get('/article/{article_id}')
async def article_detail(article_id: int):
    article_obj = session.query(Article).get(article_id)
    return return_data(data=article_obj)


@blog_router.get('/like/article/{article_id')
async def like_article(article_id: int):
    article_obj = session.query(Article).get(article_id)
    article_obj.like_num += 1
    session.commit()
    # todo 生成一条谁点赞谁的文章记录
    return return_data()


@blog_router.get('/article/list/')
def get_article_list(status: ArticleStatusEnum, article_type: str = 'public', free: bool = True,
                     user_id: int = Query(default=0)):
    article_obj_list = session.query(Article).filter_by(type=article_type, free=free)
    if user_id:
        article_obj_list = article_obj_list.filter(Article.user_id == user_id)
    return return_data(data_list=article_obj_list.all())


@blog_router.post('/add/comment/{article_id}')
async def add_comment(article_id: int, comment: AddCommentItem):
    comment_obj = Comment(detail=comment.detail, img_url=comment.img_url, article_id=article_id)
    session.add(comment_obj)
    session.commit()
    return return_data()


@blog_router.get('/comment/{comment_id}')
async def comment_detail(comment_id: int):
    comment = session.query(Comment).filter(Comment.id == comment_id).first()
    return return_data(data=comment)


@blog_router.get('/comment/operate/{id}')
async def comment_operate_detail(id: int):
    comment_operate = session.query(CommentOperate).filter(CommentOperate.id == id).first()
    return return_data(data=comment_operate)


@blog_router.post('/update/article/status')
async def updata_article_status(status: ArticleStatusEnum, article_ids: List[int] = Query(...)):
    print(status.value)
    session.query(Article).filter(Article.id.in_(article_ids)).update({'status': status.value})
    session.commit()
    return return_data(data_list=article_ids)


@blog_router.get('/newst/comment/list/{user_id}')
async def newst_comment_list(user_id: int):
    comments_list = session.query(Comment).filter()
    return return_data(data_list=comments_list)


@blog_router.get('/test/cookies/')
async def test(cookie: str = Cookie(None)):
    print(cookie)
    return return_data(data=cookie)
