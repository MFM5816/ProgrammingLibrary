"""
demo09_silhouette_score.py   轮廓系数
"""
import sklearn.cluster as sc
import numpy as np
import matplotlib.pyplot as mp
import sklearn.metrics as sm

# 读取样本
x = np.loadtxt(
	'../ml_data/multiple3.txt', delimiter=',')

# 划分4个聚类
model = sc.KMeans(n_clusters=4)
model.fit(x)
# pred_y = model.predict(x)
pred_y = model.labels_
print(model.cluster_centers_)
# 输出轮廓系数
print(sm.silhouette_score(
	x, pred_y, sample_size=len(x), metric='euclidean'))

# 绘制图像
mp.figure('KMeans', facecolor='lightgray')
mp.title('KMeans', fontsize=16)
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

mp.scatter(x[:,0], x[:,1], c=pred_y, cmap='brg_r',
	label='Samples', s=80)
centers = model.cluster_centers_
mp.scatter(centers[:,0], centers[:,1], s=1000,
	marker='+', color='yellow', label='centers')

mp.legend()
mp.show()