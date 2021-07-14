from bs4 import BeautifulSoup as bs
from pprint import pprint
import requests as req

# 검색 url
url = 'https://search.naver.com/search.naver?query=날씨'
html = req.get(url) # 웹사이트 가져오기
# pprint(html.text)
soup = bs(html.text, 'html.parser') # beautifulsoul으로 

datas = soup.find('div', {'class' : 'detail_box'})  # 미세먼지 영역찾기
# pprint(finedust)
details = datas.findAll('dd')       # 요소 3개 찾기
# pprint(details)

# 미세먼지
finedust = details[0].find('span', {'class', 'num'}).get_text()
pprint(finedust)
# 초미세먼지
ultrafinedust = details[1].find('span', {'class', 'num'}).get_text()
# 오존
ozone = details[2].find('span', {'class', 'num'}).get_text()

print('{0}, {1}, {2}'.format(finedust, ultrafinedust, ozone))
