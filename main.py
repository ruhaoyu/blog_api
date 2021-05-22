# -*- coding: utf-8 -*-

# @File    : main.py
# @Date    : 2021-03-17
# @Author  : yuruhao
import uvicorn
from fastapi import FastAPI, Depends, HTTPException, Query, APIRouter
# from fastapi.openapi.docs import (
#     get_redoc_html,
#     get_swagger_ui_html,
#     get_swagger_ui_oauth2_redirect_html,
# )
# from fastapi.staticfiles import StaticFiles
from apps.blog.blog_enum import ArticleStatusEnum
from apps.blog.models import Article
from apps.user import user_router
from apps.blog import blog_router
from apps.books import book_router
from base.parsedata import return_data
from db.mysql import session

app = FastAPI(title='简书', version='1.0.0', description='一个优质创作社区')
#
# app = FastAPI(docs_url=None, redoc_url=None, title='书籍互换', version='1.0.0',
#               description='你是否有很多看过的旧书？你是否想得到没看过的新书？何不在这里进行交换？')

# static_path = os.path.join(os.path.basename(__file__), "../..")
# root = os.path.abspath(static_path)
#
# app.mount("/static", StaticFiles(directory=f"{root}/books/static"), name="static")


# @app.get("/docs", include_in_schema=False)
# async def custom_swagger_ui_html():
#     return get_swagger_ui_html(
#         openapi_url=app.openapi_url,
#         title=app.title + " - Swagger UI",
#         oauth2_redirect_url=app.swagger_ui_oauth2_redirect_url,
#         swagger_js_url="/static/js/swagger-ui-bundle.js",
#         swagger_css_url="/static/css/swagger-ui.css",

router = APIRouter()

#     )
@router.get('/article/list/')
def get_article_list(status: ArticleStatusEnum, article_type: str = 'public', free: bool = True,
                     user_id: int = Query(default=0)):
    article_obj_list = session.query(Article).filter_by(type=article_type, free=free)
    if user_id:
        article_obj_list = article_obj_list.filter(Article.user_id == user_id)
    return return_data(data_list=article_obj_list.all())


app.include_router(user_router, prefix='/user', tags=['用户中心接口'])
app.include_router(router, prefix='', tags=['博客文章接口'])
app.include_router(book_router, prefix='/book', tags=['书籍相关接口'])

if __name__ == '__main__':
    uvicorn.run('main:app', host='127.0.0.1', port=8000, reload=True)
