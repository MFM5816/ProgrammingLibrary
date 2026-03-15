"""
demo06_ridge.py  岭回归
"""
import numpy as np
import sklearn.linear_model as lm
import matplotlib.pyplot as mp

x, y = np.loadtxt('../ml_data/abnormal.txt', 
	delimiter=',', unpack=True)

# 训练线性回归模型
model = lm.LinearRegression()
model.fit(x.reshape(-1, 1), y)
pred_y = model.predict(x.reshape(-1, 1))

# 绘制这些点
mp.figure('Ridge Regression', facecolor='lightgray')
mp.title('Ridge Regression', fontsize=18)
mp.grid(linestyle=':')
mp.scatter(x, y, s=80, color='dodgerblue',
	label='Sample Points')
mp.plot(x, pred_y, color='orangered', 
	label='Regression Line')

# 基于岭回归，训练模型
model = lm.Ridge(
	100, fit_intercept=True, max_iter=10000)
model.fit(x.reshape(-1,1), y)
pred_y = model.predict(x.reshape(-1, 1))
mp.plot(x, pred_y, color='blue', 
	label='Ridge Regression Line')



mp.legend()
mp.show()

