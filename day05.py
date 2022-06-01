##### Level 01 실습 문제 #####

### 1 ###

# math = float(input('수학 점수: '))
# sci = float(input('과학 점수: '))

# avg = (math + sci)/2

# if avg >= 90:
#     print('A')
# elif avg >= 80:
#     print('B')
# elif avg >= 70:
#     print('C')
# else:
#     print('D')


### 2 ###

# n1 = float(input('첫 번째 숫자: '))
# n2 = float(input('두 번째 숫자: '))
# op = input('연산자(+, -, *, / 중 하나를 입력해주세요): ')

# if op == '+':
#     print(n1 + n2)
# elif op == '-':
#     print(n1 - n2)
# elif op == '*':
#     print(n1 * n2)
# elif op == '/':
#     print(n1 / n2)
# else:
#     print('연산자가 이상해요')


### 3 ###

# month = int(input('월: '))

# if month == 3 or month == 4 or month == 5:
#     print(month, '월은 봄입니다!')
# elif month == 6 or month == 7 or month == 8:
#     print(month, '월은 여름입니다!')
# elif month == 9 or month == 10 or month == 11:
#     print(month, '월은 가을입니다!')
# elif month == 12 or month == 1 or month ==2:
#     print(month, '월은 겨울입니다!')
# else:
#     print('입력이 바르지 않습니다.')

# if 3 <= month <= 5:
#     print(month, '월은 봄입니다!')
# elif 6 <= month <= 8:
#     print(month, '월은 여름입니다!')
# elif 9 <= month <= 11:
#     print(month, '월은 가을입니다!')
# elif 1 <= month <= 12: # 3~11월에서 걸리면 여기까지 내려올 일 없음
#     print(month, '월은 겨울입니다!')
# else:
#     print('입력이 바르지 않습니다.')

# if 1 <= month <= 12:
#    if 3 <= month <= 5:
#        print(month, '월은 봄입니다!')
#    elif 6 <= month <= 8:
#        print(month, '월은 여름입니다!')
#    elif 9 <= month <= 11:
#        print(month, '월은 가을입니다!')
#    else:
#        print(month, '월은 겨울입니다!')
# else:
#     print('입력이 바르지 않습니다.')


### 4 ###

# 아이디 = input('아이디 입력: ')
# 패스워드 = input('패스워드 입력: ')

# if 아이디 == 'admin':
#     if 패스워드 == 'admin':
#         print('로그인 성공')
#     else:
#         print('패스워드가 틀렸습니다.')
# else:
#     print('계정이 존재하지 않습니다.')

# 아이디 = input('아이디 입력: ')

# if 아이디 == 'admin':
#     패스워드 = input('패스워드 입력: ')
#     if 패스워드 == 'admin':
#         print('로그인 성공')
#     else:
#         print('패스워드가 틀렸습니다.')
# else:
#     print('계정이 존재하지 않습니다.')


### 5 ###

# A = int(input('숫자를 입력해주세요: '))

# if A >= 0:
#     print('절대값은', A, '입니다.')
# else: # 파이썬에서 -A는 A*(-1)와 같음
#     print('절대값은', -A, '입니다.')

# 파이썬에 절대값 구해주는 abs() 함수도 있음


### 6 ###

# print('='*30)
# print('사과 3000원')
# print('배 2000원')
# print('='*30)

# app = int(input('구입할 사과의 개수: '))
# pear = int(input('구입할 배의 개수: '))
# mon = int(input('소지 금액: '))

# total = app*3000 + pear*2000

# if total > mon:
#     print('구매 불가')
#     print(total-mon, '원이 더 필요합니다.')
# else:
#     print('잔돈은', mon-total, '원 입니다.')


### 7 ###

# A = int(input('숫자를 입력해주세요: '))

# if A%15 == 0:
#     print('15의 배수입니다.')
# elif A%3 == 0:
#     print('3의 배수입니다.')
# elif A%5 == 0:
#     print('5의 배수입니다.')


### 8 ###

# print('='*30)
# print('1. 아메리카노')
# print('2. 카페라떼')
# print('='*30)

# menu = int(input('메뉴 선택(숫자만 입력해주세요): '))

# if menu == 1 or menu == 2:
#     if menu == 1:
#         menu = '아메리카노'
#     else:
#         menu = '카페라떼'
    
#     print('='*30)
#     print('1. ICE')
#     print('2. HOT')
#     print('='*30)

#     temp = int(input('온도 선택(숫자만 입력해주세요): '))

#     if temp == 1:
#         temp = 'ICE'
#     else:
#         temp = 'HOT'

#     print(temp, menu, '선택')    

# else:
#     print('메뉴 선택이 잘못되었습니다.')


# 강사님 풀이(온도 입력 오류까지)

# print("="*30)
# print("1. 아메리카노")
# print("2. 카페라떼")
# print("="*30)

# menu = int(input("메뉴입력 : "))

# if 1 <= menu <= 2:
#     print("="*30)
#     print("1. HOT")
#     print("2. ICE")
#     print("="*30)

#     temp = int(input("온도 입력 : "))
#     if 1 <= temp <= 2:
#         if menu == 1:
#             if temp == 1:
#                 print("따뜻한 아메리카노")
#             else:
#                 print("아이스 아메리카노")
#         else:
#             if temp == 1:
#                 print("따뜻한 카페라떼")
#             else:
#                 print("아이스 카페라떼")
#         # 정상적으로 입력
#     else:
#         print("온도입력오류!")
#         # 온도이상할때
# else:
#     print("메뉴입력오류!")
#     # 메뉴 이상할때

# pass는 아무런 역할을 하지 않음!
# 콜론 다음 종속문장 써주긴 해야되는데~
# 전체적인 뼈대잡을 때 아주아주아주아주 유용하게 쓰임



##### Level 02 실습 문제 #####

### 3 ### (오늘은 목요일로 변경)

# N = int(input('입력: '))

# if N%7 == 0:
#     print('목요일')
# elif N%7 == 1:
#     print('금요일')
# elif N%7 == 2:
#     print('토요일')
# elif N%7 == 3:
#     print('일요일')
# elif N%7 == 4:
#     print('월요일')
# elif N%7 == 5:
#     print('화요일')
# else:
#     print('수요일')


### 4 ###

# year = int(input('연도: '))

# if year%400 == 0:
#     print('윤년')
# elif year%100 == 0:
#     print('평년')
# elif year%4 == 0:
#     print('윤년')
# else:
#     print('평년')


# # 평년은 출력하지 않는 경우

# year = int(input('연도: '))

# if year%400 == 0:
#     print('윤년')
# elif year%100 == 0:
#     pass
# elif year%4 == 0:
#     print('윤년')
# else:
#     pass



##### Level 03 실습 문제 #####


### 2 ###

hr = int(input('시: '))
min_ = int(input('분: '))

if hr == 0:
    if min_ >= 30:
        min_ = min_ - 30
    else:
        hr = 23
        min_ = 60 - (30 - min_)
else:
    if min_ >= 30:
        min_ = min_ - 30
    else:
        hr = hr - 1
        min_ = 60 - (30 - min_)

print('30분 전 시간은', hr, '시', min_, '분 입니다.')


# 강사님 풀이

h = int(input('시: '))
m = int(input('분: '))

t = h * 60 + m - 30
if t < 0:
    t = t + 1440

print(t//60, '시간', t%60, '분')



##### Level 03 실습 문제 #####


### 1 ### (Level 03 2번 심화)

h = int(input('시: '))
m = int(input('분: '))
N = int(input('몇 분 전: '))

t = h * 60 + m - N%1440
if t < 0:
    t = t + 1440

print(t//60, '시간', t%60, '분')








