# -*- coding: utf-8 -*-
# 枚举
# @File    : base_enum.py
# @Date    : 2021-03-22
# @Author  : yuruhao
from enum import Enum


class LoginNameEnum(Enum):
    wechat = 'wechat'
    sina = 'sina'
    qq = 'qq'
    email_163 = 'email_163'