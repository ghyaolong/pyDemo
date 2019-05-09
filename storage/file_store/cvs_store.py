#!/usr/bin/python3
# -*- coding:UTF-8-*-
'''
@File:cvs_store.py
@Author: Yaochenglong
@Date :
@Desc: CSV文件存储
'''
import csv
import pandas as pd

# with open('data.csv','w',newline='') as csvfile:
#     writer = csv.writer(csvfile,delimiter=',')
#     writer.writerow(['id','name','age'])
#     writer.writerow(['10001','Mike','20'])
#     writer.writerow(['10002', 'Bob', '22'])
#     writer.writerow(['10003', '荆轲', '2000'])
#     #或
#     writer.writerows([['10004', '荆轲', '2000'],['10005', '荆轲', '2000']])
#
# ## 写入字典
# with open('data.csv','w',newline='',encoding='utf8') as csvfile:
#     fieldnames=['id','name','age']
#     writer = csv.DictWriter(csvfile,fieldnames=fieldnames)
#     writer.writeheader()
#     writer.writerow({'id':'1006','name':'荆轲','age':22})
#     writer.writerow({'id':'1007','name':'荆轲12', 'age': 22})


#####################        读   取     ###################
# with open('data.csv','r',encoding='utf-8') as csvfile:
#     reader = csv.reader(csvfile)
#     for row in reader:
#         print(row)


df = pd.read_csv('data.csv')
print(df)






