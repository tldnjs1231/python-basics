##### Level 01 실습 문제 #####

##### 1 #####
# 수학, 과학 성적을 입력받고, 
# 평균이 90점 이상이면 A,
# 평균이 80점 이상이면 B,
# 평균이 70점 이상이면 C,
# 나머지는 D가 출력되는 프로그램

math = float(input('수학 점수: '))
sci = float(input('과학 점수: '))

avg = (math + sci)/2

if avg >= 90:
    print('A')
elif avg >= 80:
    print('B')
elif avg >= 70:
    print('C')
else:
    print('D')



##### 2 #####
# 두 수와 연산자를 입력받고 사칙연산 결과를 출력하는 프로그램
# (연산자에 이상한 값이 들어가면 "연산자가 이상해요" 출력)

n1 = float(input('첫 번째 숫자: '))
n2 = float(input('두 번째 숫자: '))
op = input('연산자(+, -, *, / 중 하나를 입력해주세요): ')

if op == '+':
    print(n1 + n2)
elif op == '-':
    print(n1 - n2)
elif op == '*':
    print(n1 * n2)
elif op == '/':
    print(n1 / n2)
else:
    print('연산자가 이상해요')


    
##### 3 #####
# 달을 입력받고 계절을 출력하는 프로그램
# ex1) 월: 1
#      1 월은 겨울입니다!
# ex1) 월: 13
#      입력이 바르지 않습니다.

month = int(input('월: '))


# 논리 연산자 or 사용
if month == 3 or month == 4 or month == 5:
    print(month, '월은 봄입니다!')
elif month == 6 or month == 7 or month == 8:
    print(month, '월은 여름입니다!')
elif month == 9 or month == 10 or month == 11:
    print(month, '월은 가을입니다!')
elif month == 12 or month == 1 or month ==2:
    print(month, '월은 겨울입니다!')
else:
    print('입력이 바르지 않습니다.')


# 부등호 사용
if 3 <= month <= 5:
    print(month, '월은 봄입니다!')
elif 6 <= month <= 8:
    print(month, '월은 여름입니다!')
elif 9 <= month <= 11:
    print(month, '월은 가을입니다!')
elif 1 <= month <= 12:
    # 위에서 3~11월 중 하나에 해당될 경우 어차피 조건문 실행이 종료되므로,
    # 3~11을 포함한 1 이상 12 이하를 조건으로 설정해도 무방함
    print(month, '월은 겨울입니다!')
else:
    print('입력이 바르지 않습니다.')


# 조건문의 중첩
if 1 <= month <= 12:
   if 3 <= month <= 5:
       print(month, '월은 봄입니다!')
   elif 6 <= month <= 8:
       print(month, '월은 여름입니다!')
   elif 9 <= month <= 11:
       print(month, '월은 가을입니다!')
   else:
       print(month, '월은 겨울입니다!')
else:
    print('입력이 바르지 않습니다.')



##### 4 #####

# 아이디, 패스워드를 모두 입력받은 후 admin 계정 판별
아이디 = input('아이디 입력: ')
패스워드 = input('패스워드 입력: ')

if 아이디 == 'admin':
    if 패스워드 == 'admin':
        print('로그인 성공')
    else:
        print('패스워드가 틀렸습니다.')
else:
    print('계정이 존재하지 않습니다.')


# 아이디가 admin인 경우에만 패스워드 입력
아이디 = input('아이디 입력: ')

if 아이디 == 'admin':
    패스워드 = input('패스워드 입력: ')
    if 패스워드 == 'admin':
        print('로그인 성공')
    else:
        print('패스워드가 틀렸습니다.')
else:
    print('계정이 존재하지 않습니다.')



##### 5 #####
# 수(A) 를 입력받고 절댓값을 출력하는 프로그램
# ex1) 수: -3
#      절댓값은 3 입니다.
# ex1) 수: 4
#      절댓값은 4 입니다.

A = int(input('숫자를 입력해주세요: '))

if A >= 0:
    print('절댓값은', A, '입니다.')
else:
    print('절댓값은', -A, '입니다.')
    # 파이썬에서 -A는 A*(-1)와 동일

# 참고) 파이썬에는 절댓값을 구해주는 abs() 함수가 존재함



##### 6 #####
# 구입할 사과(3000), 배(2000)의 개수와 현재 소지 금액을 입력 받고,
# 1) 구매가 가능한 경우 잔돈이 얼마인지 출력
# 2) 구매가 불가능한 경우 “구매 불가” 메시지와 구매가 가능하기 위해 필요한 추가 금액 출력

print('='*30)
print('사과 3000원')
print('배 2000원')
print('='*30)

app = int(input('구입할 사과의 개수: '))
pear = int(input('구입할 배의 개수: '))
mon = int(input('소지 금액: '))

total = app*3000 + pear*2000

if total > mon:
    print('구매 불가')
    print(total-mon, '원이 더 필요합니다.')
else:
    print('잔돈은', mon-total, '원 입니다.')



##### 7 #####
# 수(A)를 입력받고 배수를 판별하는 프로그램
# A가 3의 배수이면 “3의 배수입니다.”
# A가 5의 배수이면 “5의 배수입니다.”
# A가 15의 배수이면 “15의 배수입니다.”

A = int(input('숫자를 입력해주세요: '))

if A%15 == 0:
    print('15의 배수입니다.')
elif A%3 == 0:
    print('3의 배수입니다.')
elif A%5 == 0:
    print('5의 배수입니다.')



##### 8 #####
# 미니 자판기

print('='*30)
print('1. 아메리카노')
print('2. 카페라떼')
print('='*30)

menu = int(input('메뉴 선택(숫자만 입력해주세요): '))

if 1 <= menu <= 2:
    if menu == 1:
        menu = '아메리카노'
    else:
        menu = '카페라떼'
    
    print('='*30)
    print('1. ICE')
    print('2. HOT')
    print('='*30)

    temp = int(input('온도 선택(숫자만 입력해주세요): '))
    
    if 1 <= temp <= 2:
        if temp == 1:
            temp = 'ICE'
        else:
            temp = 'HOT'
            
        print(temp, menu, '선택')
    
    else:
    print('온도 선택이 잘못되었습니다.')        

else:
    print('메뉴 선택이 잘못되었습니다.')


# 중첩 제어문의 전체적인 뼈대를 잡을 때 pass가 유용하기 쓰임
# ':' 다음의 종속문장에 대한 고민이 필요할 때,
# 아무런 역할을 하지 않는 pass를 임시로 종속문장에 넣어주면 코드를 실행해보면서 수정하기 편함




##### Level 02 실습 문제 #####

##### 1 #####
# 오늘이 목요일이라면 N일 후는 무슨 요일인지 출력

N = int(input('입력: '))

if N%7 == 0:
    print('목요일')
elif N%7 == 1:
    print('금요일')
elif N%7 == 2:
    print('토요일')
elif N%7 == 3:
    print('일요일')
elif N%7 == 4:
    print('월요일')
elif N%7 == 5:
    print('화요일')
else:
    print('수요일')



##### 2 #####
# 연도를 입력 받고 해당 연도가 윤년인지 평년인지 판별하는 프로그램

year = int(input('연도: '))

if year%400 == 0:
    print('윤년')
elif year%100 == 0:
    print('평년')
elif year%4 == 0:
    print('윤년')
else:
    print('평년')


# 평년은 출력하지 않는 경우
year = int(input('연도: '))

if year%400 == 0:
    print('윤년')
elif year%100 == 0:
    pass
elif year%4 == 0:
    print('윤년')
else:
    pass




##### Level 03 실습 문제 #####

##### 1 #####
# 시, 분을 입력 받고 30분 전 시간을 출력해주는 프로그램

# 풀이 1)
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


# 풀이 2)
hr = int(input('시: '))
min_ = int(input('분: '))

total_min = hr * 60 + min_ - 30

if total_min < 0:
    total_min = total_min + 1440
    # 하루 24시간을 분으로 환산하면 1440분

print('30분 전 시간은', total_min//60, '시', total_min%60, '분 입니다.')


# 심화: 몇 분 전 시간을 출력할지 입력을 받는 프로그램
hr = int(input('시: '))
min_ = int(input('분: '))
N = int(input('몇 분 전: '))

total_min = hr * 60 + min_ - N%1440

if total_min < 0:
    total_min = total_min + 1440

print(N, '분 전 시간은', total_min//60, '시', total_min%60, '분 입니다.')





