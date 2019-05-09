#!/usr/bin/python3
# -*- coding:UTF-8-*-
'''
@File:test_demo.py
@Author: Yaochenglong
@Date :
@Desc:
'''
import json

########### json.dumps()用于将dict类型的数据转成str，因为如果直接将dict类型的数据写入json文件中会发生报错，因此在将数据写入时需要用到该函数

name_emb={'a':'111','b':'222','c':'333'}
# print(name_emb)
# print(type(name_emb))
# jsObj = json.dumps(name_emb)
# print(jsObj)
# print(type(jsObj))

# emb_filename =('emb_json.json')
# with open(emb_filename,'w') as f:
#     str = json.dumps(name_emb)
#     f.write(str)
#     f.close()

###  json.dump()用于将dict类型的数据转成str，并写入到json文件中  下面两种方法都可以将数据写入json文件
#solution 1
jsObj = json.dumps(name_emb)
with open('em_json.json','w') as f:
    f.write(jsObj)
    f.close()

#sulution 2
json.dump(name_emb,open('emb_json.json','w'))



#########################################################################################################


########   json.loads()用于将str类型的数据转成dict
# name_emb = {"a": "111", "b": "222", "c": "333"}
# jsDumps = json.dumps(name_emb)
# jsLoads = json.loads(jsDumps)
# print(name_emb,type(name_emb))
# print(jsDumps,type(jsDumps))
# print(jsLoads,type(jsLoads))

## json.load用于从json文件中读取数据
jsObj = json.load(open('emb_json.json'))
print(jsObj)
print(type(jsObj))
for key in jsObj.keys():
    print(key,jsObj.get(key))








