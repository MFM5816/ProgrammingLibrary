from urllib import request
import time
import random
from useragents import ua_list
import re
import os

class MaoyanSpider(object):
    def __init__(self):
        self.url = 'https://maoyan.com/board/4?offset={}'

    # 请求功能函数 - html
    def get_html(self,url):
        headers = {
            'User-Agent':random.choice(ua_list)
        }
        req = request.Request(url=url,headers=headers)
        res = request.urlopen(req)
        html = res.read().decode()

        return html

    # 解析功能函数
    def re_func(self,re_bds,html):
        pattern = re.compile(re_bds,re.S)
        r_list = pattern.findall(html)

        return r_list

    # 解析一级页面
    def parse_html(self,one_url):
        one_html = self.get_html(one_url)
        re_bds = '<div class="movie-item-info">.*?href="(.*?)".*?title="(.*?)".*?<p class="star">(.*?)</p>.*?class="releasetime">(.*?)</p>'
        # r_list: [('/films/1203','name','star','time'),()]
        r_list = self.re_func(re_bds,one_html)
        self.save_html(r_list)

    def save_html(self,r_list):
        item = {}
        # r: ('/films/1203','name','star','time')
        for r in r_list:
            item['name'] = r[1].strip()
            item['star'] = r[2].strip()[3:]
            item['time'] = r[3].strip()[5:15]
            two_link = 'https://maoyan.com' + r[0]
            item['comment'] = self.get_comment(two_link)
            print(item)
            self.save_image(two_link,item['name'])

    # 获取评论的函数
    def get_comment(self,two_link):
        two_html = self.get_html(two_link)

        with open('test.html','w') as f:
            f.write(two_html)

        re_bds = '<div class="comment-content">(.*?)</div>'
        comment_list = self.re_func(re_bds,two_html)

        return comment_list


    # 保存图片函数
    def save_image(self,two_link,name):
        two_html = self.get_html(two_link)

        re_bds = '<div class="img.*?"><img class="default-img" data-src="(.*?)" alt=""></div>'
        # link_list: ['src1','src2','src3']
        link_list = self.re_func(re_bds,two_html)

        print(link_list)

        # 创建对应文件夹
        directory = '/home/tarena/images/' + name + '/'
        if not os.path.exists(directory):
            os.makedirs(directory)

        for link in link_list:
            headers = {'User-Agent':random.choice(ua_list)}
            req = request.Request(url=link,headers=headers)
            res = request.urlopen(req)
            html = res.read()

            filename = directory + \
                    link.split('@')[0][-10:]
            with open(filename,'wb') as f:
                f.write(html)
                time.sleep(random.randint(1,3))

    def run(self):
        for offset in range(0,21,10):
            url = self.url.format(offset)
            self.parse_html(url)
            time.sleep(random.randint(1,2))

if __name__ == '__main__':
    spider = MaoyanSpider()
    spider.run()



























