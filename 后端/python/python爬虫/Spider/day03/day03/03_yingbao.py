import requests

url = 'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1570861377384&di=d91c7af06d3acb8e2edb33a57e407db7&imgtype=0&src=http%3A%2F%2Fb-ssl.duitang.com%2Fuploads%2Fitem%2F201702%2F28%2F20170228090601_jnLUR.jpeg'
headers = { 'User-Agent': 'Mozilla/5.0' }

html = requests.get(url=url,headers=headers).content
with open('赵丽颖.jpg','wb') as f:
    f.write(html)































