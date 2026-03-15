"""
demo04_sigmoid.py
"""
import numpy as np
import matplotlib.pyplot as mp

x = np.linspace(-10, 10, 500)
y = 1 / (1+np.exp(-x))

mp.grid(linestyle=':')
mp.plot(x, y)
mp.show()