"""
demo04_bin.py  二值化
"""
import numpy as np
import sklearn.preprocessing as sp

raw_samples = np.array([[17., 100., 4000],
					    [20., 80., 5000],
					    [23., 75., 5500]])

bin = sp.Binarizer(threshold=80)
r = bin.transform(raw_samples)
print(r)

# 读取图片
import scipy.misc as sm
import matplotlib.pyplot as mp
#读取文件
original = sm.imread('../da_data/lily.jpg', True)
mp.subplot(221)
mp.imshow(original, cmap='gray')
mp.xticks([])
mp.yticks([])
mp.tight_layout()


mask = img2.astype('?')
img3 = np.zeros_like(original)
img3[mask] = original[mask]
mp.subplot(224)
mp.imshow(img3, cmap='gray')
mp.xticks([])
mp.yticks([])
mp.tight_layout()


mp.subplot(222)
bin = sp.Binarizer(threshold=137)
img2 = bin.transform(original)
mp.imshow(img2, cmap='gray')
mp.xticks([])
mp.yticks([])
mp.tight_layout()

mp.show()