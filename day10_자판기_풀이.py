import random  # random 의 기능을 가져온다!!
import time    # time 의 기능을 가져온다!!
import os      # os 의 기능을 가져온다!!

# random.randint(A,B) A부터 B까지 랜덤 수 반환
# time.sleep(x)       x 초만큼 코드를 잠시 멈춤
# os.system("cls")    화면을 갱신해줌~~




money = 0
errcnt = 0

while True:
    # 메뉴출력
    print("="*30)
    print("1. 콜라/300")
    print("2. 돈 넣기")
    print("3. 잔돈반환")
    print("4. 종 료")
    print("="*30)
    print(f"현재금액 {money}")

    # 선택받고
    menu = input("MENU > ")
    
    # 처리
    if menu == "1":
        errcnt = 0
        if money >= 300:
            money -= 300
            print("콜라 맛있게 드세요")
        else:
            print("구매 불가능!!")

    elif menu == "2":
        errcnt = 0
        m = input("돈을 넣어주세요 : ")
        if m.isnumeric():
            m = int(m)
            money += m
        else:
            print("숫자를 입력해주세요 !")

    elif menu == "3":
        errcnt = 0
        if money:
            print(f"{money} 가 반환됩니다 !")
            money = 0
        else:
            print("투입된 금액이 없습니다 !")

    elif menu == "4":
        errcnt = 0
        if money:
            print(f"{money} 챙겨가세요~~")
        break
    else:
        errcnt += 1
        if errcnt == 3:
            print("장난하지마~")
            break
        print("입력오류!!")
        
    time.sleep(0.5)
    os.system("cls")




    