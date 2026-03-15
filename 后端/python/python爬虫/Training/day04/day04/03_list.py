# 方法一
my_list = [1,2,3,4,5,1,2,2,3,2,3,4]
my_set = set(my_list)
result = list(my_set)

# 方法二
my_list = [1,2,3,4,5,1,2,3,2,3,4]
my_list.sort()
last = my_list[-1]

for index in range(len(my_list)-2,-1,-1):
    if last == my_list[index]:
        del my_list[index]
    else:
        last = my_list[index]

print(my_list)

# 方法三
my_list = [1,2,3,4,5,1,2,3,2,3,4]
L = []

for char in my_list:
    if char not in L:
        L.append(char)

print(L)














