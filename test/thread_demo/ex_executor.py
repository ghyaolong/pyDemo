#!/usr/bin/python3
# -*- coding:UTF-8-*-
'''
@File:ex_executor.py
@Author: Yaochenglong
@Date :
@Desc:
'''
import time,concurrent.futures
numbers  = list(range(1,11))

def count(n):
    for i in range(10000000):
        i += i
    return i*n

def worker(x):
    result = count(x)
    print(f'数字：{x}的计算结果是:{result}')

#顺序执行
def sequential_execution():
    start_time = time.process_time()
    for i in numbers:
        worker(i)
    end_time = time.process_time()
    print(f'花费时间：{end_time-start_time}秒')

# 线程池
def threading_execution():
    start_time = time.process_time()
    with concurrent.futures.ThreadPoolExecutor(max_workers = 5) as executor:
        for i in numbers:
            executor.submit(worker,i)
    end_time = time.process_time()
    print(f'线程池花费时间：{end_time - start_time}秒')


# 进程池
def process_execution():
    start_time = time.process_time()
    with concurrent.futures.ProcessPoolExecutor(max_workers = 5) as executor:
        for i in numbers:
            executor.submit(worker,i)
    end_time = time.process_time()
    print(f'线程池花费时间：{end_time - start_time}秒')

if __name__ == '__main__':
    #sequential_execution()
    threading_execution()
    #process_execution()



