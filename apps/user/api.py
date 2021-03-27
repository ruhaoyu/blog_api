# -*- coding: utf-8 -*-

# @File    : api.py
# @Date    : 2021-03-18
# @Author  : yuruhao
from apps.user.models import User
from base.parsedata import return_data
from db.mysql import session
from routers import router


@router.get('/')
async def index():
    return return_data()


@router.get('/user/profile/{user_id}')
async def user_profile(user_id: int):
    user_obj = session.query(User).get(user_id)
    return return_data(data=user_obj)
