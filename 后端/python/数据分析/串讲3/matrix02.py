import numpy as np
a = np.arange(12).reshape([3, 4])
b = np.arange(12).reshape([4, 3])
# wrong
print(a)
print(b)
print("multi\n", a * b.T,type(a))
print("matrix multi\n", np.matmul(a, b))
print(np.dot(a, b))

x = np.matrix([[1, 3, 5], [2, 4, 6]])
y = np.matrix([[7, 9, 11], [8, 10, 12]])
print(x, x.shape,type(x), "# x.shape")
print(y, y.shape, "# y.shape")

print(x * y.T, "# x * y.T")
print(np.matmul(x, y.T), "# np.matmul(x, y.T)")
print(np.multiply(x, y), "# matrix multiply")

w = np.array([1, 2, 4])
print("ndarray", w.shape,w.T.shape)
v = np.matrix([1, 2, 4])
print("matrix ", v.shape,v.T.shape)

x = np.matrix([[1, 3, 5], [2, 4, 6]])
print(x, "# x")
y = np.matrix("1,2,3;4,5,6;7,8,9")
print(y, "# y")


x = np.array([[1, 3, 5], [2, 4, 6]])
y = np.array([[7, 9, 11], [8, 10, 12]])
print(x.T)
print(y.T)

e = np.mat('1 2 6; 3 5 7; 4 8 9')
print(e)
print(e.I)
print(e * e.I)
a = np.array([
    [1, 2, 6],
    [3, 5, 7],
    [4, 8, 9]])
# 点乘法求ndarray的点乘结果，与矩阵的乘法运算结果相同
k = a.dot(a)
print('k',k)
# linalg模块中的inv方法可以求取a的逆矩阵
l = np.linalg.inv(a)
print(l)





