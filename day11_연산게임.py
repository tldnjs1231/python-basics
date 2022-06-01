import random
import time
import os


# Q. 연산게임

# 1. 한 자리 수 두 개를 랜덤으로 받습니다~ (A,B)
# 2. 사용자에게 문제를 냅니다. A + B =
# 3. 사용자가 맞추면 "맞았습니다."
#    사용자가 틀리면 "틀렸습니다."
# ===============================================
# 4. life, score 추가
#  - 틀리면 life -1, 맞추면 score +100
#  - life 가 0 일 때 게임오버
# 5. 콤보기능추가
#  - 0 combo 는 100점
#  - 1 combo 는 120점
#  - 2 combo 는 140점
#  .... 1combo 당 20 점씩 쌓이도록
# ================================================
# 6. 1/2 확률로 뺄셈문제 출제되도록
# 7. 1/5 확률로 점수가 200 점 짜리가 출제되도록


# ~5번 코드

life = 5
score = 0
combo = 0

while True:

    print("="*30)
    print("● "*life + "○ "*(5-life))
    print(f"{combo} COMBO!")
    print("="*30)

    A = random.randint(1,9)
    B = random.randint(1,9)

    user = int(input(f"{A} + {B} = "))

    if user == A+B:
        print("맞았습니다")
        
        score += 100 + (20*combo)
        combo += 1
        

    else:
        print("틀렸습니다")
        life -= 1
        combo = 0
        
        if life == 0:
            print(f"니점수 {score}")
            break

    time.sleep(0.7)
    os.system("cls")



# ~6번 코드

life = 5
score = 0
combo = 0

while True:

    print("="*30)
    print("● "*life + "○ "*(5-life))
    print(f"{combo} COMBO!")
    print("="*30)

    A = random.randint(1,9)
    B = random.randint(1,9)
    op = random.randint(1,2) # 1 덧셈, 2 뺄셈

    if op == 1:
        user = int(input(f"{A} + {B} = "))
        정답 = A+B
    elif op == 2:
        user = int(input(f"{A} - {B} = "))
        정답 = A-B


    if user == 정답:
        print("맞았습니다")
        score += 100 + (20*combo)
        combo += 1
    else:
        print("틀렸습니다")
        life -= 1
        combo = 0
        
        if life == 0:
            print(f"니점수 {score}")
            break

    time.sleep(0.7)
    os.system("cls")



# ~7번 코드 + 연산결과 마이너스 나오는 것 방지
# + 1/7 확률로 라이프 -2

life = 5
score = 0
combo = 0

while True:

    print("="*30)
    print("● "*life + "○ "*(5-life))
    print(f"{combo} COMBO!")
    print("="*30)

    A = random.randint(1,9)
    B = random.randint(1,9)
    op = random.randint(1,2) # 1 덧셈, 2 뺄셈
    s200 = random.randint(1,5) # 1 일 때
    l2 = random.randint(1,7) # 1

    if l2 == 1:
        라이프 = 2
        print("이번문제 life - 2")
    else:
        라이프 = 1


    if s200 == 1:
        점수 = 200
        print("이번문제 score +200")
    else:
        점수 = 100



    if op == 1:
        user = int(input(f"{A} + {B} = "))
        정답 = A+B
    elif op == 2:
        if A >= B:
            user = int(input(f"{A} - {B} = "))
            정답 = A-B
        else:
            user = int(input(f"{B} - {A} = "))
            정답 = B-A


    if user == 정답:
        print("맞았습니다")
        score += 점수 + (20*combo)
        combo += 1
    else:
        print("틀렸습니다")
        life -= 라이프
        combo = 0
        
        if life == 0:
            print(f"니점수 {score}")
            break

    time.sleep(0.7)
    os.system("cls")

# 위 코드는 게임이 끝나지 않고 계속되는 문제가 있음
# 마지막 니 점수 바로 위 life == 0을 life <= 0으로 수정하면 됨

# 암기게임, 인디언포커 등으로 연습하면 좋음
# 코드 짤 때 구글링 하는 것 중요


