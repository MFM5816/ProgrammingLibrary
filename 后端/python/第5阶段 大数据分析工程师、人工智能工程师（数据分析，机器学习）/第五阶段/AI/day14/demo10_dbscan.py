"""
demo10_dbscan.py   DBSCAN聚类
"""
import sklearn.cluster as sc
import numpy as np
import matplotlib.pyplot as mp
import sklearn.metrics as sm

# 读取样本
x = np.loadtxt(
	'../ml_data/perf.txt', delimiter=',')

# 自定义一组半径，使用轮廓系数得到最优半径
rs = np.linspace(0.3, 1.2, 10)
models, scores = np.array([]), np.array([])
for r in rs:
	model = sc.DBSCAN(eps=r, min_samples=5)
	model.fit(x)
	pred_y = model.labels_
	score = sm.silhouette_score(x, pred_y, 
		sample_size=len(x), metric='euclidean')
	models = np.append(models, model)
	scores = np.append(scores, score)
# 最优模型...
best_ind = scores.argmax()
print(rs[best_ind])
print(scores[best_ind])
best_model = models[best_ind]
# 只拿到核心样本
labels = best_model.labels_
core_indices = best_model.core_sample_indices_
# 拿到孤立样本
offset_mask = labels == -1

# 绘制图像
mp.figure('DBSCAN', facecolor='lightgray')
mp.title('DBSCAN', fontsize=16)
mp.scatter(x[:,0][offset_mask], 
		   x[:,1][offset_mask], 
		   color='gray', marker='D', alpha=0.5,
	label='Offset Samples', s=100)
mp.scatter(x[:,0][core_indices], 
		   x[:,1][core_indices], 
		   c=labels[core_indices], cmap='jet',
	label='Core Samples', s=80)
mp.legend()
mp.show()