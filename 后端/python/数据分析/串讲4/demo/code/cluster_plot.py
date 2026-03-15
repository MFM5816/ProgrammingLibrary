import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

datafile = '../tmp/zscoreddata.csv' # 读取数据

data = pd.read_csv(datafile)

#设置类别个数5
k = 5
#创建聚类模型对象
kmodel = KMeans(n_clusters=k)
kmodel.fit(data)

#查看聚类中心和对应的类别
print(kmodel.cluster_centers_)
print(kmodel.labels_)



#图形展示

clu = kmodel.cluster_centers_
x = [1,2,3,4,5]
colors = ['red','green','yellow','blue','black']
for i in range(5):
    plt.plot(x, clu[i],label='cluster'+str(i), color=colors[i], marker='o')

plt.xlabel('L R F M C')
plt.ylabel('values')
plt.show()