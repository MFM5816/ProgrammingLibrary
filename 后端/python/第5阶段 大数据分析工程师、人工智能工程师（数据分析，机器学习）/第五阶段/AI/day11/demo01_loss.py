"""
demo07_loss.py 损失函数
"""
import numpy as np
import matplotlib.pyplot as mp
from mpl_toolkits.mplot3d import axes3d

n = 500
grid_w0, grid_w1 = np.meshgrid(
	np.linspace(0, 9, n), np.linspace(0, 3.5, n))

# 根据每个网格点坐标，通过某个公式计算z高度坐标
grid_loss = np.zeros_like(grid_w0)
x = np.array([0.5, 0.6, 0.8, 1.1, 1.4])
y = np.array([5.0, 5.5, 6.0, 6.8, 7.0])
for px, py in zip(x, y):
	grid_loss += (grid_w0 + grid_w1*px - py)**2 / 2

# 绘制
mp.figure('Loss', facecolor='lightgray')
mp.title('Loss', fontsize=18)
ax3d = mp.gca(projection='3d')
ax3d.set_xlabel('w0')
ax3d.set_ylabel('w1')
ax3d.set_zlabel('loss')
ax3d.plot_surface(grid_w0, grid_w1, grid_loss, 
	rstride=30, cstride=30, cmap='jet')
mp.tight_layout()
mp.show()

