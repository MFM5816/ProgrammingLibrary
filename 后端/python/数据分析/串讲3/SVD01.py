import numpy as np

M = np.mat('1 2 3;4 5 6;7 8 9')
print(M)
U, sv, V = np.linalg.svd(M)
print(U.shape)
print(V.shape)
print(sv.shape)
print(U * np.diag(sv) * V)
