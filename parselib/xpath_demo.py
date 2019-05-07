#!/usr/bin/python3
# -*- coding:UTF-8-*-
'''
@File:xpath_demo.py
@Author: Yaochenglong
@Date :
@Desc:
'''

from lxml import etree
text='''
<div>
<ul>
<li class="item-0"><a href="link1.html">first</a></li>
<li class="item-1"><a href="link2.html">second</a></li>
<li class="item-inactive"><a href="link3.html">third</a></li>
<li class="item-1"><a href="link4.html">fourth</a></li>
<li class="item-0"><a href="link5.html">fifth</a>
</ul>
</div>
'''
#
# html = etree.HTML(text)
# result = etree.tostring(html)
# print(result.decode('utf8'))

############  获取所有节点
# html = etree.parse('test.html',etree.HTMLParser())
# result = html.xpath('//*')
# print(result)
##  获取所有li节点
# html = etree.parse('test.html',etree.HTMLParser())
# result = html.xpath('//li')
# print(result)

##  获取子节点
# html = etree.parse('test.html',etree.HTMLParser())
# result = html.xpath('//li/a')
# print(result)

###### 获取父节点

# html = etree.parse('test.html',etree.HTMLParser())
# result = html.xpath('//a[@href="link4.html"]/../@class')
# print(result)
# ### 获取父节点2
# html = etree.parse('test.html',etree.HTMLParser())
# result = html.xpath('//a[@href="link4.html"]/parent::*/@class')
# print(result)


#html = etree.parse('test.html',etree.HTMLParser())
##  属性匹配
# result = html.xpath('//li[@class="item-0"]')
# print(result)

##### 文本获取
# result = html.xpath('//li[@class="item-0"]//text()')
# print(result)


##  属性获取
# result = html.xpath('//li/a/@href')
# print(result)


## 属性多值匹配
# text = '''
# <li class="li li-first"><a href="link.html">first item</a></li>
# '''
# html = etree.HTML(text)
# result = html.xpath('//li[contains(@class,"li")]/a/text()')
# print(result)


## 多属性匹配
# text = '''
# <li class="li li-first" name="item"><a href="link.html">first item</a></li>
# '''
# html = etree.HTML(text)
# result = html.xpath('//li[contains(@class,"li") and @name="item"]/a/text()')
# print(result)

## 按序选择
# html = etree.HTML(text)
# result = html.xpath('//li[1]/a/text()')
# print(result)
# result = html.xpath('//li[last()]/a/text()')
# print(result)
# result = html.xpath('//li[position()<3]/a/text()')
# print(result)
# result = html.xpath('//li[last()-2]/a/text()')
# print(result)



##  节点抽选择
html = etree.HTML(text)
# 获取当前节点的所有父节点
# result = html.xpath('//li[1]/ancestor::*')
# print(result)

# 获取当前节点所有父节点中的div节点
# result = html.xpath('//li[1]/ancestor::div')
# print(result)

## 获取当前节点的所有属性
# result = html.xpath('//li[1]/attribute::*')
# print(result)

##
result = html.xpath('//li[1]/child::a[@href="link1.html"]')
print(result)

result = html.xpath('//li[1]/descendant::span')
print(result)







