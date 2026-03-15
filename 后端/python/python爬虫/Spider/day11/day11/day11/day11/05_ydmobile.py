'''手机端有道翻译数据抓取'''
import requests
from lxml import etree

post_url = 'http://m.youdao.com/translate'
headers = { 'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1' }
word = input('请输入要翻译的单词:')
data = {
    'inputtext': word,
    'type': 'AUTO',
}

html = requests.post(
    url=post_url,
    data=data,
    headers=headers
).text

p = etree.HTML(html)
result = p.xpath('//ul[@id="translateResult"]/li/text()')[0]

print('翻译结果:',result)
























