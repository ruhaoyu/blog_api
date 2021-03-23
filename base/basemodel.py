# -*- coding: utf-8 -*-
# 数据模型
# @File    : basemodel.py
# @Date    : 2021-03-22
# @Author  : yuruhao
from fastapi import Query
from pydantic import BaseModel


class BookItem(BaseModel):
    id: int = ''
    title: str = Query('', max_length=5)
    new_percent: str
    author: str
    pub_com: str = ''
