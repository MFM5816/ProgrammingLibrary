"""
demo03_mfcc.py
"""
import numpy as np
import matplotlib.pyplot as mp
import python_speech_features as sf
import scipy.io.wavfile as wf

# 读音频文件
sample_rate, sigs = wf.read(
	'../da_data/filter.wav')
print(sample_rate, sigs.shape)
# 提取音频文件的mfcc
mfcc = sf.mfcc(sigs, sample_rate)
print(mfcc.shape)
# 画mfcc  
mp.imshow(mfcc.T, cmap='gist_rainbow')
mp.show()











