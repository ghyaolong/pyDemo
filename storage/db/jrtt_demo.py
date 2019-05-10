#!/usr/bin/python3
# -*- coding:UTF-8-*-
'''
@File:
@Author: Yaochenglong
@Email: 289911401@qq.com
@Date :
@Desc:爬取今日头条街拍美图
'''
import requests,os
from urllib.parse import urlencode
from hashlib import md5
from multiprocessing.pool import Pool


def get_page(offset):
    params = {
        'aid': '24',
        'app_name': 'web_search',
        'offset': offset,
        'format': 'json',
        'keyword': '街拍',
        'autoload': 'true',
        'en_qc': '1',
        'cur_tab': '1',
        'count': '20',
        'from': 'search_tab',
        'pd': 'synthesis'
    }
    url = 'https://www.toutiao.com/api/search/content/?'+urlencode(params)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36',
        'x-requested-with':'XMLHttpRequest'
    }
    print(url)
    try:
        #url1 = 'https://www.toutiao.com/api/search/content/?aid=24&app_name=web_search&offset=0&format=json&keyword=%E8%A1%97%E6%8B%8D&autoload=true&count=20&en_qc=1&cur_tab=1&from=search_tab&pd=synthesis&timestamp=1557415299886'
        resposne = requests.get(url,headers = headers)
        if resposne.status_code == 200:
            print(resposne.json())
            return resposne.json()
    except Exception as e:
        print(e)
        return None



def get_images(json):
    if json.get('data'):
        for item in json.get('data'):
            title = item.get('title')
            images = item.get('iamge_list')
            for image in images:
                yield{
                    'image':image.get('url'),
                    'title':title
                }

def save_image(item):
    if not os.path.exists(item.get('title')):
        os.mkdir(item.get('title'))
    try:
        response = requests.get(item.get('image'))
        if response.status_code == 200:
            file_path = '{0}/{1}.{2}'.format(item.get('title'),md5(response.content).hexdigest(),'jpg')
            if not os.path.exists(file_path):
                with open(file_path,'wb') as f:
                    f.write(response.content)
            else:
                print('Already Download',file_path)
    except requests.ConnectionError:
        print('Faild to save Image')

def main(offset):
    json = get_page(offset)
    for item in get_images(json):
        print(item)
        save_image(item)


GROUP_START = 1
GROUP_END = 5

if __name__ == '__main__':
    # pool = Pool()
    # groups = ([x*20 for x in range(GROUP_START,GROUP_END+1)])
    # pool.map(main,groups)
    # pool.close()
    # pool.join()
    get_page(20)