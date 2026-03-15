import re
import os

with open('file3.md','r') as f:
    data = f.read()
    result = re.sub('root','tarena',data)
    print(result)

# 把file3.md文件中,root全部改为tarena
os.system("sed -i 's/root/tarena/g' file3.md")
print('Success!')

# sed -i 's/原内容/新内容/g' 文件名














