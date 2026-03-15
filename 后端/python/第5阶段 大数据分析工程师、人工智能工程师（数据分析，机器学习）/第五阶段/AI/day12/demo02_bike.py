"""
demo02_bike.py   共享单车
"""
import numpy as np
import matplotlib.pyplot as mp
import sklearn.ensemble as se
import sklearn.metrics as sm
import sklearn.utils as su

data = []
with open('../ml_data/bike_day.csv', 'r') as f:
	for line in f.readlines():
		data.append(line[:-1].split(','))
# 通过data整理输入、输出、header
data = np.array(data)
header = data[0, 2:13]
x = data[1:, 2:13].astype('f8')
y = data[1:, -1].astype('f8')

# 整理训练集、测试集  训练随机森林回归模型
x, y = su.shuffle(x, y, random_state=7)
train_size = int(len(x) * 0.9)
train_x, test_x, train_y, test_y = \
	x[:train_size], x[train_size:], \
	y[:train_size], y[train_size:]

model = se.RandomForestRegressor(
	max_depth=10, n_estimators=1000,
	min_samples_split=2)
model.fit(train_x, train_y)
pred_test_y = model.predict(test_x)
# 评估模型
print(sm.r2_score(test_y, pred_test_y))
# 使用模型
sample = \
	[[1, 2, 1, 0, 0, 1, 1, 0.35, 0.38,0.75, 0.1]]
result = model.predict(sample)
print(result)
day_fi = model.feature_importances_

mp.figure('Feature Importance', facecolor='lightgray')
mp.subplot(211)
mp.title('Day Feature Importance', fontsize=16)
mp.grid(linestyle=':', axis='y')
x = np.arange(day_fi.size)
sorted_indices = day_fi.argsort()[::-1]
mp.xticks(x, header[sorted_indices])
mp.bar(x, day_fi[sorted_indices], 0.8, 
	color='dodgerblue', label='DT Feature Importances')
mp.legend()
mp.tight_layout()



data = []
with open('../ml_data/bike_hour.csv', 'r') as f:
	for line in f.readlines():
		data.append(line[:-1].split(','))
# 通过data整理输入、输出、header
data = np.array(data)
header = data[0, 2:14]
x = data[1:, 2:14].astype('f8')
y = data[1:, -1].astype('f8')

# 整理训练集、测试集  训练随机森林回归模型
x, y = su.shuffle(x, y, random_state=7)
train_size = int(len(x) * 0.9)
train_x, test_x, train_y, test_y = \
	x[:train_size], x[train_size:], \
	y[:train_size], y[train_size:]

model = se.RandomForestRegressor(
	max_depth=10, n_estimators=1000,
	min_samples_split=2)
model.fit(train_x, train_y)
pred_test_y = model.predict(test_x)
# 评估模型
print(sm.r2_score(test_y, pred_test_y))

hour_fi = model.feature_importances_

mp.figure('Feature Importance', facecolor='lightgray')
mp.subplot(212)
mp.title('Hour Feature Importance', fontsize=16)
mp.grid(linestyle=':', axis='y')
x = np.arange(hour_fi.size)
sorted_indices = hour_fi.argsort()[::-1]
mp.xticks(x, header[sorted_indices])
mp.bar(x, hour_fi[sorted_indices], 0.8, 
	color='orangered', label='Hour Feature Importances')
mp.legend()
mp.tight_layout()
mp.show()