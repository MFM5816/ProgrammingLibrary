# -*- coding: utf-8 -*-
import scrapy
import time
import random
from hashlib import md5
import json
from ..items import YoudaoItem

class YoudaoSpider(scrapy.Spider):
    name = 'youdao'
    allowed_domains = ['fanyi.youdao.com']
    word = input('请输入要翻译的单词:')

    # 重写start_requests()方法
    def start_requests(self):
        # 1.url参数: 定义post的URL地址
        post_url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
        # 2.formdata参数: 定义form表单数据为字典
        ts,salt,sign = self.get_ts_salt_sign(self.word)
        formdata = {
            "i": self.word,
            "from": "AUTO",
            "to": "AUTO",
            "smartresult": "dict",
            "client": "fanyideskweb",
            "salt": salt,
            "sign": sign,
            "ts": ts,
            "bv": "5d4cb17cceb9ecd02ece3ed9923d3a7a",
            "doctype": "json",
            "version": "2.1",
            "keyfrom": "fanyi.web",
            "action": "FY_BY_REALTlME",
        }
        cookies = self.get_cookies()
        # 3.交给调度器入队列
        yield scrapy.FormRequest(
            url=post_url,
            formdata=formdata,
            callback=self.parse,
        )
    # 处理cookies为字典
    def get_cookies(self):
        cs = "OUTFOX_SEARCH_USER_ID=584508170@10.108.160.19; OUTFOX_SEARCH_USER_ID_NCOO=415742579.8667161; JSESSIONID=aaa6xixEY8dfdcuUIHo3w; ___rl__test__cookies=1571131223483"
        cs_list = cs.split('; ')
        cs_dict = {}
        for c in cs_list:
            cs_dict[c.split('=')[0]] = c.split('=')[1]

        return cs_dict


    # 获取ts,salt,sign
    def get_ts_salt_sign(self,word):
        ts = str(int(time.time()*1000))
        salt = ts + str(random.randint(0,9))
        string = "fanyideskweb" + word + salt + "n%A-rKaT5fb[Gy?;N5@Tj"
        s = md5()
        s.update(string.encode())
        sign = s.hexdigest()

        return ts,salt,sign

    def parse(self,response):
        # 1.获取翻译结果: item['result']
        # 2.交给管道文件处理: yield item
        item = YoudaoItem()
        html = json.loads(response.text)
        item['result'] = html['translateResult'][0][0]['tgt']

        yield item






