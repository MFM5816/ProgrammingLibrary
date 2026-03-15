"""
demo05_ohe.py  独热编码
"""
import numpy as np
import sklearn.preprocessing as sp

samples = np.array([[1, 3, 2],
					[7, 5, 4],
					[1, 8, 6],
					[7, 3, 9]])
ohe = sp.OneHotEncoder(sparse=False)
r = ohe.fit_transform(samples)
print(r)