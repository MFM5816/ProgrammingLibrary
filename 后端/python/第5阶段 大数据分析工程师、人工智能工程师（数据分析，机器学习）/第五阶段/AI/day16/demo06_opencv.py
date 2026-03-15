"""
demo06_opencv.py   opencv基础
"""
import cv2 as cv
import numpy as np

original = cv.imread('../ml_data/forest.jpg')
print(original.shape, original[0,0])
cv.imshow('original', original)
# 切出图像中的某一通道数据
blue = np.zeros_like(original)
blue[:,:,0] = original[:,:,0]
cv.imshow('blue', blue)
green = np.zeros_like(original)
green[:,:,1] = original[:,:,1]
cv.imshow('green', green)
red = np.zeros_like(original)
red[:,:,2] = original[:,:,2]
cv.imshow('red', red)
# 图像裁剪
h, w = original.shape[:2]
cropped = original[ int(h/4) : int(h*3/4), 
		 		    int(w/4) : int(w*3/4) ]
cv.imshow('cropped', cropped)
# 图像缩放
resize1 = cv.resize(original, (300, 200))
cv.imshow('resize1', resize1)
resize2 = cv.resize(resize1, None, fx=2, fy=2)
cv.imshow('resize2', resize2)
# 图像保存
cv.imwrite('red.jpg', red)
cv.waitKey()