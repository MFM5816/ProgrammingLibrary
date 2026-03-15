import requests
import json
import time
from urllib import parse

class TencentSpider(object):
    def __init__(self):
        self.one_url = 'https://careers.tencent.com/tencentcareer/api/post/Query?timestamp=1571206111698&countryId=&cityId=&bgIds=&productId=&categoryId=&parentCategoryId=&attrId=&keyword={}&pageIndex={}&pageSize=10&language=zh-cn&area=cn'
        self.two_url = 'https://careers.tencent.com/tencentcareer/api/post/ByPostId?timestamp=1571206506767&postId={}&language=zh-cn'
        self.headers = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
        # 打开文件
        self.f = open('tencent.json','w')
        self.job_list = []

    def parse_html(self,url):
        one_html = requests.get(
            url=url,
            headers=self.headers
        ).json()
        # 提取postId,拼接二级页面地址
        for one in one_html['Data']['Posts']:
            # postId ,two_url
            postid = one['PostId']
            two_url = self.two_url.format(postid)
            self.get_data(two_url)
            time.sleep(0.1)

    def get_data(self,two_url):
        html = requests.get(
            url=two_url,
            headers=self.headers
        ).json()
        job = {}
        job['name'] = html['Data']['RecruitPostName']
        job['duty'] = html['Data']['Responsibility']
        job['require'] = html['Data']['Requirement']
        # 所有数据都添加都字典job中
        self.job_list.append(job)
        print(job)

    def run(self):
        keyword = input('请输入关键字:')
        keyword = parse.quote(keyword)

        total_page = self.get_total_page(keyword)
        for page in range(1,total_page+1):
            url = self.one_url.format(keyword,page)
            self.parse_html(url)

        # 存储到json文件中
        json.dump(self.job_list,self.f,ensure_ascii=False)
        # 关闭文件
        self.f.close()

    # 获取总页数
    def get_total_page(self,keyword):
        url = self.one_url.format(keyword,1)
        html = requests.get(url=url,headers=self.headers).json()
        count = html['Data']['Count']
        if count % 10 == 0:
            total_page = count // 10
        else:
            total_page = (count // 10) + 1

        return total_page

if __name__ == '__main__':
    spider = TencentSpider()
    spider.run()















