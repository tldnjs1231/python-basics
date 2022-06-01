##### 함수 #####

# 두 수의 합을 구해주는 함수

# # 선언 부분
# def hap(x, y):
#     num = x + y
#     return num

# # 사용 부분
# x = hap(10, 20)
# print(x)



# 두 수의 차이를 구해주는 함수

# def cha1(x, y):
#     num = abs(x - y)
#     return num

# def cha2(x, y):
#     if x >= y:
#         num = x - y
#     else:
#         num = y - x
#     return num

# x = cha1(10, 20)
# print(x)



# 약수 구해주는 함수

# def div(x):
    
#     L = []

#     for i in range(1, x+1):
#         if x % i == 0:
#             L.append(i)
    
#     return L

# print(div(6))



# 짝수인지 판단하는 코드
# jjak(10)   > True
# jjak(9)    > False

# def jjak(x):
#     if x % 2 == 0:
#         return True
#     else:
#         return False

# print(jjak(10), jjak(9))


# # 함수 활용

# N = int(input())
# if jjak(N):
#     print(N, '짝수다')



# 각 자리가 홀수로만 이루어진 수인지 판단하는 함수

# def odd_only(x):
#     for i in str(x):
#         if int(i) % 2 == 0:
#             return False
#     return True

# def hol1(x):
#     x = str(x)
#     cnt = 0
#     for i in x:
#         if int(i) % 2:
#             cnt += 1
#     if len(x) == cnt:
#         return True
#     return False

# def hol2(x):
#     x = str(x)
#     for i in x:
#         if int(i) % 2 == 0:
#             return False
#     return True


# # 함수 활용

# for i in li:
#     if hol2(i):
#         print(i) 



# 소수인지 판단해주는 함수
# 2에서 x-1까지 나눠지면 소수가 아닌 것(False 반환)

# def sosu(x):
#     for i in range(2, x):
#         if x % i == 0:
#             return False
#     return True



# 파일 이름을 입력받고 유효하게 바꿔주는 함수
# / \ " ? : * < > |

# def file_name(x):
#     for i in '\/"?:*<>|':
#         x = x.replace(i, '')
#     return x



# (참고) 유효값 입력받는 함수
# 문구, 최소, 최대

# import os
# import time

# def 유효값입력(문구, 최소, 최대):
#     while True:
#         user = input(문구)
#         if user.isnumeric():
#             user = int(user)
#             if 최소 <= user <= 최대:
#                 return user
#             else:
#                 print(f"{최소} 에서 {최대} 까지만 입력바람!")
#         else:
#             print("숫자입력해주세요 ~ ")
#         time.sleep(0.7)
#         os.system("cls")

# kor = 유효값입력("kor : ", 0, 100)
# math = 유효값입력("math : ", 0, 100)
# sci = 유효값입력("sci : ", 0, 100)



# 장문의 문자열을 입력받고, 문자열이 30글자 이상일 때는 앞에서 30글자까지만 출력한 뒤 생략기호("...")를 뒤에 추가해주고, 아닐 경우 그냥 문자열을 출력해주는 함수

# def 요약(x):
#     cnt = 0
#     for i in x:
#         cnt += 1
#     if cnt <= 30:
#         return x
#     else:
#         return x[:30] + ' ...'

# print(요약("abcd"))
# print(요약("abcdefghijklmnopqrstuvwxyz0123456789"))



##### 클래스 #####

# 클래스는 객체를 생성하기 위해서 만든다!
# 클래스로 속성을 모아놓으면 객체 생성하면서 바로 적용됨

class 모험가:
    
    # 필드: 클래스 안의 변수
    힘 = 10
    빠르기 = 100
    민첩 = 10
    항마력 = 100
    점프력 = 100
    인벤 = []
    닉네임 = ""

    # 매서드: 클래스 안의 함수
    def 걷는다():
        pass
    def 달팽이세마리():
        pass
    def 뛴다():
        pass

# A는 객체, A는 모험가 class의 인스턴스 (o)
# A는 인스턴스, A는 모험가 class의 객체 (x)
A = 모험가()


# 클래스와 함수의 구분
# 사용할 때 클래스와 함수의 형태가 비슷해 구분이 어려우므로
# 클래스는 무조건 첫 글자를 대문자로 해주기로 개발자들끼리 약속

class Maple:
    pass

def add():
    pass

A = Maple()
B = add()



