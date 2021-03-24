# -*- coding: utf-8 -*-
# 返回数据统一处理
# @File    : parsedata.py
# @Date    : 2021-03-22
# @Author  : yuruhao


def return_data(msg='ok', code=200, data='', data_list=''):
    if not data_list:
        data_list = []
    return {'msg': msg, 'code': code, 'data': data, 'data_list': data_list}
