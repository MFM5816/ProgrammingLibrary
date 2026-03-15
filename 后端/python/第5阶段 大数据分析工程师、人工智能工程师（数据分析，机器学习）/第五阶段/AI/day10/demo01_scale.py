"""
demo01_scale.py   均值移除
"""
import sklearn.preprocessing as sp
import numpy as np

samples = [[17, 80, 4000], 
		   [20, 90, 4500],
		   [23, 95, 5500]]
# 均值移除
r = sp.scale(samples)
print(r)
print(r.mean(axis=0))
print(r.std(axis=0))

# 求相似度
#         年龄  薪水   身高
# user1   25   20000  180   
# user2   28   19000  176
# user3   40   20000  175

