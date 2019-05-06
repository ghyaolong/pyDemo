#!/usr/bin/python3
# -*- coding:UTF-8-*-
'''
@File:spider.py
@Author: Yaochenglong
@Date :
@Desc:
'''
import requests
# import requests
# r = requests.get('https://github.com/favicon.ico')
# with open('favicon.ico','wb') as f:
#     f.write(r.content)


###     上传文件
# files = {'file':open('favicon.ico','rb')}
# r = requests.post('http://httpbin.org/post',files = files)
# print(r.text)


###   Cookies
# r = requests.get('https://www.baidu.com')
# print(r.cookies)
#
# for key,value in r.cookies.items():
#     print(key+ '='+value)



###   session的使用

# s = requests.Session()
# s.get('http://httpbin.org/cookies/set/number/123123')
# r = s.get('http://httpbin.org/cookies')
# print(r.text)



###   SSL 证书认证
# import logging
# #requests.packages.urllib3.disable_warnings()
# logging.captureWarnings(True)
#
#
# resposne  = requests.get('https://www.12306.cn',verify = False)
# #或者可以指定本地证书作为客户端证书，还可以是单个文件(包含秘钥和证书)或一个包含两个文件的元组
# #resposne  = requests.get('https://www.12306.cn',cert=('/path/server.crt','/path/key'))
#
# print(resposne.status_code)


###         代理
# proxies = {
#     #'http':'http:user:password@10.10.1.10:3128',  ## 如果代理需要用户名和密码的话，可以这么写
#
#     #使用socks协议代理
#     #'http':'socks5://127.0.0.1:9999',
#
#     'http':'http://10.10.1.10:3128',
#     'https':'https://10.10.1.10:1080'
# }
#
# requests.get('https://www.taobao.com',proxies=proxies)



## 超时设置

# r = requests.get('https://www.taobao.com',timeout=(5,11))
# print(r.status_code)


##  身份认证
# from requests.auth import HTTPBasicAuth
# r = requests.get('http://localhost:8760',auth = HTTPBasicAuth('username','password'))
# 或者使用下面的简写方式
# r = requests.get('http://localhost:8760',auth = ('username','password'))
# print(r.status_code)

## 使用oath1认证
# from requests_oauthlib import OAuth1
#
# url = 'https://api.twiter.com/1.1/account/verify_credentials.json'
# auth = OAuth1('YOUR_APP_KEY','YOUR_APP_SECRET','USER_OAUTH_TOKEN','USER_OAUTH_TOKEN_SECRET')
# requests.get(url,auth = auth)


##  Prepared Request
from requests import Request,Session
url = 'http://httpbin.org/post'
data = {
    'name':'germy',
    'age':22
}

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36'
}
s = Session()
req = Request('POST',url,data=data,headers=headers)
prepped = s.prepare_request(req)
resposne = s.send(prepped)
print(resposne.text)











