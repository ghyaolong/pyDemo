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


headers = {
    'User-Agent':'xxx'
}

req = requests.get('https://www.baidu.com',headers = headers)