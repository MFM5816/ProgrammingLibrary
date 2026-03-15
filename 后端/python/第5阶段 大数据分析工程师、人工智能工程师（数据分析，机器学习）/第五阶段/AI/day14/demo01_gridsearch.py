"""
demo01_gridsearch.py  网格搜索
"""
import numpy as np
import matplotlib.pyplot as mp
import sklearn.svm as svm
import sklearn.model_selection as ms

# 整理样本
data = np.loadtxt(
	'../ml_data/multiple2.txt', delimiter=',')
x = data[:, :2]
y = data[:, -1]
print(x.shape, y.shape)

# 训练模型
train_x, test_x, train_y, test_y = \
	ms.train_test_split(
		x, y, test_size=0.25, random_state=7)

# 使用网格搜索 找到最优模型
model = svm.SVC()
params = [
    {'kernel':['linear'], 'C':[1, 10, 100, 1000]},
    {'kernel':['poly'], 'C':[1], 'degree':[2, 3]}, 
    {'kernel':['rbf'], 'C':[1,10,100,1000], 
     'gamma':[1, 0.1, 0.01, 0.001]}]
model = ms.GridSearchCV(model, params, cv=5)
model.fit(train_x, train_y)
# 获取模型训练后的最优超参数
print(model.best_params_)
print(model.best_score_)
print(model.best_estimator_)
# 获取模型训练过程中，每一组超参数的测试得分：
for p, s in zip(model.cv_results_['params'], 
			    model.cv_results_['mean_test_score']):
	print(p, '->', s)

# 测试
pred_test_y = model.predict(test_x)
import sklearn.metrics as sm
print(sm.classification_report(test_y, pred_test_y))


# 画图
mp.figure('SVM Classification', facecolor='lightgray')
mp.title('SVM Classification', fontsize=16)
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
mp.scatter(test_x[:,0], test_x[:,1], s=80, 
	c=test_y, cmap='brg_r', label='Samples')
mp.legend()
mp.show()




