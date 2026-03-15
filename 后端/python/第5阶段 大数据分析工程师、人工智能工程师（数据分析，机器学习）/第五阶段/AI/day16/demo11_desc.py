"""
demo11_desc.py 特征值矩阵
"""
import cv2 as cv

original = cv.imread('../ml_data/table.jpg')
cv.imshow('Original', original)
gray = cv.cvtColor(original, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)
sift = cv.xfeatures2d.SIFT_create()
keypoints = sift.detect(gray)
# 提取图像的特征值矩阵
_, desc = sift.compute(gray, keypoints)
print(desc.shape)
cv.imshow('desc', desc)
cv.waitKey()