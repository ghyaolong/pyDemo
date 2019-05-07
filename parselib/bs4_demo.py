#!/usr/bin/python3
# -*- coding:UTF-8-*-
'''
@File:
@Author: Yaochenglong
@Email: 289911401@qq.com
@Date :
@Desc:Beautiful_soup库的使用
'''
from bs4 import BeautifulSoup
# soup = BeautifulSoup('<p>Hello</p>','lxml')
# print(soup.string)

##  beautifulsoup的基本使用
html='''
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>The Dormouse's story</title>
</head>
<body>

	<p class="story" >Once upon a time there were three little sisters
	;and their names were
  <a href="http://example.com/elsie" id="link1">Elsie</a>
  and
  <a href="http://example.com/sister" id="link3">Lacie</a>
  and
  <a href="http://example.com/sister" id="link3">Tillie</a>;
  and the lived at the bottle of a well.<p>
  	<p class="story">...</p>
'''
soup = BeautifulSoup(html,"lxml")



# #把要解析的字符串以标准的缩进格式输出
# print(soup.prettify())
# #输出HTML 中title 节点的文本内容
# print(soup.title.string)



## 节点选择器   (如果单个节点结构层次非常清晰，可以选用这种方式来解析。)  ##

### 1 .选择元素
# print(soup.title)
# print(type(soup.title))
# print(soup.title.string)
# print(soup.head)
# print(soup.p)
#
# ### 2.提取信息
#
# #2.1调用string获取文本的值
# #2.2调用name获取节点的名称
# print(soup.title.name)
# #2.3获取属性
# print('-'*100)
# print(soup.p.attrs)
# print(soup.p.attrs['name'])
# #或
# print(soup.p['name'])
# print(soup.p['class'])
#
#
# ### 3.嵌套选择
# print('-'*100)
# print(soup.head.title)
# print(type(soup.head.title))
# print(soup.head.title.string)

### 4.关联选择
#4.1子节点和子孙节点
#print(soup.p.contents)
#print(soup.p.children)
# print(type(soup.p.children))
# for i,child in enumerate(soup.p.descendants):
#     print(i,child)

#4.2父节点和祖先节点(如果要获取某个节点元素的父节点，可以调用parent 属性,如果想获取所有的祖先节点，可以调用parents 属性：)
#print(soup.a.parent)
#print(list(enumerate(soup.a.parents)))

#4.3 兄弟节点
#print('Next Sibling',soup.a.next_sibling)
#print('Prev Sibling',soup.a.previous_sibling)
#print('Next Siblings',list(enumerate(soup.a.next_siblings)))
#print('Prev Siblings',soup.a.previous_siblings)

#4.4提取信息
#print('Next Sibling',soup.a.next_sibling.string)
#print('parents')
#print(type(soup.a.parents))
#print(list(soup.a.parents)[0])
# 获取属性
#print(list(soup.a.parents)[0].attrs['class'])
#print('Next Siblings',list(enumerate(soup.a.next_siblings)))
#print('Prev Siblings',soup.a.previous_siblings)



##############               6方法选择器   ##############
#6.1    find_all()         查询所有符合条件的元素。给它传入一些属性或文本，就可以得到符合条件的元素
# 根据节点名称来查询元素
html ='''
<div class="panel">
<div class="panel-heading">
<h4>Hello</h4>
</div>
<div class="panel-body">
<ul class="list" id="list-1" name="elements">
<li class="element">Foo</li>
<li class="element">Bar</li>
<li class="element">Jary</li>
</ul>
<ul class="list list-small" id="list-2">
<li class="element">Foo</li>
<li class="element">Bar</li>
</ul>
</div>
</div>
'''
soup = BeautifulSoup(html,'lxml')
#print(soup.find_all(name='ul'))
# #print(type(soup.find_all(name='ul')[0]))
# for ul in soup.find_all(name='ul'):
#     print(ul.find_all(name='li'))
#     for li in ul.find_all(name='li'):
#         print(li.string)

## attrs  传入一些属性来查询
print(soup.find_all(attrs={'id':'list-1'}))
print(soup.find_all(attrs={'name':'elements'}))







