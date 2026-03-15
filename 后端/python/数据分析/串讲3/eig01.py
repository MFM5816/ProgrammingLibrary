import numpy as np
import scipy.misc as sm
import matplotlib.pyplot as mp

# 读取图片数据
img = sm.imread('dog.jpg', True)
print(img.shape)

# 提取img矩阵的特征值与特征向量
img = np.mat(img)
eigvals, eigvecs = np.linalg.eig(img)
print("特征值，特征向量：", eigvals.shape, eigvecs.shape)

# 抹掉一部分特征值
eigvals[120:] = 0
img2 = eigvecs * np.diag(eigvals) * eigvecs.I
img2 = img2.real
print(img2.dtype)

# 奇异值分解
U, sv, V = np.linalg.svd(img)
sv[50:] = 0
img3 = U * np.diag(sv) * V

mp.figure('Dog')
mp.subplot(221)
mp.imshow(img, cmap='gray')
mp.xticks([])
mp.yticks([])

mp.subplot(222)
mp.imshow(img2, cmap='gray')
mp.xticks([])
mp.yticks([])

mp.subplot(224)
mp.imshow(img3, cmap='gray')
mp.xticks([])
mp.yticks([])
mp.tight_layout()
mp.show()
