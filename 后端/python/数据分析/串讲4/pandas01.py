import pandas as pd
import numpy as np
np.random.seed(12345)


obj = pd.Series(range(3), index=['a', 'b', 'c'])
index = obj.index
print(index)
print(index[1:])

obj = pd.Series([4.5, 7.2, -5.3, 3.6], index=['d', 'b', 'a', 'c'])
print(obj)
obj2 = obj.reindex(['a', 'b', 'c', 'd', 'e'])
print(obj2)


obj3 = pd.Series(['blue', 'purple', 'yellow'], index=[0, 2, 4])
print(obj3)
print(obj3.reindex(range(6), method='ffill'))
print(obj3.reindex(range(6), method='bfill'))

frame = pd.DataFrame(np.arange(9).reshape((3, 3)),
                     index=['a', 'c', 'd'],
                     columns=['Ohio', 'Texas', 'California'])
print(frame)
frame2 = frame.reindex(['a', 'b', 'c', 'd'])
print(frame2)


states = ['Texas', 'Utah', 'California']
print(frame.reindex(columns=states))
print(frame.loc[['a', 'b', 'c', 'd'], states])

print('-'*45)
# 删除
data = pd.DataFrame(np.arange(16).reshape((4, 4)),
                    index=['Ohio', 'Colorado', 'Utah', 'New York'],
                    columns=['one', 'two', 'three', 'four'])

print(data)
print(data.drop(['Colorado', 'Ohio']))

print(data.drop('two', axis=1))
print(data.drop(['two', 'four'], axis='columns'))
print(obj.drop('c', inplace=True))
print(obj)

print('-'*45)
# loc 和 iloc
data = pd.DataFrame(np.arange(16).reshape((4, 4)),
                    index=['Ohio', 'Colorado', 'Utah', 'New York'],
                    columns=['one', 'two', 'three', 'four'])
print(data)
print(data.loc['Colorado', ['two', 'three']])
print(data.iloc[2, [3, 0, 1]])
print(data.iloc[[1, 2], [3, 0, 1]])
print(data.loc[ :'Utah', 'two'])
print(data.iloc[:, :3][data.three > 5])

print('-'*45)
# 算数运算和数据对齐
s1 = pd.Series([7.3, -2.5, 3.4, 1.5], index=['a', 'c', 'd', 'e'])
s2 = pd.Series([-2.1, 3.6, -1.5, 4, 3.1],
               index=['a', 'c', 'e', 'f', 'g'])
print(s1)
print(s2)
print(s1+s2)

df1 = pd.DataFrame(np.arange(9.).reshape((3, 3)), columns=list('bcd'),
                   index=['Ohio', 'Texas', 'Colorado'])
df2 = pd.DataFrame(np.arange(12.).reshape((4, 3)), columns=list('bde'),
                   index=['Utah', 'Ohio', 'Texas', 'Oregon'])
print(df1)
print(df2)
print(df1+df2)

df1 = pd.DataFrame({'A': [1, 2]})
df2 = pd.DataFrame({'B': [3, 4]})
print(df1)
print(df2)
print(df1 - df2)

print('-'*45)
# 在算术⽅法中填充值
df1 = pd.DataFrame(np.arange(12.).reshape((3, 4)),
                   columns=list('abcd'))
df2 = pd.DataFrame(np.arange(20.).reshape((4, 5)),
                   columns=list('abcde'))
df2.loc[1, 'b'] = np.nan
print(df1)
print(df2)
print(df1 + df2)
print(df1.add(df2, fill_value=0))
print(1 / df1)
print(df1.rdiv(1))
print(df1.reindex(columns=df2.columns, fill_value=0))

# 排序和排名
frame = pd.DataFrame(np.arange(8).reshape((2, 4)),
                     index=['three', 'one'],
                     columns=['d', 'a', 'b', 'c'])
print(frame.sort_index())
print(frame.sort_index(axis=1))
print(frame.sort_index(axis=1, ascending=False))

obj = pd.Series([7, -5, 7, 4, 2, 0, 4])
print(obj.rank())
# 也可以根据值在原数据中出现的顺序给出排名
print(obj.rank(method='first'))

# 汇总和计算描述统计
df = pd.DataFrame([[1.4, np.nan], [7.1, -4.5],
                   [np.nan, np.nan], [0.75, -1.3]],
                  index=['a', 'b', 'c', 'd'],
                  columns=['one', 'two'])
print(df)
print(df.describe())
