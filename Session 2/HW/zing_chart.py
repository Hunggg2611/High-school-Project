from urllib.request import urlopen
from bs4 import BeautifulSoup
web = urlopen('http://nhaczingmp3.com/bang-xep-hang/bai-hat-Viet-Nam/IWZ9Z08I.html')
content = web.read().decode('utf8')
web.close()
soup = BeautifulSoup(content, 'html.parser')
ul_chart = soup.find('ul', 'box-song')
li_chart_list = ul_chart.find_all('li')
for li in li_chart_list:
    a = li.a
    print(a['title'])
