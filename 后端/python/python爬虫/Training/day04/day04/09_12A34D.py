from threading import Thread,Lock
import string

# 1. 开始执行的线程一定是 f1
# 2. f1彻底执行1次,f2再彻底执行1次,依次循环
# 3. 尝试用锁来实现?

# 获取对方锁来实现逻辑
# 输出 12 34 56 78
def f1():
    for i in range(1,52,2):
        lock2.acquire()
        print(i,end='')
        print(i+1,end='')
        lock1.release()

# 输出 A B C D E F G
def f2():
    chars = string.ascii_uppercase
    for j in chars:
        lock1.acquire()
        print(j)
        lock2.release()


lock1 = Lock()
lock2 = Lock()

# 保证让f1先执行
lock1.acquire()

t1 = Thread(target=f1)
t2 = Thread(target=f2)

t1.start()
t2.start()

t1.join()
t2.join()













