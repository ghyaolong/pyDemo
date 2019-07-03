#!/usr/bin/python3
# -*- coding:UTF-8-*-
'''
@Desc: 正则表达式
@Author: Yaochenglong
@Email: 289911401@qq.com
@Date : 

'''
import re
content = 'adfadf'

result = re.match('abc',content)

print(result.group())
print(result.group(1))
print(result.span())

'''
search()

findall()

sub()

compile()

'''