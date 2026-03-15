import matplotlib.pyplot as mp
import numpy as np

x = np.linspace(0, 5 * np.pi+3, 50)
wave = np.sin(x)
transformed = np.fft.fft(wave)
# 绘制wave图像
mp.figure('FFT')
mp.subplot(231)
mp.plot(wave)
mp.xticks([])
mp.yticks([])
# 将wave进行傅里叶变换
mp.subplot(232)
mp.plot(transformed)
mp.xticks([])
mp.yticks([])
# 进行逆向傅里叶变换
mp.subplot(233)
mp.plot(np.fft.ifft(transformed))
mp.xticks([])
mp.yticks([])
# 移频
shifted = np.fft.fftshift(transformed)
mp.subplot(234)
mp.plot(shifted)
mp.xticks([])
mp.yticks([])
# 还原移频
mp.subplot(235)
mp.plot(np.fft.ifftshift(shifted))
mp.xticks([])
mp.yticks([])
mp.show()
