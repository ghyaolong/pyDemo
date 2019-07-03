#!/usr/bin/python3
# -*- coding:UTF-8-*-
'''
@Desc:
@Author: Yaochenglong
@Email: 289911401@qq.com
@Date :
'''

from bs4 import BeautifulSoup

# 使用CSS选择器

html='''
<div class="panel">
<div class="panel-heading">
<h4>Hello</h4>
</div>
<div class="panel-body">
<ul class="list" id="list-1">
<li class="element">Foo</li>
<li class="element">Bar</li>
<li class="element">Jay</li>
</ul>
<ul class="list list-small" id="list-2">
<li class="element">Foo</li>
<li class="element">Bar</li>
</ul>
</div>
</div>
'''

soup = BeautifulSoup(html,'lxml')
print(soup.select('.panel .panel-heading'))
print('-'*50)

# 嵌套是选择
for u in soup.select('ul'):
    print(u.select('li'))



# 获取属性
for ul in soup.select('ul'):
    print(ul['id'])
    #或
    print(ul.attrs['id'])


# 获取文本
for li in soup.select('li'):
    print('Get Text:',li.get_text())
    #或
    print('String:',li.string)

