#!/usr/bin/python3
# -*- coding:UTF-8-*-
'''
@File:ex_queue.py
@Author: Yaochenglong
@Date :
@Desc:
'''
import queue,threading,time,random


def producer(data_queue):
    for i in range(5):
        time.sleep(0.5)
        item = random.randint(1,100)
        data_queue.put(item)
        print(f'{threading.current_thread().name}在队列中放入数据{item}')


def consumer(data_queue):
    while True:
        try:
            item = data_queue.get(timeout=3)
            print(f'{threading.current_thread().name}从队列中移除了{item}')
        except queue.Empty as e:
            print(e)
            break
        else:
            data_queue.task_done()


def main():
    q = queue.Queue()

    threads=[]
    p = threading.Thread(target=producer,args=(q,))
    p.start()

    for i in range(2):
        p = threading.Thread(target=consumer,args=(q,))
        threads.append(p)

    for t in threads:
        t.start()

    for t in threads:
        t.join()

    q.join()

if __name__ == '__main__':
    main()
