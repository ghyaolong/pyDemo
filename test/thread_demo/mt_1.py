#!/usr/bin/python3
# -*- coding:UTF-8-*-
'''
@File:mt_1.py
@Author: Yaochenglong
@Date :
@Desc:_thread 实现多线程
'''

import time
import _thread

def worker(n):
    print(f'函数执行开始于:{time.ctime()}')
    time.sleep(n)
    print(f'函数执行结束于:{time.ctime()}')

def main():
    print(f'【主函数执行开始于:{time.ctime()}】')
    _thread.start_new_thread(worker,(4,))
    _thread.start_new_thread(worker,(2,))
    time.sleep(4)
    print(f'【主函数执行结束于:{time.ctime()}】')

if __name__ == '__main__':
    main()
