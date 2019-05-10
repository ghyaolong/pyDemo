#!/usr/bin/python3
# -*- coding:UTF-8-*-
'''
@File:mt_4.py
@Author: Yaochenglong
@Date :
@Desc: 同步原语：锁
'''
import threading
import time,random

eggs = []

lock = threading.Lock()
def put_egg(n,lst):
    with lock:
        for i in range(1,n+1):
            time.sleep(random.randint(0,2))
            lst.append(i)


def main():
    threads=[]
    for i in range(3):
        t = threading.Thread(target=put_egg,args=(5,eggs))
        threads.append(t)

    for t in threads:
        t.start()
    for t in threads:
        t.join()
    print(eggs)
if __name__ == '__main__':
    main()
