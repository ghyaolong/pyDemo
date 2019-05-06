#!/usr/bin/python3
# -*- coding:UTF-8-*-
'''
@File:maoyan_spider.py
@Author: Yaochenglong
@Date :
@Desc:抓取猫眼电影的排行 ,地址 https://maoyan.com/board/4?offset=20
'''

import requests
import re

def get_one_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36'
    }
    r = requests.get(url=url, headers=headers)
    reg = re.compile('<dd>.*?board-index.*?>(.*?)</i>.*?data-src="(.*?)".*?name.*?a.*?>(.*?)</a>.*?star.*?>(.*?)</p>.*?releasetime.*?>(.*?)</p>.*?integer.*?>(.*?)</i>.*?fraction.*?>(.*?)</i>.*?</dd>',re.S)
    #reg = re.compile('<dd>.*?board-index.*?>(.*?)</i>.*?data-src="(.*?)".*?name.*?a.*?>(.*?)</a>.*?star.*?>(.*?)</p>.*?releasetime.*?>(.*?)</p>.*?integer.*?>(.*?)</i>.*?fraction.*?>(.*?)</i>.*?</dd>',re.S)
    items = reg.findall(r.text)
    for item in items:
        print(item)


def main():
    url = 'https://maoyan.com/board/4'
    html = get_one_page(url)
    print(html)

main()



