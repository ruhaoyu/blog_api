# -*- coding: utf-8 -*-

# @File    : api.py
# @Date    : 2021-03-18
# @Author  : yuruhao

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm

from apps.blog.models import Article
from apps.user.models import User
from apps.user.usercenter import UserBaseModel, get_current_user, fake_users_db, UserInDB, fake_hash_password
from base.base_enum import LoginNameEnum
from base.parsedata import return_data
from db.mysql import session

user_router = APIRouter()


@user_router.post("/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user_dict = fake_users_db.get(form_data.username)
    if not user_dict:
        raise HTTPException(status_code=400, detail="用户名密码错误")
    user = UserInDB(**user_dict)
    hashed_password = fake_hash_password(form_data.password)
    if not hashed_password == user.hashed_password:
        raise HTTPException(status_code=400, detail="用户名密码错误")

    return {"access_token": user.username, "token_type": "bearer"}


@user_router.get('/{}')
async def login_by_third_paty(name: LoginNameEnum):
    return return_data(data={'name': name})


@user_router.get("/users/me")
async def read_users_me(current_user: UserBaseModel = Depends(get_current_user)):
    return current_user


@user_router.get('/files/{file_path:path}')
async def path_test(file_path):
    return return_data(data={'file_path': file_path})


@user_router.get('/user/profile/{user_id}')
async def user_profile(user_id: int):
    user_obj = session.query(User).get(user_id)
    return return_data(data=user_obj)


@user_router.get('/user/articles/{user_id}')
async def user_articles(user_id: int):
    articles = session.query(Article).filter(Article.user_id == user_id).all()
    return return_data(data_list=articles)
