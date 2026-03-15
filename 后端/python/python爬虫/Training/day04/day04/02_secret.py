# 1、每一位分别加5，然后分别将其替换为该数除以10取余后的结果
# 2、将该数的第1位和第4位互换，第二位和第三位互换
# 3、最后合起来作为加密后的整数输出

# 加密函数
def encrption(num):
    L = []
    for n in num:
        L.append(str((int(n)+5) % 10))
    # 换位置 - 反转
    L.reverse()
    result = ''.join(L)

    return result

if __name__ == '__main__':
    num = input('请输入四位数字:')
    if len(num) == 4:
        print(encrption(num))
    else:
        print('不是四位!!!!!!!')














