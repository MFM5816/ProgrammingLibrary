# 功能: 把文件中每10行yield到生成器
def readfile(f):
    count = 0
    line_list = []
    for line in f:
        line_list.append(line)
        count += 1

        if count == 10:
            yield line_list
            line_list = []
            count = 0
    # 把剩下的不到10行的也yield
    if line_list:
        yield line_list

if __name__ == '__main__':
    with open('file.md','r') as f:
        g = readfile(f)
        for content in g:
            print(content)

# 结果输出:
# ['1\n','2\n','3\n',xxxx]
# ['11\n',xxx]
























