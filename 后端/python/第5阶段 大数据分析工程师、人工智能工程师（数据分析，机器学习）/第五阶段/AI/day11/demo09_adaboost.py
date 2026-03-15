"""
demo09_adaboost.py   正向激励
"""
import numpy as np
import sklearn.datasets as sd
import sklearn.tree as st
import sklearn.utils as su
import sklearn.metrics as sm

# 加载数据
boston = sd.load_boston()
print(boston.data.shape)
print(boston.target.shape)
print(boston.feature_names)
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

# 基于正向激励，训练模型
import sklearn.ensemble as se
model = se.AdaBoostRegressor(
	model, n_estimators=400, random_state=7)
model.fit(train_x, train_y)
pred_test_y = model.predict(test_x)
print(sm.r2_score(test_y, pred_test_y))
print(sm.mean_absolute_error(test_y, pred_test_y))

# 岭回归
import sklearn.linear_model as lm
model = lm.Ridge(
	0, fit_intercept=True, max_iter=10000)
model.fit(train_x, train_y)
pred_test_y = model.predict(test_x)
print(sm.r2_score(test_y, pred_test_y))
print(sm.mean_absolute_error(test_y, pred_test_y))



