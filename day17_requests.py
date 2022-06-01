import requests
from bs4 import BeautifulSoup


##### 1. requests #####

# requests.get(url)
# url로 request 날림, response를 반환

res = requests.get('https://www.naver.com')
print(type(res))

print(res.text) # HTML 소스



# res.text는 파이썬에서 아무 의미 없는 문자열
# html 소스 끌어와도 그냥 꺾쇠일 뿐, 태그로 인식 못하고 문자열로 인식
# 그래서 필요한 것이 파싱
# 파싱: 규격에 맞춰 해석함






