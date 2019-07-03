#!/usr/bin/python3
# -*- coding:UTF-8-*-
'''
@Desc:
@Author: Yaochenglong
@Email: 289911401@qq.com
@Date : 

'''

import requests

headers = {
    'Cookie':'_xsrf=K9txDQxz0FfVcXwLkykkey9Kh6ntptke; _zap=831c064d-c5a6-42ce-819f-0902d7ff0be3; d_c0="AOApOO4Kkw-PTkXj3yx4WLzrxP0gzvNTczI=|1560345906"; q_c1=b716c36c9bd1492a817b9648db1218d0|1560345907000|1560345907000; tgw_l7_route=7c109f36fa4ce25acb5a9cf43b0b6415; tst=r; capsion_ticket="2|1:0|10:1561909148|14:capsion_ticket|44:NWY5MTE2YjFiNjdjNDcwOTkyMmYwODYxNzNmZWU0Njc=|3f69a5a2d16fd8d52456bffd118a07da6ed0d4cd9903a7de673e90d87b96b98c"; z_c0="2|1:0|10:1561909152|4:z_c0|92:Mi4xQU1UeEFnQUFBQUFBNENrNDdncVREeVlBQUFCZ0FsVk5vQ1VHWGdCWjdlTjhyVlI3NW1mZkJaUXdYV0k1dUpjeTZR|d6bd95148ce7c95379cd7c591c6897c10ad64efc295593d4d377a56449fd94ff"',
    'Host':'www.zhihu.com',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36'
}

r = requests.get('https://www.zhihu.com',headers = headers)
print(r.content.decode('utf-8'))