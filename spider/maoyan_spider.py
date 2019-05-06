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
import json
from requests.exceptions import RequestException
import time
def get_one_page(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36'
        }
        r = requests.get(url=url, headers=headers)
        if r.status_code == 200:
            return r.text
    except RequestException:
        return None

def parse_one_page(html):
    reg = re.compile('<dd>.*?board-index.*?>(.*?)</i>.*?data-src="(.*?)".*?name.*?a.*?>(.*?)</a>.*?star.*?>(.*?)</p>.*?releasetime.*?>(.*?)</p>.*?integer.*?>(.*?)</i>.*?fraction.*?>(.*?)</i>.*?</dd>',re.S)
    items = re.findall(reg,html)
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

def write_to_file(context):
    with open('result.txt','a',encoding='utf8') as f:
        f.write(json.dumps(context,ensure_ascii=False)+'\n')

def main(offset):
    url = 'https://maoyan.com/board/4?offset='+str(offset)
    html = get_one_page(url)
    for item in parse_one_page(html):
        print(item)
        write_to_file(item)

if __name__ == '__main__':
    for i in range(10):
        main(offset=i*10)
        time.sleep(1)



