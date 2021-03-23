# -*- coding: utf-8 -*-

# @File    : index.py
# @Date    : 2021-03-18
# @Author  : yuruhao

from parsedata import return_data
from routers import router


@router.get('/')
async def index():
    return return_data()
