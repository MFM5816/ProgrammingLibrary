"""
demo06_lbe.py  labelencoder标签编码
"""
import numpy as np
import sklearn.preprocessing as sp

samples = np.array(['bmw', 'audi', 'bmw', 
	'bz', 'toyota', 'ford', 'audi', 'redflag',
	'ford'])

lbe = sp.LabelEncoder()
r = lbe.fit_transform(samples)
print(r)

# 模拟预测：
r = [1, 1, 0, 0, 3, 3, 4, 5, 1]
r = lbe.inverse_transform(r)
print(r)

