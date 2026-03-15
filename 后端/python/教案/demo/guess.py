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
