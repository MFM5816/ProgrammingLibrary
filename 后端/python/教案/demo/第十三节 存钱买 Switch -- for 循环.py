"""
第十三节 存钱买 Switch -- for 循环
"""
#课堂练习1
"""
输出 5 遍 Hello World
"""
#方法1
print("Hello World")
print("Hello World")
print("Hello World")
print("Hello World")
print("Hello World")

#方法2 使用for循环
for i in range(5):
    print("Hello World")


#课堂练习2
"""
输出 0-5 之间所有的整数
"""
#方法一
print(0)
print(1)
print(2)
print(3)
print(4)
print(5)

#方法二
for i in range(6): # i -> [0,n-1)
    print(i)

#今日知识
"""
1. for 循环的常用语法 :
    for i in range(x):
        语句组
    
    (1) 说明：
        1 语句组重复执行 x 次
        2 i 能取到的值：0 到 x-1，[0，x-1)
        3 x 必须是一个大于零的整数
2. 关于计数技巧: 从 a 到 b 之间有 b-a+1 个整数
"""
#课堂练习3
"""
输出 0-100 之间所有的偶数
"""
for i in range(101):
    #偶数 被2整除 =》 除以2没有余数
    #当是被2整除的数字，就输出该数字
    if i % 2 ==0:
        print(i)


#拓展练习
"""
1.请用户输入 n，输出 0~n 之间所有的 3 的倍数
"""
n = int(input())
for i in range(n+1):
    if i % 3 == 0:
        print(i)

"""
2. 请用户输入 n，代表有 n 个苹果，然后输入这 n 个苹果的质量（0-100），请输
出有多少个苹果的质量超过 80
"""
n = int(input("n?"))
count = 0
for i in range(n):
    w = int(input("w"))
    if w >= 80:
        count = count + 1
print(count)

