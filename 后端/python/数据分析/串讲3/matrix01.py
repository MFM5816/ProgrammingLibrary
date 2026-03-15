import numpy as np

# 向量化 Vectorize
def myfunc(a, b):
    'Return a-b if a>b, otherwise return a+b'
    if a>b:
        return a-b
    else:
        return a+b

a = [1, 2, 3, 4]
b = 2
func = np.vectorize(myfunc)
print(func(a, b))

# frompyfunc函数
fun = np.frompyfunc(myfunc, 2, 1)
# 2 为myfunc中的参数个数
# 1 为myfunc中的返回值的个数
print(fun(a, b))