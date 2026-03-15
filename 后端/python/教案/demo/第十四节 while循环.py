#第十四节 -while 循环
#1.体验下面的程序,思考两个程序的区别
#程序1 请输入你的5个爱好，并输出
for i in range(5):
    like = input("like?")
    print("我喜欢",like)

#程序2 请输入你的爱好，当输入空格时停止输入
while True:  #使用无限循环一定设置停止条件
    like  = input("like?")
    if like == " ":   #设置停止条件
        break
    print("我喜欢",like)

#知识点
    
"""
语法：
    for i in range(n):
        循环语句
    while 循环条件:  
        循环语句

    #当将循环条件直接写为"True"时，则变为条件恒成立，循环为无限循环
     若想让其停止，则需要break。
区别：
    for 循环擅长次数固定的循环;
    while 循环擅长达到目的循环;

"""
#2.练习
"""
使用 while 循环输出 1-10 之间的所有整数
"""
i = 0 #计数器
while i <=10:
    print(i)
    i = i + 1 #务必让计数器自增1，否则就变成死循环了

#拓展练习
"""
1.使用 while 循环输出 1-10 之间的所有偶数:
"""
i = 0 
while i <=10:
    if i % 2 == 0:
        print(i)
    i = i + 1 
"""
2.  请用户输入 n，输出 0~n 之间所有的 3 的倍数（使用 while 循环）
"""
n = int(input("n"))
i = 0
while i <= n:
    if i % 3 == 0:
        print(i)
    i = i + 1
