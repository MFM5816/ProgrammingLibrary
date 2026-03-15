#!-*- coding=utf-8 -*-
'''解决死锁的代码'''
from threading import Thread,Lock
import time

lock1 = Lock()
lock2 = Lock()

# 线程1事件函数
def f1():
    # lock1加锁
    lock1.acquire()
    # 第1行打印
    print('线程1锁住了lock1')
    time.sleep(0.1)

    while True:
        # result为True或者False
        result = lock2.acquire(timeout=1)
        if result:
            # 第4行输出
            print('线程1锁住了lock2')
            lock2.release()
            break

        else:
            lock1.release()

# 线程2事件函数
def f2():
    # lock2加锁
    lock2.acquire()
    # 第2行打印
    print('线程2锁住了lock2')
    time.sleep(0.1)
    lock1.acquire()
    # 第3行打印
    print('线程2锁住了lock1')
    lock1.release()

    lock2.release()

t1 = Thread(target=f1)
t2 = Thread(target=f2)
t1.start()
t2.start()
t1.join()
t2.join()




























