# -*- coding: utf-8 -*-
# 用户中心
# @File    : usercenter.py
# @Date    : 2021-03-18
# @Author  : yuruhao
from apps.user.models import User
from base.base_enum import LoginNameEnum
from db.mysql import session
from base.parsedata import return_data
from routers import router


@router.get('/login')
async def login():
    return return_data()


@router.get('/profile/{user_id}')
async def user_profile(user_id: int):
    user = session.query(User).filter_by(id=user_id).first()
    if not user:
        return return_data(code=404, msg='用户不存在')
    return return_data(data={'id': user_id, 'login_name': user.login_name, 'cn_name': user.cn_name})


@router.get('/{}')
async def login_by_third_paty(name: LoginNameEnum):
    return return_data(data={'name': name})


@router.get('/files/{file_path:path}')
async def path_test(file_path):
    return return_data(data={'file_path': file_path})


