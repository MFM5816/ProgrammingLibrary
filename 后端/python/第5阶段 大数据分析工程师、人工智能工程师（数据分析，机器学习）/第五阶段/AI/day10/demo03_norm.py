"""
demo03_norm.py  归一化
"""
import numpy as np
import sklearn.preprocessing as sp


samples = np.array([[20, 10, 5], 
					[5,  2,  1],
					[18, 6, 12]])

r = sp.normalize(samples, norm='l2')
print(r)
