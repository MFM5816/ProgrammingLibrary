import requests
from urllib import parse
import re
import time
import random
from fake_useragent import UserAgent
import os

class BaiduImageSpider(object):
    def __init__(self):
        self.url = 'https://image.baidu.com/search/index?tn=baiduimage&word={}'

    def get_ua(self):
        ua = UserAgent()
        agent = ua.random
        return agent

    def get_image(self,url,word):
        html = requests.get(
            url=url,
            headers={'User-Agent':self.get_ua()}
        ).text
        pattern = re.compile('"hoverURL":"(.*?)"',re.S)
        # link_list: ['http://xxx.jpg','','']
        link_list = pattern.findall(html)

        # 创建对应文件夹
        directory = '/home/tarena/images/{}/'.format(word)
        if not os.path.exists(directory):
            os.makedirs(directory)

        i = 1
        for link in link_list:
            # /home/tarena/images/赵丽颖/赵丽颖_1.jpg
            filename = directory+word+'_'+str(i)+'.jpg'
            filename = '{}{}_{}.jpg'.format(directory,word,i)
            self.save_image(link,filename)
            i += 1
            time.sleep(random.randint(1,2))

    def save_image(self,link,filename):
        html = requests.get(
            url=link,
            headers={'User-Agent':self.get_ua()}
        ).content
        with open(filename,'wb') as f:
            f.write(html)
            print('%s下载成功' % filename)

    def run(self):
        word = input('请输入姓名:')
        params = parse.quote(word)
        url = self.url.format(params)
        self.get_image(url,word)

if __name__ == '__main__':
    spider = BaiduImageSpider()
    spider.run()



