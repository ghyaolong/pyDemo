#!/usr/bin/python3
# -*- coding:UTF-8-*-
'''
@File:redis_demo.py
@Author: Yaochenglong
@Date :
@Desc:redis数据库操作用例
在使用之前，请确保安装好了redis-py库,如果要做导入导出的话，还需要安装RedisDump。
pip install redis
pip ubstakk redis-dump
'''
from redis import StrictRedis,ConnectionPool
#连接redis
# redis = StrictRedis(host='localhost',port=6379,db=0,password='')
# redis.set('name','Bob')
# print(redis.get('name'))

#使用connectionPool来连接
# pool = ConnectionPool(host='localhost',port='6379',db=0,decode_responses=True)
# redis = StrictRedis(connection_pool=pool)
# print(redis.get('name'))

url = 'redis://@localhost:6379/0'
pool = ConnectionPool.from_url(url)
redis = StrictRedis(connection_pool=pool)
print(redis.get('name'))
print(redis.randomkey())
print(redis.flushdb())
#键操作  字符串操作  redis的基础操作 再次省略......


## RedisDump :redis数据的导入导出功能










