from selenium import webdriver
from ydmapi import *
from PIL import Image

class YdmSpider(object):
    def __init__(self):
        self.url = 'http://www.yundama.com/'
        # 部分windows需要将chrome窗口最大化
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('--start-maximized')
        self.browser = webdriver.Chrome(options=self.options)

    # 1.获取首页截图: index.jpg
    def get_index(self):
        self.browser.get(self.url)
        self.browser.save_screenshot('index.png')

    # 2.获取验证码截图: cache.jpg
    def get_cachejpg(self):
        # 1.找验证码节点位置(x y坐标)
        location = self.browser.find_element_by_xpath('//*[@id="verifyImg"]').location
        # 2.大小(宽度和高度)
        size = self.browser.find_element_by_xpath('//*[@id="verifyImg"]').size
        # 左上角x y坐标
        left = location['x']
        top = location['y']
        # 右下角x y坐标
        right = left + size['width']
        bottom = top + size['height']

        # 3.截图验证码图片 - crop((x,y,x,y))
        img = Image.open('index.png').crop((left,top,right,bottom))
        img.save('cache.png')

    # 云打码在线识别
    def get_cache(self):
        result = get_result('cache.png')

        return result

    # 入口函数
    def run(self):
        self.get_index()
        self.get_cachejpg()
        result = self.get_cache()
        print(result)

if __name__ == '__main__':
    spider = YdmSpider()
    spider.run()




































