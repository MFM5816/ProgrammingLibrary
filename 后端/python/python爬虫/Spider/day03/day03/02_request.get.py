import requests

url = 'http://www.baidu.com/'
headers = { 'User-Agent':'Mozilla/5.0' }

res = requests.get(url=url,headers=headers)
# 字符编码
res.encoding = 'utf-8'
# 字符串类型
html = res.text
# bytes类型
html = res.content
# HTTP响应码
code = res.status_code
# 返回实际数据的URL地址
url = res.url



# html = requests.get(url=url,headers=headers).text














