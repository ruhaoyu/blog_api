# -*- coding: utf-8 -*-

# @File    : api.py
# @Date    : 2021-03-18
# @Author  : yuruhao

from apps.user.models import User
from base.base_enum import LoginNameEnum
from base.parsedata import return_data
from db.mysql import session
from routers import router


@router.get('/')
async def index():
    return return_data()


@router.get('/login')
async def login():
    return return_data()


@router.get('/{}')
async def login_by_third_paty(name: LoginNameEnum):
    return return_data(data={'name': name})


@router.get('/files/{file_path:path}')
async def path_test(file_path):
    return return_data(data={'file_path': file_path})


@router.get('/user/profile/{user_id}')
async def user_profile(user_id: int):
    user_obj = session.query(User).get(user_id)
    return return_data(data=user_obj)



