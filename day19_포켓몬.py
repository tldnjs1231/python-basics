from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep # 업로드, 스크롤 등 작업하는 시간 기다리기 위해
import requests


# requests 대신 selenium 사용해서 페이지 소스 가져오기
# requests 하면 시간이 많이 걸리므로 selenium 사용

driver = webdriver.Chrome('chromedriver.exe')
driver.get('https://pokemongo.inven.co.kr/dataninfo/pokemon/')
sleep(2)

ht = driver.page_source # html 소스 가져오기
driver.close()


# 소스 가져왔으므로 파싱 작업

soup = BeautifulSoup(ht, 'html.parser')



# Mission) poke 폴더 안에 제목이 포켓몬 이름인 사진 파일 가져오기
# https://pokemongo.inven.co.kr/dataninfo/pokemon/


# 포켓몬 이름에는 특수문자가 없지만 혹시 모르니까 매번 넣어주면 좋을듯
def file_name(st):
    for i in '/\?:*<>|"':
        st = st.replace(i, '')
    return st


for i in soup.select('.pokemonicon'):

    name = file_name(i.select_one('.pokemonname').text)
    img_link = 'https:' + i.select_one('img').get('src')
    # 그런데, 개발자 툴 자세히 보면 src에 http:가 생략되어 있음
    # 따라서 http: 앞에 붙여줌
    # 참고) 포켓몬 아이콘 클릭해서 들어가면 상세 페이지 나옴
    # 거기서 포켓몬 사진 소스 보면 이미지 링크 한 부분이 다름
    # pokemonicon이던 부분이 pokemonimage
    # name 변수 text 뒤에 .replace('pokemonicon', 'pokemonimage')
    # 붙여주면 더 화질 좋은 사진을 받을 수 있음

    r = requests.get(img_link) 
    
    f = open(f'poke/{name}.png', 'wb')
    f.write(r.content)




