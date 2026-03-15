import time

def get_time(func):
    def get_result():
        start = time.time()
        func()
        end = time.time()
        print('执行时间%f秒' % (end-start))

    return get_result

@get_time
def test():
    print('我是test函数')
    time.sleep(1)

get_time(test())


















