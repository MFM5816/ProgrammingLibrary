'''产生死锁的代码'''
from threading import Thread,Lock
import time

lock1 = Lock()
lock2 = Lock()

# 线程1事件函数
def f1():
    # lock1加锁
    lock1.acquire()

    print('线程1锁住了lock1')
    time.sleep(0.1)
    lock2.acquire()
    print('线程1锁住了lock2')
    lock2.release()

    lock1.release()

# 线程2事件函数
def f2():
    # lock2加锁
    lock2.acquire()

    print('线程2锁住了lock2')
    time.sleep(0.1)
    lock1.acquire()
    print('线程2锁住了lock1')
    lock1.release()

    lock2.release()

t1 = Thread(target=f1)
t2 = Thread(target=f2)
t1.start()
t2.start()
t1.join()
t2.join()




























