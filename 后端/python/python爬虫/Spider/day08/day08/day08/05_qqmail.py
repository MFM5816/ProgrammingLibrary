from selenium import webdriver

url = 'https://mail.qq.com/'
browser = webdriver.Chrome()
browser.get(url)

# 1.切换到iframe子页面
iframe = browser.find_element_by_id('login_frame')
browser.switch_to.frame(iframe)
# 2.用户名+密码+登录按钮
browser.find_element_by_id('u').send_keys('2621470058')
browser.find_element_by_id('p').send_keys('zhanshen001')
browser.find_element_by_id('login_button').click()













