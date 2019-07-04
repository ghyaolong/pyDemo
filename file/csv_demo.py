#!/usr/bin/python3
# -*- coding:UTF-8-*-
'''
@Desc:
@Author: Yaochenglong
@Email: 289911401@qq.com
@Date : 2019/7/4 10:45
'''

import csv

# with open('data.csv','w',newline='') as csvfile:
#     writer = csv.writer(csvfile,delimiter=' ')
#     writer.writerow(['id','name','age'])
#     writer.writerow(['1','张三','男'])
#     writer.writerow(['2','张死', '男'])
#     writer.writerows([['3','张死', '男'],['4','张死', '男']])


with open('datadict.csv','w',newline='',encoding='utf-8') as csvfile:
    fieldname = ['id','name','age']
    writer = csv.DictWriter(csvfile,fieldname)
    writer.writeheader()
    writer.writerow({'id':'1','name':'zhagnsan','age':'女'})


# csv库读取
import csv

with open('datadict.csv','r',encoding='utf-8') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
print('='*50)

# pandas读取csv
import pandas as pd
df = pd.read_csv('datadict.csv')
print(df)
print(df.columns)
print(df.index)



