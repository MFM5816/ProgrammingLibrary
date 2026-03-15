import time

def get_world(n):
    # 1.终止递归的条件
    if n == 0:
        return
    # 2.具体做的事情
    print('hello world')
    time.sleep(1)
    # 3.返回函数
    return get_world(n-1)

if __name__ == '__main__':
    get_world(3)















