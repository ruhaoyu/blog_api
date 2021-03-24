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
