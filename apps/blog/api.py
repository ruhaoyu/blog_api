# -*- coding: utf-8 -*-
# 
# @File    : api.py
# @Date    : 2021-03-24
# @Author  : yuruhao
from sqlalchemy import Enum

from apps.blog.blog_enum import ArticleStatusEnum
from base.parsedata import return_data
from routers import router


@router.get('/article/list/')
def get_article_list(status: ArticleStatusEnum, article_type: str='public', free: bool = True,
                     user_id: int = 0):
    if user_id:
        article_list = [1, 3, 4]
    else:
        article_list = [5, 6, 7]
    if article_type:
        article_list = [0, 0, 0]
    return return_data(data_list=article_list)
