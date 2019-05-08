#!/usr/bin/python3
# -*- coding:UTF-8-*-
'''
@File:pyquery_demo.py
@Author: Yaochenglong
@Date :
@Desc:
'''
from pyquery import PyQuery as pq
import requests
#  2 初始化
## 2.1字符串初始化
html='''
<div id ="container" name="abc">
<ul class="list">
<li class="item-1">first item</li>
<li class="item-1"><a href="link2.html">second item</a></li>
<li class="item-0 active"><a href="link3.html"><span class="bold">thrid item</span></a></li>
<li class="item-1 active"><a href="link4.html">fourth item</a></li>
<li class="item-0"><a href="link5.html">fifth item</a></li>
</ul>
</div>
'''
doc = pq(html)
# doc = pq(html)
# #print(doc('li'))
#
# ## 2.2url初始化
# doc = pq(url='http://cuiqingcai.com')
# print(doc('title'))
#
# doc = pq(requests.get('https://cuiqingcai.com').text)
# print(doc('title'))
#
# ## 2.3 文件初始化
# doc = pq(filename='test.html')
# print(doc('li'))

## 3.基本的CSS选择器
# doc = pq(html)
# print(doc('#container .list li'))
# print(type(doc('#container .list li')))

## 4.查找节点

items = doc('.list')
# print(items)
# print(type(items))
# lis = items.find('li')
# print(type(lis))
# print(lis)
#子节点
# lis = items.children('.active')
# print(lis)
#父节点
#

#兄弟节点
# li = doc('.list .item-0.active')
# print(li.siblings('.active'))

#遍历
# li = doc('.list .item-0.active')
# print(li)
# print(str(li))

# li = doc('li').items()
# print(type(li))
# for l in li:
#     print(l,type(l))

#6获取信息，调用哦attr()方法来获取属性
# a = doc('.item-0.active a')
# print(a,type(a))
# print(a.attr('href'))
#获取文本
# a = doc('.item-0.active a')
# print(a.text())
# a = doc('.item-0.active')
# print(a.html())


#7节点操作 ，比如为某个节点添加一个class ，移除某个节点等，这些操作有时候会为提取信息带来极大的便利。

## addClass和removeClass
li = doc('.item-0.active')
# print(li)
# #li.remove_class('active')
# li.removeClass('active')
# print(li)
# li.addClass('active')
# print(li)

## attr、 text和html
#print(li)
# li.attr('name','link')
# print(li)
# print(li.text('changed item'))
# print(li)
#print(li.html('<span>changed item</span>'))

## remove
# html='''
# <div class="warp">
# 		Hello,World
# 	<p>this is a paragraph.</p>
# </div>
# '''
# doc = pq(html)
# warp = doc('.warp')
# print(warp.find('p').remove().text())


### 8 .伪类选择器

li = doc('li:first-child')
print(li)
li = doc('li:last-child')
print(li)

li = doc('li:nth-child(2)')
print(li)

li = doc('li:contains(2)')
print(li)

















