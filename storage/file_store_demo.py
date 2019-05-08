#!/usr/bin/python3
# -*- coding:UTF-8-*-
'''
@File:file_store_demo.py
@Author: Yaochenglong
@Date :
@Desc:
'''
import requests
from pyquery import PyQuery as qp

url = 'https://www.zhihu.com/explore'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36'
}
html = requests.get(url,headers=headers).text
doc = qp(html)
items = doc('.explore-feed.feed-item').items()
for item in items:
    question = item.find('h2').text()
    author = item.find('.author-link-line').text()
    #print(item.find('.content').html())
    answer = qp(item.find('.content').html()).text()
    file = open('explore.txt','a',encoding='utf8')
    file.write('\n'.join([question,author,answer]))
    file.write('\n'+'='*50+'\n')
    file.close()

