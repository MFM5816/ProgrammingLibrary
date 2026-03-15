"""
demo04_vc.py  验证曲线
"""
import numpy as np
import sklearn.ensemble as se
import sklearn.metrics as sm
import sklearn.preprocessing as sp
import sklearn.model_selection as ms
import matplotlib.pyplot as mp

data = []
with open('../ml_data/car.txt', 'r') as f:
	for line in f.readlines():
		data.append(line[:-1].split(','))
data = np.array(data)
print(data.shape)

# 整理输入集与输出集
col_num = data.shape[1]
train_x, train_y, encoders = [], [], []
for col in range(col_num):
	col_array = data[:, col]
	encoder = sp.LabelEncoder()
	if col < col_num-1:
		train_x.append(encoder.fit_transform(col_array))
	else:
		train_y = encoder.fit_transform(col_array)
	encoders.append(encoder)

train_x = np.array(train_x).T
train_y = np.array(train_y)
print(train_x.shape, train_y.shape)
print(train_x[0], train_y[0])

# 训练模型：
model = se.RandomForestClassifier(
	max_depth=9, n_estimators=140, random_state=7)

# # 验证曲线  验证max_depth
# depths = np.arange(1, 20)
# train_scores, test_scores = ms.validation_curve(
# 	model, train_x, train_y,
# 	'max_depth', depths, cv=5)
# f1s = np.mean(test_scores, axis=1)

# mp.grid(linestyle=':')
# mp.plot(depths, f1s, 'o-', label='max_depth')
# mp.legend()
# mp.show()


# # 验证曲线  验证n_estimators
# estimators = np.arange(100,200,5)
# train_scores, test_scores = ms.validation_curve(
# 	model, train_x, train_y,
# 	'n_estimators', estimators, cv=5)
# f1s = np.mean(test_scores, axis=1)

# mp.grid(linestyle=':')
# mp.plot(estimators, f1s, 'o-', label='estimators')
# mp.legend()
# mp.show()


model.fit(train_x, train_y)

# 准备测试
data = [
    ['high', 'med', '5more', '4', 'big', 'low'],
    ['high', 'high', '4', '4', 'med', 'med'],
    ['low', 'low', '2', '4', 'small', 'high'],
    ['low', 'med', '3', '4', 'med', 'high']]
data = np.array(data)
test_data = []
for i, col in enumerate(data.T):
	encoder = encoders[i]
	col_val = encoder.transform(col)
	test_data.append(col_val)
test_data = np.array(test_data).T
pred_test_y = model.predict(test_data)
print(pred_test_y)
print(encoders[-1].inverse_transform(pred_test_y))