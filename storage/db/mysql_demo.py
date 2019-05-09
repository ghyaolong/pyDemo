#!/usr/bin/python3
# -*- coding:UTF-8-*-
'''
@File:mysql_demo.py
@Author: Yaochenglong
@Date :操作关系型数据库 mysql
@Desc:
'''

import pymysql

#  创建数据库
# db = pymysql.connect(host='localhost',user='root',password='123456789',port=3306)
# cursor = db.cursor()
# cursor.execute('SELECT VERSION()')
# data = cursor.fetchone()
# print('Database version:',data)
# cursor.execute('create database spiders default character set UTF8MB4')
# db.close()


#创建表
# db = pymysql.connect(host='localhost',user='root',password='123456789',port=3306,db='spiders')
# cursor = db.cursor()
# sql = 'CREATE TABLE IF NOT EXISTS students(id varchar(255) not null,name varchar(255) not null ,age int not null ,primary key(id))'
# cursor.execute(sql)
# db.close()


## 插入数据

id = '20120001'
user = 'Bob'
age = 20
db = pymysql.connect(host='localhost',user='root',password='123456789',port=3306,db='spiders')
cursor = db.cursor()
#  style 1
# sql = 'INSERT INTO students(id,name,age) values(%s,%s,%s)'
# try:
#     cursor.execute(sql,(id,user,age))
#     db.commit()
# except:
#     db.rollback()
# db.close()

#  style 2
# data = {
#     'id':'20120001',
#     'name':'Bob',
#     'age':20
# }
# print(tuple(data.values()))
# table = 'students'
# keys = ', '.join(data.keys())
# values = ', '.join(['%s']*len(data))
# sql = 'INSERT INTO {table}({keys}) vlaues ({keys})'.format(table=table,keys = keys,values=values)
# try:
#     if cursor.execute(sql,tuple(data.values())):
#         print('Successful')
#         db.commit()
# except:
#     print('Faild')
#     db.rollback()
# db.close()


##  更新数据
# sql = 'UPDATE students set age = %s where name = %s'
# try:
#     cursor.execute(sql,(25,'Bob'))
#     db.commit()
# except:
#     db.rollback()
# db.close()


## 删除数据
# table = 'students'
# condition = 'age > 20'
# sql = 'DELETE FROM {table} where {condition}'.format(table=table,condition = condition)

## 查询数据

##  如果数据量大的话，建议不要使用fetchall方法，应该使用fetchone一条一条取
sql = 'select * from students where age >20'
try:
    cursor.execute(sql)
    print('count:',cursor.rowcount)
    one = cursor.fetchone()
    print('one:',one)
    results = cursor.fetchall()
    print('result:',results)
    print('result type',type(results))
    ### 使用fetchone一条一条取
    # row = cursor.fetchone()
    # while row:
    #     print('row:',row)
    #     row = cursor.fetchone()
    
    for row in results:
        print(row)
except Exception as e:
    print('Error:',e)






