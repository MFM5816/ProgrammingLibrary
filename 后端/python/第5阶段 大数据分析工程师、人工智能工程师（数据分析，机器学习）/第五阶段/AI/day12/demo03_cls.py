"""
demo03_cls.py  简单分类
"""
import numpy as np
import matplotlib.pyplot as mp
x = np.array([ [3, 1],
		       [2, 5],
		       [1, 8],
		       [6, 4],
		       [5, 2],
		       [3, 5],
		       [4, 7],
		       [4, -1]])
y = np.array([0, 1, 1, 0, 0, 1, 1, 0])

# 画图
mp.figure('Simple Classification', facecolor='lightgray')
mp.title('Simple Classification', fontsize=16)
# 绘制分类边界线
n = 500
l, r = x[:,0].min()-1, x[:,0].max()+1
b, t = x[:,1].min()-1, x[:,1].max()+1
grid_x, grid_y = np.meshgrid(np.linspace(l, r, n), 
	        				 np.linspace(b, t, n))
# 根据业务，模拟预测
grid_z = np.piecewise(grid_x, 
			 [grid_x>grid_y, grid_x<=grid_y],
			 [0, 1])
mp.pcolormesh(grid_x, grid_y, grid_z, cmap='gray')
mp.scatter(x[:,0], x[:,1], s=80, 
	c=y, cmap='brg_r', label='Samples')
mp.legend()
mp.show()




