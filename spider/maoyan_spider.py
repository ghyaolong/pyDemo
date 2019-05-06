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
        #print(item)
        yield {
            'index:':item[0],
            'iamge':item[1],
            'title': item[2].strip(),
            'actor': item[3].strip()[3:] if len(item[3]) > 3 else '',
            'time': item[4].strip()[5:] if len(item[4]) > 5 else '',
            'score': item[5].strip() + item[6].strip()
        }


def main():
    url = 'https://maoyan.com/board/4'
    html = get_one_page(url)
    print(html)

main()



