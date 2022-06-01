import requests
from bs4 import BeautifulSoup


##### 웹 크롤링 실습 #####

# Q. 웹툰 참교육 82화 평점, 참여자수, 등록일 가져오기
# https://comic.naver.com/webtoon/detail?titleId=758037&no=82&weekday=mon


# res = requests.get('https://comic.naver.com/webtoon/detail?titleId=758037&no=82&weekday=mon')


# soup = BeautifulSoup(res.text, 'html.parser')


# TotalNumber = soup.select_one('#topPointTotalNumber > strong')
# TotalPerson = soup.select_one('.pointTotalPerson > em')
# date = soup.select_one('.date')
# tip. 셀렉터 이름이 너무 길면 개발자 툴에서 더블클릭 후 복사하면 됨

# print(TotalNumber)
# print(TotalPerson)
# print(date)



# Q. 웹툰 참교육 웹툰제목, 작가이름, 작품소개, 웹툰장르, 웹툰연령
# https://comic.naver.com/webtoon/list?titleId=758037&weekday=mon


# res = requests.get('https://comic.naver.com/webtoon/list?titleId=758037&weekday=mon')


# soup = BeautifulSoup(res.text, 'html.parser')


# title = soup.select_one('h2 > .title')
# writer = soup.select_one('.wrt_nm')
# intro = soup.select_one('.detail > p')
# genre = soup.select_one('.genre')
# age = soup.select_one('.age')

# print(title)
# print(writer)
# print(intro)
# print(genre)
# print(age)



# Q. 웹툰 참교육 1화부터 82화까지 평점, 참여자수, 등록일 가져오기
# https://comic.naver.com/webtoon/list?titleId=758037&weekday=mon


# for i in range(1, 82):
#     res = requests.get(f'https://comic.naver.com/webtoon/detail?titleId=758037&no={i}&weekday=mon')

#     soup = BeautifulSoup(res.text, 'html.parser')

#     rate = soup.select_one('#topPointTotalNumber > strong').text
#     per = soup.select_one('.pointTotalPerson > em').text
#     date = soup.select_one('.date').text

#     print(f'참교육 {i}화 평점 {rate}, 참여자수 {per}, 등록일 {date}')



# 퇴근 문제)
# 롤에는 159 개의 챔피언이 있습니다.

# https://lol.inven.co.kr/dataninfo/champion/detail.php?code={}

# 저기 code 의 인자가 챔피언 출시순서를 의미해요 1~159 까지요!

# 롤 캐릭터 나온 순서를 리스트로 저장!!
# 다음 프로그램을 작성해보세요!!

# ex)
# 몇 번째 캐릭터 찾아줄까 ? 159
# 159 번째 캐릭터는 '레나타 글라스크' 야!!

# ex)
# 몇 번째 캐릭터 찾아줄까 ? 158
# 158 번째 캐릭터는 '제리' 야!!



# tqdm
# 크롤링 하다보면 데이터가 방대해 긁어오는 데 오래 걸리는 경우가 있음
# 진행 상황을 시각화해 지루하지 않게 만들어주는 라이브러리
# iter 부분에 tqdm() 씌워주면 됨
# 명령 프롬포트에 pip install tqdm 입력하여 설치 후 사용

from tqdm import tqdm


champs = []

for i in tqdm(range(1, 160)):
    res = requests.get(f'https://lol.inven.co.kr/dataninfo/champion/detail.php?code={i}')

    soup = BeautifulSoup(res.text, 'html.parser')

    name = soup.select_one('.korName').text.split(',')[0]
    champs.append(name)


num = input('몇 번째 캐릭터 찾아줄까? ')

print(f'{num} 번째 캐릭터는 {champs[int(num)-1]} 야!!')




