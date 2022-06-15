import turtle as t
from random import randint as ri


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




##### 글자 출력 #####

t.ht()
t.pu()
t.speed(0)

t.colormode(255) # 색상 RGB로 조정하도록 설정
# t.color(100, 100, 100) # RGB 색상 설정
t.setup(900, 600) # 창의 가로 세로 길이 설정
# t.goto(0, 0) # x, y로 커서 이동
# 거북이 기본 위치 (0, 0)
# 따라서 t.setup(900, 600)의 경우 x축 값은 -450~450 존재
# t.write('hello', font=('맑은고딕', 30, 'bold'))
# t.write(적을문자, font=(글씨체, 크기, 속성))
# 글자는 현재 거북이 위치에서 오른쪽, 위 방향으로 출력됨
# 따라서 이를 고려해 오른쪽, 위쪽에 여백을 남겨놓고 t.goto 설정해야 함



# 실습1: Hello world 를 위치 랜덤하게 2000번 출력하기

# for i in range(2000):
#     t.goto(ri(-420, 380), ri(-280, 240)) # 위치 이동
#     t.write('Hello world', font=('맑은고딕', 30, 'bold')) # 출력



# 실습2: Hello world 를 위치, 색상 랜덤하게 2000번 출력하기

# for i in range(2000):
#     t.color(ri(0, 255), ri(0, 255), ri(0, 255)) # 색상 설정
#     t.goto(ri(-420, 380), ri(-280, 240)) # 위치 이동
#     t.write('Hello world', font=('맑은고딕', 30, 'bold')) # 출력



# 실습3: BTS - Dynamite 가사 빈도수 분석
# 많이 등장하는 단어일수록 크게 보이도록 프로그래밍

from day15_dynamite import di

for i in di:
    t.color(ri(0, 255), ri(0, 255), ri(0, 255))
    t.goto(ri(-420, 350), ri(-280, 240))
    t.write(i, font=('맑은고딕', (di[i]+4)*3, 'bold'))


t.mainloop() # turtle 창 유지(default: 코드 실행 후 창 닫기)
t.exitonclick() # 클릭 시 창 닫기




# 다이너마이트 가사 빈도수 분석이랑 이 뒷부분 녹강 확인



