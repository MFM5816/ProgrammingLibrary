import time
from threading import Thread

def timer(n):
    while True:
        print(time.ctime().split()[3])
        time.sleep(n)

t = Thread(target=timer,args=(1,))
t.start()
t.join()

















