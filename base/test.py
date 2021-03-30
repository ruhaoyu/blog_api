# -*- coding: utf-8 -*-
# 书籍交换
# @File    : test.py
# @Date    : 2021-03-22
# @Author  : yuruhao
from fastapi import Query

from apps.books.models import Books
from base.basemodel import BookItem
from db.mysql import session
from base.parsedata import return_data



