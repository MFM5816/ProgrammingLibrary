#课堂练习1
"""
猜数字
程序随机产生0-100之间的一个整数guess；
然后玩家输入猜测的数字num；
当输入猜测的数字num大于guess，则输出数字大了；
当输入猜测的数字num小于guess，则输出数字小了；
当输入猜测的数字num等于guess，则输出猜中了，并停止程序
"""
#导入random库
#random 随机数库
import random

#使用random库产出一个随机数
guess = random.randint(0,101)

while True:
    #输入猜测的数字
    num = int(input("?"))
    #当输入猜测的数字num大于guess，则输出数字大了；
    if num > guess:
        print("猜大了")
    #当输入猜测的数字num小于guess，则输出数字小了；
    elif num < guess:
        print("猜小了")
    else:
        print("猜中了")
        break

#课堂练习2
"""
使用turtle库绘制正方形

图形绘制函数库
"""
#导入turtle 并名为pen
import turtle as pen

#设置pen的属性
pen.pensize(3) #设置笔的粗细
pen.color("red") #设置笔的颜色

for i in range(4): #绘制4次
    #绘制100的直线
    pen.forward(100)
    #向左转90度
    pen.left(90)

"""
使用turtle库绘制五角星
图形绘制函数库
"""

import turtle as pen

#设置pen的属性
pen.pensize(3) #设置笔的粗细
pen.color("red","yellow") #设置笔的颜色和填充颜色

#调整绘制方向
pen.left(108)

#开始填充
pen.begin_fill()
#开始绘制
for i in range(5):
    #绘制一个角
    pen.forward(200)
    pen.left(144)
    pen.forward(200)
    #为下一次绘制调整方向
    pen.right(72)
pen.end_fill()
#结束填充
