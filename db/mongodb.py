#!/usr/bin/python3
# -*- coding:UTF-8-*-
'''
@File:
@Author: Yaochenglong
@Email: 289911401@qq.com
@Date :
@Desc:
'''
import pymongo
client = pymongo.MongoClient(host='localhost',port=27017)  # 或client = pymongo.MongoClient('mongodb://localhost:27017/')
# 指定数据库
db = client['DB']
collection = db['student']
student = {
    'id':'20170002',
    'name':'lisi',
    'age':20,
    'gender':'male'
}
result = collection.insert_one(student)
print(result)

