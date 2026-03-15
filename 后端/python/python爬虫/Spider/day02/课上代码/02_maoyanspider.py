from urllib import request
import re
import time
import random
from useragents import ua_list
import csv

class MaoyanSpider(object):
    def __init__(self):
        self.url = 'https://maoyan.com/board/4?offset={}'

    def get_html(self,url):
        headers = {'User-Agent':random.choice(ua_list)}
        req = request.Request(url=url,headers=headers)
        res = request.urlopen(req)
        html = res.read().decode()
        # 直接解析
        self.parse_html(html)

    def parse_html(self,html):
        re_bds = '<div class="movie-item-info">.*?title="(.*?)".*?<p class="star">(.*?)</p>.*?class="releasetime">(.*?)</p>'
        pattern = re.compile(re_bds,re.S)
        # r_list: [('大话西游','周星驰','1994'),(),()]
        r_list = pattern.findall(html)
        self.save_html(r_list)

    # writerow()实现
    # def save_html(self,r_list):
    #     with open('maoyan.csv','a') as f:
    #         writer = csv.writer(f)
    #         for r in r_list:
    #             name = r[0].strip()
    #             star = r[1].strip()[3:]
    #             #上映时间：1994-09-10(加拿大)
    #             time = r[2].strip()[5:15]
    #             L = [name,star,time]
    #             writer.writerow(L)
    #             print(name,time,star)

    # writerows()实现 - [(),(),()]
    def save_html(self, r_list):
        L = []
        with open('maoyan.csv', 'a') as f:
            writer = csv.writer(f)
            for r in r_list:
                name = r[0].strip()
                star = r[1].strip()[3:]
                # 上映时间：1994-09-10(加拿大)
                time = r[2].strip()[5:15]
                L.append((name,star,time))
                print(name, time, star)
            # 在for循环外面
            writer.writerows(L)

    def run(self):
        for offset in range(0,31,10):
            url = self.url.format(offset)
            self.get_html(url)
            time.sleep(random.uniform(1,2))

if __name__ == '__main__':
    spider = MaoyanSpider()
    spider.run()

































