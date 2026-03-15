"""
demo01_fi.py   特征重要性
"""
import numpy as np
import sklearn.datasets as sd
import sklearn.tree as st
import sklearn.utils as su
import sklearn.metrics as sm
import matplotlib.pyplot as mp

# 加载数据
boston = sd.load_boston()
print(boston.data.shape)
print(boston.target.shape)
print(boston.feature_names)
header = boston.feature_names
# 打乱数据集，划分测试集 与 训练集
x, y = su.shuffle(
	boston.data, boston.target, random_state=7)
train_size = int(len(x) * 0.8)
train_x, test_x, train_y, test_y = \
	x[:train_size], x[train_size:], \
	y[:train_size], y[train_size:]

# 使用训练集训练， 使用测试集测试
model = st.DecisionTreeRegressor(max_depth=4)
model.fit(train_x, train_y)
# 
pred_test_y = model.predict(test_x)
print(sm.r2_score(test_y, pred_test_y))
print(sm.mean_absolute_error(test_y, pred_test_y))
# 输出特征重要性
dt_fi = model.feature_importances_
print(dt_fi)
mp.figure('Feature Importance', facecolor='lightgray')
mp.subplot(211)
mp.title('DT Feature Importance', fontsize=16)
mp.grid(linestyle=':', axis='y')
x = np.arange(dt_fi.size)
sorted_indices = dt_fi.argsort()[::-1]
mp.xticks(x, header[sorted_indices])
mp.bar(x, dt_fi[sorted_indices], 0.8, 
	color='dodgerblue', label='DT Feature Importances')
mp.legend()
mp.tight_layout()
# 基于正向激励，训练模型
import sklearn.ensemble as se
model = se.AdaBoostRegressor(
	model, n_estimators=400, random_state=7)
model.fit(train_x, train_y)
pred_test_y = model.predict(test_x)
print(sm.r2_score(test_y, pred_test_y))
print(sm.mean_absolute_error(test_y, pred_test_y))
ada_fi = model.feature_importances_

mp.subplot(212)
mp.title('AdaBoost Feature Importance', fontsize=16)
mp.grid(linestyle=':', axis='y')
sorted_indices = ada_fi.argsort()[::-1]
mp.xticks(x, header[sorted_indices])
mp.bar(x, ada_fi[sorted_indices], 0.8, 
	color='orangered', label='AdaBoost Feature Importances')
mp.legend()
mp.tight_layout()
mp.show()

