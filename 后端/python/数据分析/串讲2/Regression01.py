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

parameter1 = np.polyfit(x1, y,1)

mp.figure('scatter', facecolor='lightgray')
mp.title('x1')
mp.scatter(x1, y,color="r")
x = np.linspace(x1.min(), x1.max(), 1000)
y = np.polyval(parameter1, x)
mp.plot(x, y)
mp.show()



