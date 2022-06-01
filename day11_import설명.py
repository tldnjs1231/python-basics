##### import #####

import random # random의 기능을 가져온다!
import time # time의 기능을 가져온다!
import os # os의 기능을 가져온다!

# random.randint(A, B): A부터 B까지 랜덤 수 반환
# time.sleep(x): x초 만큼 코드를 잠시 멈춤
# os.system('cls'): 화면을 갱신


st = '안녕하세요~ 미니 자판기입니다.'

for i in st:
    print(i, end='')
    time.sleep(0.1)


for i in range(100):
    print("ε="*i, end="")
    if i % 2 == 0:
        print("┌( ﾟДﾟ)┘")
    else:
        print("└( ﾟДﾟ)┐")
    time.sleep(0.1)
    os.system("cls")




