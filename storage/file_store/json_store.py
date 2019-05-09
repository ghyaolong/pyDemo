#!/usr/bin/python3
# -*- coding:UTF-8-*-
'''
@File:json_store.py
@Author: Yaochenglong
@Date :
@Desc:
'''

import json
str = '''
[{
"name":"Bob",
"gender":"male",
"birthday":"2015-02-12"
}]
'''
# print(type(str))
# data = json.loads(str)
# print(type(data))
# print(data[0]['name'])
# print(data[0].get('name'))
# print(data[0].get('age',25))

# with open('data.json') as file:
#     str = file.read()
#     data = json.loads(str)
#     print(data)
#     print(type(data))

#  输出json
data=[{
"name":"张伟",
"gender":"male",
"birthday":"2015-02-12"
}]
with open('data.json','w') as file:
    file.write(json.dumps(data,indent=2,ensure_ascii=False))


