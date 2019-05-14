#!/usr/bin/python3
# -*- coding:UTF-8-*-
'''
@File:
@Author: Yaochenglong
@Email: 289911401@qq.com
@Date :
@Desc:
'''
from lxml import etree

html = etree.parse('github.html',etree.HTMLParser)
result = etree.tostring(html)

