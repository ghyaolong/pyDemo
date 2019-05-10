#!/usr/bin/python3
# -*- coding:UTF-8-*-
'''
@File:ex_mp.py
@Author: Yaochenglong
@Date :
@Desc: 适合计算密集型
'''
import time,multiprocessing

def func(n):
    print(f'{multiprocessing.current_process().name}开始于:{time.ctime()}')
    time.sleep(n)
    print(f'{multiprocessing.current_process().name}结束于:{time.ctime()}')

def main():
    print(f'主函数starttime:{time.ctime()}')
    processes = []
    p1 = multiprocessing.Process(target=func,args=(4,))
    processes.append(p1)

    p2 = multiprocessing.Process(target=func, args=(4,))
    processes.append(p2)

    for p in processes:
        p.start()

    for p in processes:
        p.join()
    print(f'主函数endtime:{time.ctime()}')

if __name__ == '__main__':
    main()


