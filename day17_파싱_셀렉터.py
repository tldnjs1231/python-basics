from bs4 import BeautifulSoup


st = """<html>
    <body>
        <div id="hello1">안녕1</div>
        <div class="hello2">안녕2</div>
        <div>
            <span>안녕3</span>
        </div>
        <a href="https://www.naver.com">NAVER</a>
    </body>
</html>"""



# BeautifulSoup(A, B)
# A: 아무 의미 없는 문자열
# B: 문법
# 아무 의미 없는 A를 B 문법을 활용해 soup에 넣는 것

soup = BeautifulSoup(st, 'html.parser')
# soup는 위의 아무 의미 없는 st를 html 형식으로 해석할 수 있는 친구!



# soup.select(셀렉터): 가져오고 싶은 태그 여러 개(list로 모두 가져옴)
# soup.select_one(셀렉터): 가져오고 싶은 태그가 하나(문자열로 가져옴)
# 하나일 때도 select 써줘도 되지만 하나면 select_one 쓰기
# select 쓰면 결과가 하나여도 무조건 리스트 자료형으로 반환
# 여러 개일 때 select_one 쓰면 최초의 하나만 가져옴

# print(soup.select('a'))
# 위의 문자열에서 a 태그 모두 가져옴

# print(soup.select('#hello1'))
# id가 hello1인 태그 모두 가져옴

print(soup.select('.hello2'))
# class가 hello2인 태그 모두 가져옴

print(soup.select('div > span'))
# div 태그 하위의 span 태그 가져옴
# 시작점은 상관 없음: 아래도 결과 똑같음
print(soup.select('html > body > div > span'))

# 하위태그 기호를 꼭 태그명과 사용할 필요는 없음
# soup.select('#a > .b > div > #c') 이런 식으로 섞어도 상관 없음
# 브라우저 개발자 툴에서 ctrl + f 누르고 셀렉터 표현 입력하면 해당 셀렉터 표현으로 선택되는 태그가 몇 개인지 확인할 수 있음
# 하나 뿐이라면 원하는 태그를 정확하게 지칭할 수 있는 것





