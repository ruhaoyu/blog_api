# -*- coding: utf-8 -*-
# 
# @File    : usercenter.py
# @Date    : 2021-04-01
# @Author  : yuruhao
from typing import Optional

from fastapi import Depends, HTTPException
from pydantic import BaseModel

from security import oauth2_scheme

fake_users_db = {
    "johndoe": {
        "username": "johndoe",
        "full_name": "John Doe",
        "email": "johndoe@example.com",
        "hashed_password": "fakehashed1",
        "disabled": False,
    },
    "alice": {
        "username": "alice",
        "full_name": "Alice Wonderson",
        "email": "alice@example.com",
        "hashed_password": "fakehashed2",
        "disabled": True,
    },
}


class UserBaseModel(BaseModel):
    username: str
    email: Optional[str] = None
    full_name: Optional[str] = None
    disabled: Optional[bool] = None


class UserInDB(UserBaseModel):
    hashed_password: str


def get_user(db, username: str):
    if username in db:
        user_dict = db[username]
        return UserInDB(**user_dict)
    return HTTPException(status_code=400, detail="用户名密码错误")


def fake_hash_password(password: str):
    return "fakehashed" + password


def fake_decode_token(token):
    user = get_user(fake_users_db, token)
    return user


async def get_current_user(token: str = Depends(oauth2_scheme)):
    user = fake_decode_token(token)
    return user


async def get_current_active_user(current_user: UserBaseModel = Depends(get_current_user)):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="用户未激活")
    return current_user
