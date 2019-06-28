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
client = pymongo.MongoClient(host='localhost',port=27017)
db = client['DB']
collection = db['student']
student = {
    'id':'20170001',
    'name':'json',
    'age':20,
    'gender':'male'
}
result = collection.insert_one(student)
print(result)

