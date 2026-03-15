"""
demo02_mms.py   范围缩放
"""
import sklearn.preprocessing as sp
import numpy as np

samples = np.array([[17, 80, 4000], 
				    [20, 90, 4500],
				    [23, 95, 5500]])

mms = sp.MinMaxScaler(feature_range=(0, 1))
r = mms.fit_transform(samples)
print(r)

# 遍历每一列
samples_ = []
for col in samples.T:
	col_min = col.min()
	col_max = col.max()
	A = np.array([[col_min, 1], [col_max, 1]])
	B = np.array([0, 1])
	x = np.linalg.lstsq(A, B)[0]
	col_ = x[0]*col + x[1]
	samples_.append(col_)
print(np.array(samples_).T)