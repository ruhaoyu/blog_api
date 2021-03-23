# -*- coding: utf-8 -*-
# 数据模型
# @File    : basemodel.py
# @Date    : 2021-03-22
# @Author  : yuruhao

from fastapi import Query
from pydantic import BaseModel


class BookItem(BaseModel):
    id: int = ''
    title: str = Query(..., max_length=20, min_length=1, regex='', title='名字必须是全名',
                       description='名称必须是正式书名')
    new_percent: float=Query(..., le=0, gt=100)
    author: str
    pub_com: str = ''
