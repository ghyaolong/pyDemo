#!/usr/bin/python3
# -*- coding:UTF-8-*-
'''
@File:
@Author: Yaochenglong
@Email: 289911401@qq.com
@Date :
@Desc:
'''
import requests

r = requests.get('https://www.baidu.com')
print(r.text)
print(r.content)
print(r.status_code)
print(r.cookies)
print(type(r.cookies))
for item in r.cookies:
    print(item.name+'='+item.value)