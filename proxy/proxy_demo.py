#!/usr/bin/python3
# -*- coding:UTF-8-*-
'''
@File:
@Author: Yaochenglong
@Email: 289911401@qq.com
@Date :
@Desc:
'''
# from urllib.error import URLError
# from urllib.request import ProxyHandler,build_opener
#
# proxy = '119.101.112.9:9999'
# proxy_handler = ProxyHandler({
#     'http':'http://'+ proxy,
#     'https':'https://'+ proxy
# })
#
# opener = build_opener(proxy_handler)
# try:
#     response = opener.open('http://httpbin.org/get')
#     print(response.read().decode('utf8'))
# except URLError as e:
#     print('错误：',e.reason)


## requests

import requests

proxy = '127.0.0.1:9743'
proxies = {
    'http': 'http://' + proxy,
    'https': 'https://' + proxy
}
try:
    response = requests.get('http://httpbin.org/get',proxies=proxies)
    print(response.text)
except requests.exceptions.ConnectionError as e:
    print(e.args)

