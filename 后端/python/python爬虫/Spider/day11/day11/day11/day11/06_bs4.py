# sudo pip3 install beautifulsoup4
from bs4 import BeautifulSoup as bs

html = '''
<div class="test">雄霸</div>
<div class="test">灭霸</div>
'''
soup = bs(html,'lxml')
r_list = soup.find_all('div',attrs={'class':'test'})
# r_list: [<div class="test">雄霸</div>,<xxx>]
for r in r_list:
    print(r.get_text())







