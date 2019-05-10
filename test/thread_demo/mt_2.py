#!/usr/bin/python3
# -*- coding:UTF-8-*-
'''
@File:mt_2.py
@Author: Yaochenglong
@Date :
@Desc:threading 实现多线程
'''

import time
import threading

def worker(n):
    print(f'{threading.current_thread().name}函数执行开始于:{time.ctime()}')
    time.sleep(n)
    print(f'{threading.current_thread().name}函数执行结束于:{time.ctime()}')

def main():
    print(f'【主函数执行开始于:{time.ctime()}】')
    # _thread.start_new_thread(worker,(4,))
    # _thread.start_new_thread(worker,(2,))
    threads=[]
    t1 = threading.Thread(target=worker,args=(4,))
    threads.append(t1)
    t2 = threading.Thread(target=worker, args=(2,))
    threads.append(t2)

    for t in threads:
        t.start()

    for t in threads:
        t.join()
    print(f'【主函数执行结束于:{time.ctime()}】')

if __name__ == '__main__':
    main()
