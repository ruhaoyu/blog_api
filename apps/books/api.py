# -*- coding: utf-8 -*-
# 
# @File    : api.py
# @Date    : 2021-03-30
# @Author  : yuruhao
from fastapi import Form

from apps.books.models import Books
from base.parsedata import return_data
from routers import router
from db.mysql import session

@router.get('/book/list/')
async def book_list(user_id:int=Form(None)):
    books = session.query(Books).all()
    return return_data(data_list=books)
