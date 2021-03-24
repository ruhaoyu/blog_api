# -*- coding: utf-8 -*-
# 返回数据统一处理
# @File    : parsedata.py
# @Date    : 2021-03-22
# @Author  : yuruhao


def return_data(msg='ok', code=200, data=''):
    return {'msg': msg, 'code': code, 'data': data}
