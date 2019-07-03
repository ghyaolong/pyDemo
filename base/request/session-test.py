#!/usr/bin/python3
# -*- coding:UTF-8-*-
'''
@Desc:
@Author: Yaochenglong
@Email: 289911401@qq.com
@Date : 

'''

import requests

s = requests.Session()
s.get('http://httpbin.org/cookies/set/number/123456')
r = s.get('http://httpbin.org/cookies')
print(r.text)