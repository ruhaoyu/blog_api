# -*- coding: utf-8 -*-
# 
# @File    : api.py
# @Date    : 2021-03-24
# @Author  : yuruhao
from sqlalchemy import Enum, and_

from apps.blog.blog_enum import ArticleStatusEnum
from apps.blog.items import ArticleItem
from apps.blog.models import Article
from base.parsedata import return_data
from db.mysql import session
from routers import router


@router.get('/article/list/')
def get_article_list(status: ArticleStatusEnum, article_type: str = 'public', free: bool = True,
                     user_id: int = 0):
    article_obj_list = session.query(Article).filter(
        and_(Article.status == status.value, Article.type == article_type, Article.free == free))
    if user_id:
        article_obj_list = article_obj_list.filter(Article.user_id==user_id)
    return return_data(data_list=article_obj_list.all())


@router.post('/pub/article/')
async def public_article(article: ArticleItem):
    article_obj = Article(title=article.title, detail=article.detail)
    session.add(article_obj)
    session.commit()
    return return_data()
