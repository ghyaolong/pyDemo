#!/usr/bin/python3
# -*- coding:UTF-8-*-
'''
@Desc:
@Author: Yaochenglong
@Email: 289911401@qq.com
@Date : 2019/7/4 11:47
'''

from redis import StrictRedis
redis = StrictRedis(host='localhost',port=6379,db=0,password='')

redis.set('name','Bob')
print(redis.get('name'))