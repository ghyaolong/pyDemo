#!/usr/bin/python3
# -*- coding:UTF-8-*-
'''
@Desc:
@Author: Yaochenglong
@Email: 289911401@qq.com
@Date : 

'''
from requests import Request,Session
url = 'http://httpbin.org/post'

data = {
    'name':'jackson'
}

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36'
}

s = Session()

req = Request('POST',url,headers)
preped = s.prepare_request(req)
r = s.send(preped)
print(r.text)