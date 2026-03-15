"""
demo03_linearRegression.py  线性回归
"""
import numpy as np
import sklearn.linear_model as lm
import matplotlib.pyplot as mp

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


# 绘制这些点
mp.figure('Linear Regression', facecolor='lightgray')
mp.title('Linear Regression', fontsize=18)
mp.grid(linestyle=':')
mp.scatter(x, y, s=80, color='dodgerblue',
	label='Sample Points')
mp.plot(x, pred_y, color='orangered', 
	label='Regression Line')
mp.legend()
mp.show()

