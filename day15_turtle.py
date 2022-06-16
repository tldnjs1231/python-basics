import turtle as t


t.shape('turtle') # 커서 모양 설정
t.color('red') # 커서 색상 설정


print(t.getshapes()) # 설정 가능한 커서 모양 list

# 설정 가능한 커서 모양 직접 확인
for i in t.getshapes():
    t.shape(i)
    input(i) # enter 누르면 다음 모양으로 이동


t.pensize(7) # 펜 두께 설정(7 정도가 적당)
t.speed(0) # 이동 속도 설정(0~1, 0에 가까울수록 빠름)

t.pu() # pen up: 펜을 든다
t.pd() # pen down: 펜을 내린다
t.ht() # hide turtle: 펜 숨김
t.st() # show turtle: 펜 드러냄

t.fd() # 머리 방향으로 100 픽셀 만큼 이동
t.lt() # 왼쪽으로 90도 회전
t.rt() # 오른쪽으로 90도 회전

t.mainloop() # turtle 창 유지(default: 코드 실행 후 창 닫기)
t.exitonclick() # 클릭 시 창 닫기



##### 도형 그리기 예제 #####

# 1. 삼각형
for i in range(3):
    t.fd(100)
    t.lt(120)


# 2. 사각형
for i in range(4):
    t.fd(100)
    t.lt(90)


# 3. 오각형
for i in range(5):
    t.fd(100)
    t.lt(72)


# 4. N각형
N = int(input('N각형: '))
for i in range(N):
        t.fd(100)
        t.lt(360/N)


# 5. 3~9각형
for N in range(3, 10):
    for i in range(N):
        t.fd(100)
        t.lt(360/N)


# 6. 별
for i in range(5):
    t.fd(100)
    t.rt(144)


# 7. 원
t.circle(50) # 반지름이 50 픽셀인 원을 반시계 방향으로 그림
t.dot(100, 'blue') # 현재 펜의 위치를 중심으로 지름 100 픽셀의 원을 그림 (default: pencolor)




##### 글자 출력: word cloud #####

t.colormode(255) # 색상을 문자열('red')이 아닌 RGB로 조정하도록 설정
# t.color(100, 100, 100) # RGB 색상 설정

t.setup(900, 600) # 창의 가로 세로 길이 설정
# word cloud 출력되기 적당한 크기 설정

t.goto(0, 0) # x, y로 커서 이동
# 거북이 기본 위치 (0, 0)
# t.setup(900, 600)의 경우 x축 값은 -450~450, y축 값은 -300~300 존재

t.write('hello', font=('맑은고딕', 30, 'bold'))
# t.write(적을문자, font=(글씨체, 크기, 속성))
# 글자는 현재 거북이 위치에서 오른쪽, 위 방향으로 출력
# 이를 고려해 글자가 잘리지 않도록 오른쪽, 위쪽에 여백을 남겨놓고 t.goto 위치 설정



# 글자 출력 실습 전 세팅

import turtle as t
from random import randint as ri

t.ht() # 커서가 보이지 않도록
t.pu() # 글자 출력을 위해 커서가 움직일 때 동선이 남지 않도록
t.speed(0)

t.colormode(255)
t.setup(900, 600)



# 실습1: hello를 위치 랜덤하게 2000번 출력하기

for i in range(2000):
    t.goto(ri(-420, 380), ri(-280, 240)) # 위치 이동: 오른쪽, 위쪽에 여백을 더 많이
    t.write('hello', font=('맑은고딕', 30, 'bold')) # 글자 출력



# 실습2: hello를 위치, 색상 랜덤하게 2000번 출력하기

for i in range(2000):
    t.color(ri(0, 255), ri(0, 255), ri(0, 255)) # 색상 랜덤 설정
    t.goto(ri(-420, 380), ri(-280, 240)) # 위치 랜덤 이동
    t.write('hello', font=('맑은고딕', 30, 'bold')) # 글자 출력



# 실습3: BTS - Dynamite 가사 빈도수 분석
# 많이 등장하는 단어일수록 크게 보이도록 프로그래밍

from day15_dynamite import dic

for i in dic:
    t.color(ri(0, 255), ri(0, 255), ri(0, 255))
    t.goto(ri(-420, 350), ri(-280, 240))
    t.write(i, font=('맑은고딕', (dic[i]+4)*3, 'bold'))


# 글자 크기를 (d[i]+4)*3로 설정한 이유:
# 빈도수 d[i]로 설정할 경우 빈도의 편차가 너무 커서 특정 글자 몇 개만 잘 보임
# 작게 출력되는 글자도 잘 보이도록 하기 위해 *3을 하는데,
# 편차를 줄이기 위해 +4를 먼저 실행
# 꼭 3, 4일 필요는 없고, 적절한 숫자를 찾아 적용

# ex)
# 1회 x 86 = 86회
# (1 + 4) * 2 = 10
# (86 + 4) * 2 = 180
# 10회 x 18 = 180회
# 덧셈을 해주면 86배에서 18배로 크게 줄어든 것 확인 가능



# 실습4: 가사 빈도수 분석 문제에 장치 설정
# 1) enter 누르면 출력 시작
# 2) 1초에 다섯 단어 출력
# 3) 한 번만 등장한 단어는 출력하지 않음

from day15_dynamite import dic
from time import sleep

input()
num = 0 # 출력되는 단어의 개수

for i in dic:
    
    # 단어가 한 번만 등장한 경우 continue
    if dic[i] == 1:
        continue
    
    # 단어 다섯 개 출력될 때마다 1초 정지
    if num % 5 == 0:
        sleep(1)
    
    # 출력하기 전에 글자 수 하나씩 증가
    num += 1
    
    t.color(ri(0, 255), ri(0, 255), ri(0, 255))
    t.goto(ri(-420, 350), ri(-280, 240))
    t.write(i, font=('맑은고딕', (dic[i]+4)*3, 'bold'))






