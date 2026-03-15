"""
demo04_speech.py 音频识别
"""
import numpy as np
import sklearn.svm as svm
import python_speech_features as sf
import scipy.io.wavfile as wf
import sklearn.metrics as sm
import os

def searchfiles(directory):
	# 声明函数，读取目录中的文件路径等信息
	# {'apple':[url,...], 'banana':[url...], 'kiwi':[...]}
	urls = {}
	for curdir, subdir, files in os.walk(directory):
		for file in files:
			path = os.path.join(curdir, file)
			label = curdir.split(os.path.sep)[-1]
			if label not in urls.keys():
				urls[label] = []
			urls[label].append(path)
	return urls

urls = searchfiles('../ml_data/speeches/training')
# 针对所有输出标签，做标签编码
import sklearn.preprocessing as sp
encoder = sp.LabelEncoder()
encoder.fit(list(urls.keys()))
# 遍历urls，整理训练集数据
train_x, train_y = [], []
for label, urllist in urls.items():
	for url in urllist:
		# 把当前音频文件转成mfcc
		sample_rate, sigs = wf.read(url)
		mfcc = sf.mfcc(sigs, sample_rate)
		mfcc = np.mean(mfcc, axis=0)
		train_x.append(mfcc)
		train_y.append(encoder.transform([label]))

train_x = np.array(train_x)
train_y = np.array(train_y).ravel()

# 训练模型
model = svm.SVC(
	kernel='linear', degree=2, probability=True)
# import sklearn.linear_model as lm
# model = lm.LogisticRegression()
# import sklearn.naive_bayes as nb
# model = nb.GaussianNB()

model.fit(train_x, train_y)
# 针对训练数据，评估测试结果
pred_train_y = model.predict(train_x)
print('train data classification report:')
print(sm.classification_report(train_y, pred_train_y))

# 加载测试样本
urls = searchfiles('../ml_data/speeches/testing')
# 遍历urls，整理测试集数据
test_x, test_y = [], []
for label, urllist in urls.items():
	for url in urllist:
		# 把当前音频文件转成mfcc
		sample_rate, sigs = wf.read(url)
		mfcc = sf.mfcc(sigs, sample_rate)
		mfcc = np.mean(mfcc, axis=0)
		test_x.append(mfcc)
		test_y.append(encoder.transform([label]))
test_x = np.array(test_x)
test_y = np.array(test_y).ravel()
# 预测
pred_test_y = model.predict(test_x)
print('test data classification report:')
print(sm.classification_report(test_y, pred_test_y))

# 输出每个样本当前类别的置信概率
probs = model.predict_proba(test_x)
for label, prob in zip(
	pred_test_y, np.max(probs, axis=1)):
	print(label, '->', prob)



