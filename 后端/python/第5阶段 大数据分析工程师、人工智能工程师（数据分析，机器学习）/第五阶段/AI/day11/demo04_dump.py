"""
demo04_dump.py  保存模型
"""
import numpy as np
import sklearn.linear_model as lm
import matplotlib.pyplot as mp
import pickle

x, y = np.loadtxt('../ml_data/single.txt', 
	delimiter=',', unpack=True)

# 训练线性回归模型
model = lm.LinearRegression()
model.fit(x.reshape(-1, 1), y)
pred_y = model.predict(x.reshape(-1, 1))

# 评估模型的性能
import sklearn.metrics as sm
print(sm.mean_absolute_error(y, pred_y))
print(sm.mean_squared_error(y, pred_y))
print(sm.median_absolute_error(y, pred_y))
print(sm.r2_score(y, pred_y))

# 保存模型
with open('linear.pkl', 'wb') as f:
	pickle.dump(model, f)
print('dump success.')