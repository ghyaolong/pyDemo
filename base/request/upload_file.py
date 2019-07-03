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

files = {
    'file':open('favicon.ico','rb')
}

r = requests.post('http://httpbin.org/post',files = files)
print(r.text)