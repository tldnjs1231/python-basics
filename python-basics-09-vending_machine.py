##### 자판기 프로그램 #####

# 현재 금액보다 주문한 음료의 가격이 비쌀 경우 금액 부족 메시지 출력
# 종료 시 현재 금액이 남아 있다면 반환
# 세 번 연속 입력 오류 발생 시 프로그램 종료


# import: 다른 파일의 클래스, 함수, 변수를 현재 파일에서 사용할 수 있도록 해주는 구문
# 기존 python 내장 함수 외에도 다양한 함수 사용 가능

# time, os 함수의 기능을 가져와 사용
import time
import os



# 자판기 코드

menu = [0, '콜라', '사이다', '커피']
price = [0, 300, 300, 200]
money = 0
errcnt = 0


while True:
    
    print('---- Menu ----')
    print('1. 콜라 / 300')
    print('2. 사이다 / 300')
    print('3. 커피 / 200')
    print('4. 돈 넣기')
    print('5. 잔돈 반환')
    print('6. 종료')
    print('-'*14)
    
    print(f'현재 금액 {money}')
    n = input('메뉴 선택 : ')
    print()

    if n.isnumeric():
        
        if 1 <= int(n) <= 3:
            errcnt = 0
            if money == 0:
                print('돈을 넣어주세요.')
            else:
                if money >= price[int(n)]:
                    print(f'{menu[int(n)]} 맛있게 드세요!')
                    money -= price[int(n)]
                else:
                    print('금액이 부족합니다.')
        
        elif int(n) == 4:
            errcnt = 0
            m = input('돈을 넣어주세요. : ')
            if m.isnumeric():
                money += int(m)
            else:
                print('금액만 입력해주세요.')
        
        elif int(n) == 5:
            errcnt = 0
            if money == 0:
                print('잔돈이 없습니다.')
            else:
                print('잔돈이 반환됩니다.')
                money = 0
        
        elif int(n) == 6:
            errcnt = 0
            if money != 0:
                print('잔돈이 반환됩니다.')
                money = 0
            break
        else:
            errcnt += 1
            if errcnt == 3:
                print('3회 연속 잘못 입력하셨습니다.')
                print('프로그램이 종료됩니다.')
                break
            print('1에서 6까지의 숫자를 입력해주세요.')

        time.sleep(1.5) # 1.5초 만큼 코드 실행 일시중지
        os.system("cls") # 화면 갱신, 현재 화면을 지움
    
    else:
        errcnt += 1
        if errcnt == 3:
                print('3회 연속 잘못 입력하셨습니다.')
                print('프로그램이 종료됩니다.')
                break    
        print('숫자를 입력해주세요.')
        
        time.sleep(1.5)
        os.system("cls")
    






