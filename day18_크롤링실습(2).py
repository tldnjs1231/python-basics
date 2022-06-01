import requests
from bs4 import BeautifulSoup


##### 바이너리 파일 크롤링 실습 #####

# Q. 월요웹툰 전체 썸네일을 '썸네일' 폴더에 저장
# 파일명은 웹툰제목.png
# https://comic.naver.com/webtoon/weekdayList?week=mon


# res = requests.get('https://comic.naver.com/webtoon/weekdayList?week=mon')

# soup = BeautifulSoup(res.text, 'html.parser')


# def file_name(st):
#     for i in '/\?:*<>|"':
#         st = st.replace(i, '')
#     return st


# for i in soup.select('.thumb > a > img'):
    
#     link = i.get('src')
#     name = file_name(i.get('title'))

#     r = requests.get(link)
    
#     f = open(f'썸네일/{name}.png', 'wb')
#     f.write(r.content)


# '제왕: 빛과 그림자' 웹툰의 경우 파일 이름에 사용할 수 없는 ':' 포함
# 따라서 해당 제목의 png 파일이 생성되지 않음
# 제목에 파일 이름에 사용 불가능한 기호가 포함된 웹툰도 잘 저장되도록
# 파일 이름을 정제하는 file_name 함수를 씌워줌



# Q. 월~일 전체 웹툰의 썸네일 저장하기

# def file_name(st):
#     for i in '/\?:*<>|"':
#         st = st.replace(i, '')
#     return st


# for k in ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']:

#     res = requests.get(f'https://comic.naver.com/webtoon/weekdayList?week={k}')

#     soup = BeautifulSoup(res.text, 'html.parser')


#     for i in soup.select('.thumb > a > img'):
        
#         link = i.get('src')
#         name = file_name(i.get('title'))

#         r = requests.get(link)
        
#         f = open(f'썸네일/{name}.png', 'wb')
#         f.write(r.content)



# Q. 인프런 1~19페이지 무료 강의들 제목 전부 가져오기
# https://www.inflearn.com/courses?charge=free&order=seq&page=1


# for k in range(1, 20):

#     res = requests.get(f'https://www.inflearn.com/courses?charge=free&order=seq&page={k}')

#     soup = BeautifulSoup(res.text, 'html.parser')

#     for i in soup.select('.card-content > .course_title'):
#         print(i.text)



##### 마저 자르기 실습 #####

# Q. 벅스 차트 1~50위까지 노래 제목, 가수 이름 가져오기
# https://music.bugs.co.kr/chart?wl_ref=M_left_02_01


res = requests.get('https://music.bugs.co.kr/chart?wl_ref=M_left_02_01')

soup = BeautifulSoup(res.text, 'html.parser')


for i in soup.select('tbody > tr')[:50]: # list 앞의 50개만 슬라이싱

    title = i.select_one('.title > a').text
    artist = i.select_one('.artist > a').text

    print(f'{title} - {artist}')















