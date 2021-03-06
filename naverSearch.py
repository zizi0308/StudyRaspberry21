import urllib.request as urq
import urllib.parse as uparse
import datetime
import json

class naverSearch(object):
    # 생성자
    def __init__(self):
        print('Naver Search API 생성')
    
    # 네이버 API 요청함수
    def getRequestUrl(self, url):
        req = urq.Request(url)
        req.add_header('X-Naver-Client-Id', 'bBS8aAYUjQGGTKqyEfXW')
        req.add_header('X-Naver-Client-Secret', '4CvK0wd7Zc')

    # 요청한 결과를 네이버 서버에 돌려받음
        try:
            res = urq.urlopen(req)
            if res.getcode() == 200: # ok
                print('[{0}] URL Request succeed'.format(datetime.datetime.now()))
                return res.read().decode('utf-8')
        except Exception as e:
                print(e)
                return None

    # 네이버검색 API 사용함수
    def getNaverSearchResult(self, sNode, search_word, page_start, display):
        base = 'https://openapi.naver.com/v1/search/'
        node = '{0}.json'.format(sNode)
        param = '?start={0}&display={1}&query={2}'.format(page_start, 
                                display, uparse.quote(search_word))
        url = base + node + param # https://openapi.naver.com...nodeval.json?start=1&display=10&query=코로나

        retData = self.getRequestUrl(url)
        if retData == None:
            return None
        else:
            return json.loads(retData)

    # 데이터 처리
    def getPostDate(self, post, jsonResult):
        title = post['title']
        desc = ['description']
        org_link = post['originallink']
        link = post['link']
        pDate = datetime.datetime.strptime(post['pubDate'], '%a, %d %d %Y %H:%M:%S +0900')    #문자열로 들어온 값을 datetime으로 파싱
        p_date = pDate.strftime('%Y-%m-%d %H:%M:%S')

        jsonResult.append({})
        pass
        return