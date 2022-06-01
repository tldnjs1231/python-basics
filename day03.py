# print(input('입력: '))

# x = input('입력: ')

# print('입력한 값은', x, '입니다.')


# 실습: 이름, 나이, 이메일을 입력 받고 출력하기

# name = input('이름: ')
# age = input('나이: ')
# email = input('이메일: ')

# print(name, age, email)


# 두 수를 입력 받고 두 수의 연산(+, -, x) 들을 출력하는 프로그램

# # 정수
# a = int(input('첫 번째 숫자를 입력해주세요: '))
# b = int(input('두 번째 숫자를 입력해주세요: '))

# print(a+b, a-b, a*b)

# # 실수
# a = float(input('첫 번째 숫자를 입력해주세요: '))
# b = float(input('두 번째 숫자를 입력해주세요: '))

# print(a+b, a-b, a*b)


# 국어, 수학, 과학 점수를 입력 받고 평균을 소수점 아래 두 자리 수까지 출력하는 프로그램

# kor = float(input('국어 점수를 입력해주세요: '))
# math = float(input('수학 점수를 입력해주세요: '))
# sci = float(input('과학 점수를 입력해주세요: '))

# avg = round((kor + math + sci)/3, 2)

# print('평균 점수: ', avg)


# 사과와 배의 개수를 입력 받고, 총 금액을 출력하는 프로그램

# p_app = 3000
# p_pear = 2000

# # 사용자 중심의 프로그램 중요
# # 가격표를 미리 제시해주면 구매 개수를 입력하기 편할 것
# print('='*30)
# print('사과', p_app, '원')
# print('배', p_pear, '원')
# print('='*30)

# app = int(input('사과의 개수: '))
# pear = int(input('배의 개수: '))

# total = app*p_app + pear*p_pear

# print('총 금액: ', total)


# 시, 분, 초를 입력 받고 총 몇 초인지 출력하는 프로그램

# hr = int(input('현재 시간을 입력해주세요(시): '))
# # 최솟값 반환하는 함수 min이 파괴될 수 있으므로 min이 아닌 min_으로
# min_ = int(input('현재 시간을 입력해주세요(분): '))
# sec = int(input('현재 시간을 입력해주세요(초): '))

# hr_sec = hr*60*60
# min_sec = min_*60

# total_sec = hr_sec + min_sec + sec

# print(total_sec)


# 섭씨온도를 화씨온도로 변환해주는 프로그램

# print('='*30)
# print('섭씨온도를 변환해드려요')
# print('='*30)

# celcius = float(input('입력: '))

# fahrenheit = celcius*1.8 + 32

# print('> 화씨온도로', fahrenheit, '입니다.')


# 정N각형의 한 내각을 구해주는 프로그램

# n = float(input('N 입력: '))

# ang = 180*(n-2)/n

# print('한 내각의 크기는', ang, '도 입니다.')


# 현재 등산한 한라산의 높이를 입력 받고, 몇 퍼센트 더 올라가야 하는지 구해주는 프로그램

# height = float(input('얼마나 올라왔냐? '))

# per = round((1947-height)/1947, 2) * 100

# print('앞으로', per, '% 더 올라가야댐ㅋㅋㅋㅋㅋ')


# 세 자리 수를 입력 받고, 각 자리 수를 출력하는 프로그램

# n = int(input('입력: '))

# n_100 = n//100
# n_10 = (n%100)//10
# n_1 = n%10

# print('백의 자리', n_100)
# print('십의 자리', n_10)
# print('일의 자리', n_1)


# 생년월일을 정수로 입력 받고, 년, 월, 일을 나눠서 출력하세요

# birthday = int(input('입력: '))

# year = birthday//10000
# month = (birthday%10000)//100
# day = birthday%100

# print(year, '년')
# print(month, '월')
# print(day, '일')


# 총 sec을 입력 받고, 시간, 분, 초를 출력해주는 프로그램

total_sec = int(input('총 초: '))

hr = total_sec//3600
min_ = (total_sec%3600)//60
sec = total_sec%60

print(hr, '시간', min_, '분', sec, '초')


