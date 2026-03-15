"""
demo05_load.py  加载模型
"""
import numpy as np
import sklearn.linear_model as lm
import matplotlib.pyplot as mp
import pickle

x, y = np.loadtxt('../ml_data/single.txt', 
	delimiter=',', unpack=True)

# 加载线性回归模型
with open('linear.pkl', 'rb') as f:
	model = pickle.load(f)

test_x = [[x.min()], [x.max()]]
pred_test_y = model.predict(test_x)

# 绘制这些点
mp.figure('Linear Regression', facecolor='lightgray')
mp.title('Linear Regression', fontsize=18)
mp.grid(linestyle=':')
mp.scatter(x, y, s=80, color='dodgerblue',
	label='Sample Points')
mp.plot(test_x, pred_test_y, color='orangered', 
	label='Regression Line')
mp.legend()
mp.show()

