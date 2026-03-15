"""
demo07_poly.py  多项式回归
"""
import numpy as np
import sklearn.linear_model as lm
import matplotlib.pyplot as mp
import sklearn.metrics as sm
import sklearn.preprocessing as sp
import sklearn.pipeline as pl

x, y = np.loadtxt('../ml_data/single.txt', 
	delimiter=',', unpack=True)

# 基于数据管线，实现多项式回归模型训练
# 1.扩展特征 2. 把扩展之后的样本交给线性回归模型
model = pl.make_pipeline(
	sp.PolynomialFeatures(7), 
	lm.LinearRegression())  
model.fit(x.reshape(-1, 1), y)
# 画出多项式曲线
px = np.linspace(x.min(), x.max(), 500)
py = model.predict(px.reshape(-1, 1))

# 绘制这些点
mp.figure('Linear Regression', facecolor='lightgray')
mp.title('Linear Regression', fontsize=18)
mp.grid(linestyle=':')
mp.scatter(x, y, s=80, color='dodgerblue',
	label='Sample Points')
mp.plot(px, py, color='orangered', 
	label='Regression Line')
mp.legend()
mp.show()

