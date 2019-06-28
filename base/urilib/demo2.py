#!/usr/bin/python3
'''
post 请求带参数
'''
import urllib.parse
import urllib.request

data = bytes(urllib.parse.urlencode({'world':'hello'}),'utf-8')
response = urllib.request.urlopen('http://httpbin.org/post',data)
print(response.read().decode('utf-8'))