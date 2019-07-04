#!/usr/bin/python3
# -*- coding:UTF-8-*-
'''
@Desc:
@Author: Yaochenglong
@Email: 289911401@qq.com
@Date : 2019/7/4 11:23
'''

import pymysql

db = pymysql.connect(host='localhost',user='root',password='123456789',port=3306)
cursor = db.cursor()
cursor.execute('SELECT VERSION()')
data = cursor.fetchone()
print(data)

