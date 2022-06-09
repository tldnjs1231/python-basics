A = [1, 2, 3]
B = (1, 2, 3)

print(type(A))
print(type(B))



# B, C의 경우 소괄호 안에 자료가 하나 뿐이면 튜플로 인식하지 않음
# 튜플로 인식하도록 하려면 뒤에 D처럼 뒤에 ,를 붙여주면 됨

A = [1]
B = (1)
C = ('apple')
D = ('apple',)

print(type(A))
print(type(B))
print(type(C))
print(type(D))



hero = ["1. 아이언맨", "2. 스파이더맨"]

print(hero)
user = int(input("영웅선택 : "))

print(hero[user-1])
# 사용자가 입력하는 값과 실제 인덱스가 다르므로 -1 해주어야 함



##### 1 #####
# 1에서부터 입력 받은 수(N)까지 출력하는 프로그램

N = int(input('입력: '))

for i in range(1, N+1):
    print(i)



##### 2 #####
# N부터 1까지 출력하는 프로그램

# N = int(input('입력: '))

# for i in range(N, 0, -1):
#     print(i)

# step 부분에 -1을 꼭 붙여줘야 함, 디폴트 값이 1이므로 그냥 두면 안됨
# list(range(10, 1)), list(range(1, 10, -1)) 둘 다 빈 리스트 반환됨


# 입력 받은 두 수(A, B) 사이의 수를 모두 출력하는 프로그램

# A = int(input('첫 번째 숫자: '))
# B = int(input('두 번째 숫자: '))

# if A >= B:
#     for i in range(A-1, B, -1):
#         print(i)
# else:
#     for i in range(A+1, B):
#         print(i)


# 1부터 100까지의 합 구하기

# sum_ = 0

# for i in range(1, 101):
#     sum_ += i

# print(sum_)


# 1부터 N까지의 합 구하는 프로그램

# N = int(input('입력: '))

# sum_ = 0

# for i in range(1, N+1):
#     sum_ += i

# print(sum_)


# Factorial 프로그램: N! = N * N-1 * N-2 * ... * 1

# N = int(input('입력: '))

# fact = 1

# for i in range(1, N+1):
#     fact *= i

# print(fact)


# 1에서 N까지의 짝수, 홀수 판별

# N = int(input('입력: '))

# for i in range(1, N+1):
#     if i%2 == 0:
#         print(i, '짝수')
#     else:
#         print(i, '홀수')


# 퇴근 문제

# 1에서 입력 받은 숫자 N까지 이어 적는다고 했을 때 총 길이를 구하세요.
# ※ len(문자열) > len 안에 문자열이 올 경우, 문자열의 길이가 반환됩니다!!

# ex) 수 입력 : 12
#     123456789101112
#     길이는 15 입니다.

# ex) 수 입력 : 15
#     123456789101112131415
#     길이는 21 입니다.

N = int(input('입력: '))

num = ''

for i in range(1, N+1):
    num += str(i)

print('길이는', len(num), '입니다.')

