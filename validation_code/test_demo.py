#!/usr/bin/python3
# -*- coding:UTF-8-*-
'''
@File:
@Author: Yaochenglong
@Email: 289911401@qq.com
@Date :
@Desc:
'''
import tesserocr
from PIL import Image
image = Image.open('test.png')
# 将图片进行灰化和二值化处理
iamge = image.convert('L')
threshold = 127
table = []
for i in range(256):
    if i < threshold:
        table.append(0)
    else:
        table.append(1)
image = image.point(table,'1')
#iamge.show()
result = tesserocr.image_to_text(image)
# print(tesserocr.file_to_text('image.png')) 此种方法没有上一面一种效果好
print(result)
