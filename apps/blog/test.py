"""
@file: test.py
@author: rrh
@time: 2021/4/16 10:30 下午
"""

from apps.blog.models import *
from apps.user.models import *
from db.mysql import session, engine
# c = Article(title='test', detail='122', user=User(login_name='pipi'))
# try:
#     a = session.add(c)
#     session.commit()
#     print(c.id)
# except Exception as ex:
#     print(ex)
#     session.rollback()
import datetime
start = datetime.datetime.now()
data_list = []
for i in range(40000):
    data_list.append(dict(title=str(i), detail=''))

engine.execute(Article.__table__.insert(), data_list)
print('批量提交', datetime.datetime.now()-start)
session.commit()
print('commit完成', datetime.datetime.now()-start)
