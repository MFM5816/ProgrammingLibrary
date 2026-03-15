"""
demo07_canny.py  边缘识别
"""
import cv2 as cv

# 读取灰度图片
original = cv.imread(
	'../ml_data/chair.jpg', cv.IMREAD_GRAYSCALE)
cv.imshow('original', original)
#提取边缘
hsobel=cv.Sobel(original, cv.CV_64F, 1, 0, ksize=5)
cv.imshow('hsobel', hsobel)
vsobel=cv.Sobel(original, cv.CV_64F, 0, 1, ksize=5)
cv.imshow('vsobel', vsobel)
sobel=cv.Sobel(original, cv.CV_64F, 1, 1, ksize=5)
cv.imshow('sobel', sobel)
# 拉普拉斯边缘识别
laplacian = cv.Laplacian(original, cv.CV_64F)
cv.imshow('Laplacian', laplacian)
# canny边缘识别
canny = cv.Canny(original, 50, 200)
cv.imshow('Canny', canny)

cv.waitKey()
