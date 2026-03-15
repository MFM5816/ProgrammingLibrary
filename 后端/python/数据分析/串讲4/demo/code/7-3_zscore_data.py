#-*- coding: utf-8 -*-
#标准差标准化

import pandas as pd

datafile = '../tmp/LRFMC.csv' #需要进行标准化的数据文件；
zscoredfile = '../tmp/zscoreddata.csv' #标准差化后的数据存储路径文件；

#标准化处理
data = pd.read_csv(datafile,usecols=[1,2,3,4,5])
data = (data - data.mean(axis = 0))/(data.std(axis = 0)) #简洁的语句实现了标准化变换，类似地可以实现任何想要的变换。
data.columns = ['Z'+i for i in data.columns] #表头重命名。

print(data)
data.to_csv(zscoredfile, index = False) #数据写入