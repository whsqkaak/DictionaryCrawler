# python 3.7에서 실행
# requests, BeautifulSoup4 설치
# 한국어를 검색하면 한국어, 영어, 일어, 중국어, 프랑스어를 긁어줌

import requests
from bs4 import BeautifulSoup as bs

while True:
    print("**한국어를 입력하면 네이버 사전에서 영어, 일어, 중국어, 프랑스어를 크롤링해주는 프로그램입니다.**\n"
          "검색할 한국어 단어를 입력해주세요.")
    word = input()

    s = requests.Session()
    dict_page = "https://dict.naver.com/search.nhn?dicQuery=" + word
    html = ""
    resp = s.get(dict_page)
    if resp.status_code == 200:
        html = resp.text
    soup = bs(html, 'html.parser')

    result = ''

    # 영어
    try:
        result += '영어 : ' + soup.find('div', {'class': 'en_dic_section search_result dic_en_entry'}) \
            .find('dl', {'class': 'dic_search_result'}).find('a', {'class': 'auto_link'}).get_text() + '\n'
    except:
        result += '영어 단어를 찾지 못했습니다.\n'

    # 일본어
    try:
        result += '일본어 : ' + soup.find('div', {'class': 'jp_dic_section search_result dic_jp_entry'}) \
            .find('dl', {'class': 'dic_search_result'}).find('dd')\
            .find('sup', {'class': 'huri'}).get_text() + '\n'
    except:
        result += '일본어 단어를 찾지 못했습니다.\n'

    # 중국어
    try:
        result += '중국어 : ' + soup.find('div', {'class': 'cn_dic_section search_result dic_cn_entry'}) \
            .find('dl', {'class': 'dic_search_result'}).find('dd')\
            .find('em').next_sibling\
            .strip() + '\n'
    except:
        result += '중국어 단어를 찾지 못했습니다.\n'

    # 프랑스어
    try:
        result += '프랑스어 : ' + soup.find('div', {'class': 'fr_dic_section search_result search_result2 dic_fr_entry'}) \
            .find('dl', {'class': 'dic_search_result'}).find('dd')\
            .find('p').get_text()\
            .strip() + '\n'
    except:
        result += '프랑스어 단어를 찾지 못했습니다.\n'

    print(result)
    print('다시 검색하시겠습니까? (Y / N)')
    re = input()
    if not (re == 'Y' or re == 'y'):
        break

