import random
import time
import os

# a 함수 import 할 때 파일 이름 a로 설정하지 말기
# ex) import random 할 경우 random.py 하면 안 됨

# random.randint(A, B): A에서 B까지 랜덤 수 반환


##### 게임 만들기 #####

# Q. 홀짝 맞추기 게임

# # 1. 랜덤으로 두 자리 수를 받는다.
# com = random.randint(10, 99)

# # 2. 사용자에게 홀짝을 입력 받는다.
# user = int(input('홀(1)? 짝(0)?: '))

# # 3. 사용자가 맞추면 "맞았습니다"
# #    틀리면 "틀렸습니다" 라고 해준다.
# if com % 2 == user:
#     print('맞았습니다')
# else:
#     print('틀렸습니다')


# while문 활용

# life = 5
# score = 0

# while True:

#     # 현재 상태 출력
#     print('='*30)
#     print('♥ '*life + '♡ '*(5-life))
#     print('='*30)

#     com = random.randint(10, 99)

#     # 숫자로 입력 받는 것이 프로그램 돌려볼 때 편함
#     # 프로그래머가 돌려볼 때 결과 확인이 편하게 받는 것이 좋음
#     user = int(input('홀(1)? 짝(0)?: '))

#     # 판단
#     if com % 2 == user:
#         print('맞았습니다')
#         score += 100
#     else:
#         print('틀렸습니다')
#         life -= 1

#         if life == 0:
#             print(f'점수: {score}')
#             break
    
#     #time.sleep(0.7)
#     input('\n\n[Enter]') # 사용자가 Enter 치면 화면 갱신
#     os.system('cls')



# Q. UP DOWN 게임

# 1. 랜덤으로 한자리수를 받는다. (com)
# 2. 사용자에게 입력을 받는다 (user)
# 3. user 가 com 보다 크면 "Down"
#    com 이 user 보다 크면 "Up"
#    맞추면 "Correct!!"
# ========================================
# 4. 맞췄을 때 시도한 횟수 출력되게 만들기
# 5. 난이도 선택받도록 만들기
#    - HARD (100~999)
#    - NORM (10~99)
#    - EASY   (1~9)
# 6. 다시하시겠습니까? 구현하기
# ==========================================
# 7. 바보 같은 입력 시 cnt 를 2개 증가시키기
#   ex) 예를 들어 50 에서 UP 이 나왔는데 30 을 입력한 상황
#        50 에서 DOWN 이 나왔는데 70 을 입력한 상황


while True:

    # 문제 출제

    while True:

        print('='*30)
        print('1. HARD (100~999)')
        print('2. NORM (10~99)')
        print('3. EASY (1~9)')
        print('='*30)
        print()
        
        level = int(input('난이도 선택(번호 입력): '))

        if level == 1:
            com = random.randint(100, 999)
        elif level == 2:
            com = random.randint(10, 99)
        elif level == 3:
            com = random.randint(1, 9)
        else:
            print("1부터 3까지의 난이도를 선택해주세요.")
            time.sleep(0.5)
            os.system('cls')
            continue
        break

    time.sleep(0.5)
    os.system('cls')

    cnt = 0


    # 게임 플레이

    while True:

        cnt += 1
        user = int(input(f'{cnt}번째 Guess: '))
        print()

        if user > com:
            print('Down')
            time.sleep(1)
            os.system('cls')
        elif user < com:
            print('Up')
            time.sleep(1)
            os.system('cls')            
        else:
            print('Correct!')
            print(f'{cnt}번 만에 맞췄습니다!')
            break

    time.sleep(0.5)
    os.system('cls')


    # 다시 하시겠습니까?

    while True:

        again = input('다시 하시겠습니까? (y/n): ')
        
        if again == 'y' or again == 'n':
            break
        else:
            print('y나 n을 입력해주세요.')
            time.sleep(0.5)
            os.system('cls')

    if again == 'n':
        break



# 7번 조건 아직 구현 안됨


