import numpy as np
from sklearn import linear_model
Data = np.loadtxt(r'Tyler.txt')
print(Data)
x = Data[:,:2]
y = Data[:,2]
print("x:", x)
print("y:", y)
regr = linear_model.LinearRegression()
regr.fit(x,y)
print('coefficients(p0,p1):',regr.coef_)
print('intercept(b):',regr.intercept_)



