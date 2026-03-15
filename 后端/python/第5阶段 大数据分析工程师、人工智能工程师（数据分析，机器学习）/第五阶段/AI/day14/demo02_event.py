"""
demo2_event.py 事件预测
"""
import numpy as np
import sklearn.svm as svm
import sklearn.preprocessing as sp
import sklearn.model_selection as ms
import sklearn.metrics as sm

class DigitEncoder():
	def fit_transform(self, y):
		return y.astype('i4')

	def transform(self, y):
		return y.astype('i4')

	def inverse_transform(self, y):
		return y.astype(str)


# 1. 加载文件整理数据集
data = []
with open('../ml_data/events.txt', 'r') as f:
	for line in f.readlines():
		data.append(line[:-1].split(','))
data = np.array(data)
data = np.delete(data, 1, axis=1)
print(data.shape)
# 针对每一列进行编码LabelEncoder   DigitEncoder
col = data.shape[1]
x, y, encoders = [], [], []
for i in range(col):
	col_val = data[:, i]
	# 判断使用哪一种Encoder对当前列进行编码
	if col_val[0].isdigit():
		encoder = DigitEncoder()
	else:
		encoder = sp.LabelEncoder()
	# 使用encoder编码当前列，存入数据集
	if i < col-1:
		x.append(encoder.fit_transform(col_val))
	else:
		y = encoder.fit_transform(col_val)
	encoders.append(encoder)

x = np.array(x).T
y = np.array(y)
print(x.shape, y.shape, x[0], y[0])

# 2. 选择模型，开始训练
train_x, test_x, train_y, test_y = \
	ms.train_test_split(
		x, y, test_size=0.25, random_state=7)
model = svm.SVC(kernel='rbf', 
	            class_weight='balanced')
model.fit(train_x, train_y)
pred_test_y = model.predict(test_x)
print(sm.classification_report(test_y, pred_test_y))

# 3. 预测结果
data = np.array([['Tuesday', '13:30:00', '21', '23']])
test_x = []
for i in range(len(data.T)):
	col_val = data[:, i]
	encoder = encoders[i]
	test_x.append(encoder.transform(col_val))
test_x = np.array(test_x).T
pred_test_y = model.predict(test_x)
print(encoders[-1].inverse_transform(pred_test_y))
