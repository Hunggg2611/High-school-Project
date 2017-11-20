from urllib.request import urlopen
from bs4 import BeautifulSoup

web = urlopen('http://s.cafef.vn/bao-cao-tai-chinh/VNM/IncSta/2017/3/0/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-sua-viet-nam.chn')
infcontent = web.read().decode('utf8')
web.close()

bs = BeautifulSoup(content, 'html.parser')
table = bs.find('table', id='tablecontent')
tdlists = table.find_all('td')
for td in tdlists:
    print(td.get_text())
