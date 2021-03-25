"""
@file: items.py
@author: rrh
@time: 2021/3/24 9:53 下午
"""
from fastapi import Query
from pydantic import BaseModel


class ArticleItem(BaseModel):
    title: str = Query(..., max_length=10, min_length=1)
    detail: str


class AddCommentItem(BaseModel):
    detail: str = Query(..., max_length=200, min_length=1)
    img_url: str = Query(None, max_length=100)
