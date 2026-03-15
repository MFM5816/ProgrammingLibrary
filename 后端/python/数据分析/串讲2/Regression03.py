import numpy as np
import matplotlib.pyplot as mp
Data = np.loadtxt(r'Tyler.txt')
print(Data)
x1= Data[:,0]
x2 = Data[:,1]
y = Data[:,2]
print("x1:", x1)
print("x2:", x2)
print("y:", y)

parameter2 = np.polyfit(x2, y,1)
mp.figure('scatter', facecolor='lightgray')
mp.title('x2')
mp.scatter(x2, y,color="r")
x = np.linspace(x2.min(), x2.max(), 1000)
y = np.polyval(parameter2, x)
mp.plot(x, y)
mp.show()