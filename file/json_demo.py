#!/usr/bin/python3
# -*- coding:UTF-8-*-
'''
@Desc:
@Author: Yaochenglong
@Email: 289911401@qq.com
@Date : 2019/7/4 10:18
'''

import json

str = '''
[
{ "name":"zhangsan",
  "gender":"male"
},
{ "name":"zhangsan2",
  "gender":"female"
}
]
'''

print(type(str))
data = json.loads(str)
print(type(data))
print(data)
print(data[0]['name'])
print(data[0].get('name1','adf'))
print('='*50)
print('输出json')

data = [{'name': '张伟', 'gender': 'male'}, {'name': 'zhangsan2', 'gender': 'female'}]

with open('data.json','w',encoding='utf-8') as file:
    file.write(json.dumps(data,indent=2,ensure_ascii=False))