##### time, os 모듈 활용 #####

import time
import os

# time.sleep(x): x초 만큼 코드 실행 중지
# os.system('cls'): 화면 갱신


### 1 ###

st = '안녕하세요~ 미니 자판기입니다!'

for i in st:
    print(i, end='')
    time.sleep(0.1)


### 2 ###

for i in range(100):
    print('ε='*i, end='')

    if i % 2 == 0:
        print('┌( ﾟДﾟ)┘')
    else:
        print('└( ﾟДﾟ)┐')
    
    time.sleep(0.1)
    os.system("cls")




