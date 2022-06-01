##### 파일 입출력 #####

# 파일 입출력: 파일 생성, 파일 읽기

# f = open('test.txt', 'w')
# 코드 실행하면 콘솔창에는 빈 화면이 뜨지만, 왼쪽 목록에 test.txt 생김

# open(A, B)
# A: 경로를 포함한 파일 이름
# B: 권한



# 경로(매우 중요!!)
# 상대경로: 현재 경로 기준
# 절대경로: 드라이브 기준(윈도우), 리눅스는 root directory(/) 기준
# 쉽게 말해서 드라이브로 시작하지 않는 경로는 모두 상대경로
# 위의 text.txt는 상대경로, 현재 폴더 위치에 text.txt 생성됨



# 왼쪽에 파일 추가 기능 사용하여 abc 폴더 생성

# f = open('abc/test.txt', 'w')
# abc 폴더 안에 test.txt 파일 생성됨



# 이번에는 test_a, test_a 안에 test_b, test_b 안에 test_c 폴더 생성

# 미션)
# test_a 안에 a.txt, test_b 안에 b.png, test_c 안에 c.cpp 생성하기

# f = open('test_a/a.txt', 'w')
# f = open('test_a/test_b/b.png', 'w')
# f = open('test_a/test_b/test_c/c.cpp', 'w')



# 권한: 파일 열 때 목적을 확실히!
# r(read): 읽기
# w(write): 쓰기
# a(append): 덧붙여쓰기



# 권한별 주의사항!!

# r
# f = open('testaaa.txt', 'r')
# 존재하지 않는 파일을 읽으려고 시도하면 에러 발생
# 경로 정확하기 입력하기!



### 쓰기 권한 ###

# w
# f = open('jeju.txt', 'w')
# 존재하지 않는 파일 이름: 파일 생성
# 새로 쓰기 > 기존 내용을 날리고 덮어쓰는 권한(존재하는 파일명 입력 시)
# f.write(x) > 파일에 x라고 작성

# 아래 경우 hello 한 줄만 작성 > w는 새로 쓰는 권한이므로
# for i in range(100):
#     f = open('test.txt', 'w')
#     f.write('hello\n')


# 아래 경우는 hello 100줄 작성
# f = open('test.txt', 'w')

# for i in range(100):
#     f.write('hello\n')



# Q. "구구단" 폴더 생성 후 코드 실행했을 때 단 별 파일 생성되도록
# 조건 1) 각각의 파일 안에는 구구단의 각 단이 찍혀있어야 함
# 조건 2) f.write 안에는 하나의 문자열이 들어가야 함
# 2단.txt
# 3단.txt
# ...
# 9단.txt

# for i in range(2, 10):
#     f = open(f'구구단/{i}단.txt', 'w')
#     for j in range(1, 10):
#         f.write(f'{i} x {j} = {i*j}\n')



# 인코딩 오류
# 데이터를 0, 1로 변환하는 인코딩 과정에서 오류가 발생할 수 있음
# 파일에 한글을 적으려고 하면 이상한 문자가 뜸

# f = open('test.txt', 'w')
# f.write('파이썬 허니잼!!')


# VScode 하단을 보면 UTF-8 인코딩 방식을 사용
# 한글을 입력할 경우 아래처럼 적어주면 인코딩 오류를 방지할 수 있음

# f = open('test.txt', 'w', encoding='utf-8')
# f.write('파이썬 허니잼!!')



# Q. 아래와 같이 출력되도록 프로그래밍
# 파이썬 허니잼!! 1
# 파이썬 허니잼!! 2
# ...
# 파이썬 허니잼!! 100

# f = open('test.txt', 'w', encoding='utf-8')
# for i in range(1, 101):
#     f.write(f'파이썬 허니잼!! {i}\n')



### 읽기 권한 ###

f = open('test.txt', 'r', encoding='utf-8')

# print(f.read()) # 파일 전체
# print('-'*30)
# print(f.readline()) # 한 줄
# print('-'*30)
print(f.readlines()) # 한 줄 한 줄 리스트로


# 파일 포인터 개념
# f를 오픈하는 순간 파일 포인터(커서)가 문서 처음 부분에 생김
# 파일 포인터는 읽기를 마치면 그 자리에 그대로 있음
# 그 자리에서부터 이어서 출력함
# 따라서 위에서 한 번에 실행시켜도 f.read()로 전체 읽고 나면
# f.readline()과 f.readlines()의 결과는 아무것도 출력되지 않음
# f.seek(0)으로 커서 다시 맨 위로 이동시킬 수 있음



# Q. 앞서 생성한 구구단 폴더 내부의 파일들을 읽어서 구구단 2~9단 출력

# for i in range(2, 10):
#     f = open(f'구구단/{i}단.txt', 'r')
#     print(f.read())



##### dictionary 복습(나만의 단어장 실습) #####

# 딕셔너리 (자료끼리 관계지어줄때)
# key, value

# d = {} # 빈 딕셔너리 
# key indexing : key 를 통해 value 에 접근

# key : 단어, value : 뜻
# d = {1:"one", 2:"two", 3:"three"}
# print(d[1])

# key indexing 을 통해 값을 갱신, 추가
# d[1] = "일" # 갱신
# d[4] = "four" # 추가
# 기존에 dict 에 존재하는 key 다, 아니다 

# in 멤버연산자 : 기존에 있는 key, 없는 key 구분
# 기본단위 in iter
# print(d)
# print(1 in d)
# print("일" in d)

# 자료삭제
# del d[1]  # 1 key, value 모두 삭제

# print(d)

# for i in d:
#     print(i)








