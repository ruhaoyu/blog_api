# -*- coding: utf-8 -*-

# @File    : api.py
# @Date    : 2021-03-18
# @Author  : yuruhao

from fastapi import APIRouter

from apps.user.models import User
from base.parsedata import return_data
from db.mysql import session

user_router = APIRouter()


@user_router.get('/')
async def index():
    return return_data()


@user_router.get('/user/profile/{user_id}')
async def user_profile(user_id: int):
    user_obj = session.query(User).get(user_id)
    return return_data(data=user_obj)
