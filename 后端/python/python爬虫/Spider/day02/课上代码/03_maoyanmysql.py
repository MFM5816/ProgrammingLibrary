from urllib import request
import re
import time
import random
from useragents import ua_list
import pymysql

class MaoyanSpider(object):
    def __init__(self):
        self.url = 'https://maoyan.com/board/4?offset={}'
        self.db = pymysql.connect(
            'localhost','root','123456','maoyandb',
            charset='utf8'
        )
        self.cursor = self.db.cursor()

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

    def save_html(self, r_list):
        # excutemany -> [(),(),()]
        L = []
        ins = 'insert into filmtab values(%s,%s,%s)'
        for r in r_list:
            t = (
                r[0].strip(),
                r[1].strip()[3:],
                r[2].strip()[5:15]
            )
            L.append(t)
        self.cursor.executemany(ins,L)
        self.db.commit()

    def run(self):
        for offset in range(0,31,10):
            url = self.url.format(offset)
            self.get_html(url)
            time.sleep(random.uniform(1,2))

        # 断开数据库连接
        self.cursor.close()
        self.db.close()

if __name__ == '__main__':
    spider = MaoyanSpider()
    spider.run()

































