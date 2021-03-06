"""
@file: api.py
@author: rrh
@time: 2021/3/27 10:26 下午
"""
from fastapi import Query, APIRouter, Form

from apps.books.models import Books
from base.basemodel import BookItem
from base.parsedata import return_data
from db.mysql import session

book_router = APIRouter()


@book_router.post('/publish/book/')
async def pulish_book(title: str, new_percent: float, author: str = Query('', max_length=50), pub_com: str = None,
                      can_email: bool = True):
    """
    发布书籍
    :param title: 书籍名称
    :param new_percent: 新旧程度
    :param author: 作者
    :param pub_com: 出版社
    :return:
    """
    book = Books(title=title, new_percent=new_percent, author=author, pub_com=pub_com)
    session.add(book)
    session.commit()
    return return_data()


@book_router.put('/edit/book/')
async def post(book: BookItem):
    book_obj = session.query(Books).filter_by(id=book.id).first()
    if not book:
        return return_data(msg='没有找到该书籍', code=404)
    book_obj.title = book.title
    book_obj.new_percent = book.new_percent
    book_obj.author = book.author
    book_obj.pub_com = book.pub_com
    session.commit()
    session.close()
    return return_data(data={"title": book.title})


@book_router.get('/book/list/')
async def book_list(user_id:int=Form(None)):
    books = session.query(Books).all()
    return return_data(data_list=books)
