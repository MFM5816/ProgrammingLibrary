from selenium import webdriver

browser = webdriver.Chrome()
browser.get('http://www.mca.gov.cn/article/sj/xzqh/2019/')
browser.find_element_by_xpath('//*[@id="list_content"]/div[2]/div/ul/table/tbody/tr[2]/td[2]/a').click()

all_handles = browser.window_handles
browser.switch_to.window(all_handles[1])

tr_list  = browser.find_elements_by_tag_name('tr')
for tr in tr_list:
    print(tr.text)

browser.close()