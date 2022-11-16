import random
import time
import os


##### 연산 게임 #####

# 1. 한 자리 수 두 개(A, B)를 랜덤으로 설정
# 2. 사용자에게 연산 문제(A + B = )를 내는 프로그램
# 3. 맞으면 "맞았습니다." 출력
#    틀리면 "틀렸습니다." 출력
# =================================================
# 4. life, score
#  - 틀리면 life -1, 맞으면 score +100
#  - life가 0이면 game over
# 5. combo
#  - 0 combo: score +100
#  - 1 combo: score +120
#  - 2 combo: score +140
#  .... 1 combo 당 score 20점씩 증가
# =================================================
# 6. 1/2 확률로 뺄셈 문제 출제
# 7. 1/5 확률로 200점짜리 문제 출제
# 8. 1/7 확률로 틀리면 life -2


# life, score, combo

life = 5
score = 0
combo = 0

while True:

    print('='*30)
    print('● '*life + '○ '*(5-life))
    print(f'{combo} COMBO!')
    print('='*30)

    A = random.randint(1, 9)
    B = random.randint(1, 9)

    user = int(input(f'{A} + {B} = '))

    if user == A + B:
        print('맞았습니다.')
        
        score += 100 + (20*combo)
        combo += 1
    
    else:
        print('틀렸습니다.')
        life -= 1
        combo = 0
        
        if life == 0:
            print(f'점수: {score}')
            break

    time.sleep(0.7)
    os.system('cls')



# 6번(뺄샘 문제) 추가

life = 5
score = 0
combo = 0

while True:

    print('='*30)
    print('● '*life + '○ '*(5-life))
    print(f'{combo} COMBO!')
    print('='*30)

    A = random.randint(1, 9)
    B = random.randint(1, 9)
    op = random.randint(1, 2) # option -> 1: 덧셈, 2: 뺄셈

    if op == 1:
        user = int(input(f'{A} + {B} = '))
        answer = A + B
    elif op == 2:
        user = int(input(f'{A} - {B} = '))
        answer = A - B

    if user == answer:
        print('맞았습니다.')
        score += 100 + (20*combo)
        combo += 1
    else:
        print('틀렸습니다.')
        life -= 1
        combo = 0
        
        if life == 0:
            print(f'점수: {score}')
            break

    time.sleep(0.7)
    os.system('cls')



# 7번(200점 문제), 8번(life -2) 추가 + 마이너스 연산결과 방지

life = 5
score = 0
combo = 0

while True:

    print('='*30)
    print('● '*life + '○ '*(5-life))
    print(f'{combo} COMBO!')
    print('='*30)

    A = random.randint(1, 9)
    B = random.randint(1, 9)
    op = random.randint(1, 2)
    s200 = random.randint(1, 5) # s200=1 -> 200점 문제 출제
    l2 = random.randint(1, 7) # l2=1 -> life -2

    if l2 == 1:
        life_loss = 2
        print('life -2 문제입니다.')
    else:
        life_loss = 1

    if s200 == 1:
        plus_score = 200
        print('score +200 문제입니다.')
    else:
        plus_score = 100

    if op == 1:
        user = int(input(f'{A} + {B} = '))
        answer = A + B
    elif op == 2:
        if A >= B:
            user = int(input(f'{A} - {B} = '))
            answer = A - B
        else:
            user = int(input(f'{B} - {A} = '))
            answer = B - A

    if user == answer:
        print('맞았습니다.')
        score += plus_score + (20*combo)
        combo += 1
    else:
        print('틀렸습니다.')
        life -= life_loss
        combo = 0
        
        if life == 0:
            print(f'점수: {score}')
            break

    time.sleep(0.7)
    os.system('cls')

# life == 0으로 설정할 경우 life가 0을 지나쳐 음수가 되면 게임이 계속 이어지는 문제 발생
# 최종 점수 print 전에 life == 0을 life <= 0으로 수정하면 문제 해결



