"""
demo08_lr.py  线性回归
"""
import numpy as np
import matplotlib.pyplot as mp

train_x = np.array([0.5, 0.6, 0.8, 1.1, 1.4])
train_y = np.array([5.0, 5.5, 6.0, 6.8, 7.0])

times = 1000
w0, w1, losses, epoches = [1], [1], [], []
lrate = 0.01
for i in range(times):
	epoches.append(i+1)
	loss = (((w0[-1] + w1[-1] * train_x) - train_y) ** 2).sum() / 2
	losses.append(loss)
	print('{:4}> w0={:.6f}, w1={:.6f}, loss={:.6f}'.format(i+1, w0[-1], w1[-1], loss))
	# 求得w0方向上的偏导数用于更新w0
	d0 = (w0[-1] + w1[-1]*train_x - train_y).sum()
	# 求得w1方向上的偏导数用于更新w1
	d1 = (train_x*(w0[-1] + w1[-1]*train_x - train_y)).sum()
	# 更新w0与w1
	w0.append(w0[-1] - d0*lrate)
	w1.append(w1[-1] - d1*lrate)

# 画图
mp.figure('Linear Regression', facecolor='lightgray')
mp.title('Linear Regression', fontsize=18)
mp.grid(linestyle=':')
mp.scatter(train_x, train_y, color='dodgerblue',
	s=80, marker='o', label='Samples')
# 绘制回归线
pred_train_y = w0[-1] + w1[-1]*train_x
mp.plot(train_x, pred_train_y, color='orangered',
	label='Regression Line', linewidth=2)
mp.legend()

# 绘制w0  w1  loss的变化曲线
w0 = w0[:-1]
w1 = w1[:-1]
mp.figure('Training Progress', facecolor='lightgray')
mp.subplot(311)
mp.title('Training Progress', fontsize=20)
mp.ylabel('w0', fontsize=14)
mp.gca().xaxis.set_major_locator(mp.MultipleLocator(100))
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
mp.plot(epoches, w0, c='dodgerblue', label='w0')
mp.legend()
mp.subplot(312)
mp.ylabel('w1', fontsize=14)
mp.gca().xaxis.set_major_locator(mp.MultipleLocator(100))
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
mp.plot(epoches, w1, c='limegreen', label='w1')
mp.legend()

mp.subplot(313)
mp.xlabel('epoch', fontsize=14)
mp.ylabel('loss', fontsize=14)
mp.gca().xaxis.set_major_locator(mp.MultipleLocator(100))
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
mp.plot(epoches, losses, c='orangered', label='loss')
mp.legend()

# 基于三维曲面图，绘制梯度下降过程
import mpl_toolkits.mplot3d as axes3d
grid_w0, grid_w1 = np.meshgrid(
    np.linspace(0, 9, 500),
    np.linspace(0, 3.5, 500))
grid_loss = np.zeros_like(grid_w0)
for x, y in zip(train_x, train_y):
    grid_loss += ((grid_w0 + x*grid_w1 - y) ** 2) / 2

mp.figure('Loss Function')
ax = mp.gca(projection='3d')
mp.title('Loss Function', fontsize=20)
ax.set_xlabel('w0', fontsize=14)
ax.set_ylabel('w1', fontsize=14)
ax.set_zlabel('loss', fontsize=14)
ax.plot_surface(grid_w0, grid_w1, grid_loss, rstride=20, cstride=20, cmap='jet')
ax.plot(w0, w1, losses, 'o-', c='orangered', label='BGD')
mp.legend()

# 以等高线的方式绘制梯度下降
mp.figure('Batch Gradient Descent', facecolor='lightgray')
mp.title('Batch Gradient Descent', fontsize=20)
mp.xlabel('w0', fontsize=14)
mp.ylabel('w1', fontsize=14)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
mp.contourf(grid_w0, grid_w1, grid_loss, 20, cmap='jet')
cntr = mp.contour(grid_w0, grid_w1, grid_loss, 20,
                  colors='black', linewidths=0.5)
mp.clabel(cntr, inline_spacing=0.1, fmt='%.2f',
          fontsize=8)
mp.plot(w0, w1, 'o-', c='orangered', label='BGD')
mp.legend()

mp.show()
