# -*- coding: utf-8 -*-
# 
# @File    : security.py
# @Date    : 2021-04-01
# @Author  : yuruhao
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/user/login")
