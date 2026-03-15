import requests
from bs4 import BeautifulSoup
import time
import random
from fake_useragent import UserAgent

class LianjiaSpider(object):
    def __init__(self):
        self.url = 'https://bj.lianjia.com/ershoufang/pg{}/'
        self.blag = 1

    # 随机headers
    def get_headers(self):
        agent = UserAgent().random
        headers = { 'User-Agent':agent }
        return headers

    # 请求函数
    def get_html(self,url):
        if self.blag <= 3:
            try:
                res = requests.get(
                    url,
                    headers=self.get_headers(),
                    timeout=5
                )
                html = res.content.decode()
                return html
            except Exception as e:
                print('Retry')
                self.blag += 1
                self.get_html(url)


    # 解析提取数据
    def parse_html(self,url):
        html = self.get_html(url)
        # html要么为正常内容,要么为None
        if html:
            # "clear LOGVIEWDATA LOGCLICKDATA"
            soup = BeautifulSoup(html,'lxml')
            li_list = soup.find_all('li',attrs={'class':'clear LOGVIEWDATA LOGCLICKDATA'})
            # li_list: [<li class="xxxx">xxx</li>,]
            for li in li_list:
                item = {}
                # positionInfo
                pos_list = li.find('div',attrs={'class':'positionInfo'}).get_text().split('-')
                item['name'] = pos_list[0].strip()
                item['address'] = pos_list[1].strip()
                # houseInfo
                hou_list = li.find('div',attrs={'class':'houseInfo'}).get_text().split('|')
                item['model'] = hou_list[0].strip()
                item['area'] = hou_list[1].strip()
                item['direct'] = hou_list[2].strip()
                item['perfect'] = hou_list[3].strip()
                item['floor'] = hou_list[4].strip()
                item['year'] = hou_list[5].strip()
                item['type'] = hou_list[6].strip()
                # totalPrice
                item['total'] = li.find('div',attrs={'class':'totalPrice'}).get_text().strip()
                # unitPrice
                item['unit'] = li.find('div', attrs={'class': 'unitPrice'}).get_text().strip()
                print(item)


    # 入口函数
    def run(self):
        for i in range(1,101):
            url = self.url.format(i)
            self.parse_html(url)
            time.sleep(random.randint(1,3))
            # 每抓取1页要初始化self.blag
            self.blag = 1

if __name__ == '__main__':
    spider = LianjiaSpider()
    spider.run()


















