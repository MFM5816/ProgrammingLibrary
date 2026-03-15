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
