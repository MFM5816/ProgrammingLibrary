#-*- coding: utf-8 -*-
#数据清洗，过滤掉不符合规则的数据

import pandas as pd

datafile= '../data/air_data.csv' #航空原始数据,第一行为属性标签
cleanedfile = '../tmp/data_cleaned.csv' #数据清洗后保存的文件

data = pd.read_csv(datafile,encoding='utf-8') #读取原始数据，指定UTF-8编码（需要用文本编辑器将数据装换为UTF-8编码）

data = data[data['SUM_YR_1'].notnull() & data['SUM_YR_2'].notnull()] #票价非空值才保留
print(data)
#只保留票价非零的，或者平均折扣率与总飞行公里数同时为0的记录。
index1 = data['SUM_YR_1'] != 0
index2 = data['SUM_YR_2'] != 0
index3 = (data['SEG_KM_SUM'] == 0) & (data['avg_discount'] == 0) #该规则是“与”
data = data[index1 | index2 | index3] #该规则是“或”
# 数据规约
data = data[['FFP_DATE','LOAD_TIME', 'FLIGHT_COUNT', 'avg_discount', 'SEG_KM_SUM','LAST_TO_END']]
print(data)
data.to_csv(cleanedfile) #导出结果

# 数据变化的LRFMC数据：
#L = LOAD_TIME - FFP_DATE （观测窗口时间 - 入会时间）
#R = LOAD_TIME - LAST_TO_END （观测窗口时间 - 最后一次乘机时间）
#F = FLIGHT_COUNT
#M = SEG_KM_SUM
#C = avg_discount

LRFMCdata = '../tmp/LRFMC.csv' #数据清洗后保存的文件

from datetime import datetime

def normal_time(date):
    return datetime.strptime(date, '%Y/%m/%d')

def interval_time(dd):
    #计算时间间隔，以月为单位
    return dd.days / 30

# data_LRFMC数据
data_LRFMC = pd.DataFrame()
# data_LRFMC.columns = ['L', 'R', 'F','M', 'C']
data_LRFMC['L'] = (data['LOAD_TIME'].apply(normal_time) - data['FFP_DATE'].apply(normal_time)).apply(interval_time)
data_LRFMC['R'] = data['LAST_TO_END']/30
data_LRFMC['F'] = data['FLIGHT_COUNT']
data_LRFMC['M'] = data['SEG_KM_SUM']
data_LRFMC['C'] = data['avg_discount']

# 显示数据的描述，最大值和最小值
data_LRFMC_describe = data_LRFMC.describe().T
MM = data_LRFMC_describe = data_LRFMC_describe[['max','min']].T
print(MM)

data_LRFMC.to_csv(LRFMCdata) #导出结果



