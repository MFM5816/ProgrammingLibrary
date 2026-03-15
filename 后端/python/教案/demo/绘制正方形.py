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
