#!/usr/bin/python3
'''
post 请求带参数
'''
import urllib.parse
import urllib.request
import socket

data = bytes(urllib.parse.urlencode({'world':'hello'}),'utf-8')
try:
    response = urllib.request.urlopen('http://httpbin.org/get',timeout=0.1)
except urllib.error.URLError as e:
    if isinstance(e.reason,socket.timeout):
        print('TIME_OUT')
    
print(response.read().decode('utf-8'))