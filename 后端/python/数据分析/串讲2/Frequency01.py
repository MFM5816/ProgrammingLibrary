import numpy as np

Data = [14,19,24,19,16,20,24,20,21,22,
        24,18,17,23,26,22,23,25,25,19,
        18,16,15,24,21,16,19,21,23,20,
        22,22,16,16,16,12,25,19,24,20]

# 求最大值
maxd = np.max(Data)
# 求最小值
mind = np.min(Data)
# 求极差
ptpd = np.ptp(Data)

print('最大值：',maxd)
print('最小值：',mind)
print('极差：',ptpd)
# 设置组限
Top = 30
Bottom = 10
# 分组为4，求组距
P = (Top - Bottom)/4
# 对组距向上取整
print('组距为：',np.ceil(P))

a = [1, 2, 3, 4, 5]
w = [0.1, 0.2, 0.3, 0.4, 0.5]
print("加权平均值：",np.average(a,weights=w))

# 求众数
counts = np.bincount(Data)
print("众数：", np.argmax(counts))

# 求中位数
print("中位数：", np.median(Data))

# 求方差
print("方差：", np.var(Data))

# 求标准差
print('标准差：', np.std(Data))

# 中位数
print("中位数：", np.median(Data))
# 25%分位数
print("25%分位数：", np.percentile(Data, 25))
# 75%分位数
print('75%分位数：', np.percentile(Data, 75))
# 求四分位数
print(np.percentile(Data, (25, 50, 75), interpolation='midpoint'))

# 求协方差
print("协方差：", np.cov(Data))



