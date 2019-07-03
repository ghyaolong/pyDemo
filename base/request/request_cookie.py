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

r = requests.get('http://www.baidu.com')

print(r.cookies)

for key,value in r.cookies.items():
    print(key+'='+value)