"""
demo07_nb.py  朴素贝叶斯
"""
import numpy as np
import matplotlib.pyplot as mp
import sklearn.naive_bayes as nb

# 整理样本
data = np.loadtxt(
	'../ml_data/multiple1.txt', delimiter=',')
x = data[:, :2]
y = data[:, -1]
print(x.shape, y.shape)

# 训练模型
model = nb.GaussianNB()
model.fit(x, y)

# 画图
mp.figure('Naive Bayes Classification', facecolor='lightgray')
mp.title('Naive Bayes Classification', fontsize=16)
# 绘制分类边界线
n = 500
l, r = x[:,0].min()-1, x[:,0].max()+1
b, t = x[:,1].min()-1, x[:,1].max()+1
grid_x, grid_y = np.meshgrid(np.linspace(l, r, n), 
	        				 np.linspace(b, t, n))
# 根据业务，模拟预测
mesh_x = np.column_stack(
	(grid_x.ravel(), grid_y.ravel()))
grid_z = model.predict(mesh_x)
# 把grid_z 变维：(500,500)
grid_z = grid_z.reshape(grid_x.shape)

mp.pcolormesh(grid_x, grid_y, grid_z, cmap='gray')
mp.scatter(x[:,0], x[:,1], s=80, 
	c=y, cmap='brg_r', label='Samples')
mp.legend()
mp.show()




