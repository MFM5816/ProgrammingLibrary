import requests
import json
from fake_useragent import UserAgent
import re

class DoubanSpider(object):
    def __init__(self):
        self.url = 'https://movie.douban.com/j/chart/top_list?'
        self.i = 0

    def parse_html(self,params):
        html = requests.get(
            url=self.url,
            params=params,
            headers={ 'User-Agent':UserAgent().random }
        ).text
        # json.loads(): 把json数据->Python数据类型
        html = json.loads(html)
        # 提取数据
        item = {}
        for film in html:
            item['name'] = film['title']
            item['score'] = film['score']
            print(item)
            self.i += 1

    def run(self):
        type_dict = self.get_all()
        menu = ''
        for key in type_dict.keys():
            # key: '剧情' '喜剧'
            menu += ' {} '.format(key)

        print(menu)
        name = input('请输入电影类别:')
        # 得到了type的值
        typ = type_dict[name]

        total = self.get_total(typ)
        # 100个电影 range(0,100,20)
        for page in range(0,total,20):
            params = {
                'type': typ,  # 电影类型
                'interval_id': '100:90',
                'action': '',
                'start': str(page),  # 每次加载电影的起始索引值 0 20 40 60
                'limit': '20'  # 每次加载的电影数量
            }
            self.parse_html(params)
        print('电影总数:',self.i)

    def get_all(self):
        url = 'https://movie.douban.com/chart'
        html = requests.get(
            url=url,
            headers={'User-Agent':UserAgent().random}
        ).text
        p = re.compile('<a href=".*?type_name=(.*?)&type=(.*?)&.*?</a>',re.S)
        r_list = p.findall(html)
        # [('剧情','5'),('喜剧','24')]
        type_dict = {}
        for r in r_list:
            type_dict[r[0]] = r[1]

        return type_dict

    def get_total(self,typ):
        url = 'https://movie.douban.com/j/chart/top_list_count?type={}&interval_id=100%3A90'.format(typ)
        html = requests.get(
            url=url,
            headers={ 'User-Agent':UserAgent().random }
        ).json()
        total = html['total']

        return total


if __name__ == '__main__':
    spider = DoubanSpider()
    spider.run()



















