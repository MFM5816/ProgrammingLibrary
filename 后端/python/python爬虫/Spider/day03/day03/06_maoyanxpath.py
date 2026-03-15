import requests
from lxml import etree

class MaoyanSpider(object):
    def __init__(self):
        self.url = 'https://maoyan.com/board/4'
        self.headers = { 'User-Agent':'' }

    def save_html(self):
        html = requests.get(url=self.url,headers=self.headers).text
        # 解析
        parse_html = etree.HTML(html)
        # 基准xpath,大的节点对象列表
        dd_list = parse_html.xpath('//dl[@class="board-wrapper"]/dd')
        item = {}
        for dd in dd_list:
            item['name'] = dd.xpath('.//p[@class="name"]/a/@title')[0].strip()
            item['star'] = dd.xpath('.//p[@class="star"]/text()')[0].strip()
            item['time'] = dd.xpath('.//p[@class="releasetime"]/text()')[0].strip()

            print(item)

    def run(self):
        self.save_html()

if __name__ == '__main__':
    spider = MaoyanSpider()
    spider.run()
















