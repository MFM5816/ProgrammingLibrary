import re

with open('file2.md','r') as f:
    s = 0
    while True:
        data = f.read(1024)
        if not data:
            break
        r_list = re.findall('[A-Z]',data)
        s += len(r_list)

print('大写字母总数:',s)















