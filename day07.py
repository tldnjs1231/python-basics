# 수를 입력받고 1 ~ N까지 짝수의 합, 홀수의 합을 구하는 프로그램

# N = int(input('입력: '))

# even = 0
# odd = 0

# for i in range(1, N+1):
#     if i % 2 == 0:
#         even += i
#     else:
#         odd += i

# print('짝수의 합', even)
# print('홀수의 합', odd)



# 수를 입력받고 1 ~ N까지 짝수의 개수, 홀수의 개수를 구하는 프로그램

# N = int(input('입력: '))

# even = 0
# odd = 0

# for i in range(1, N+1):
#     if i % 2 == 0:
#         even += 1
#     else:
#         odd += 1

# print('짝수의 개수', even)
# print('홀수의 개수', odd)



# 수를 입력받고 1 ~ N까지 3의 배수의 합과 개수를 구하는 프로그램

# N = int(input('입력: '))

# sum_ = 0
# num = 0

# for i in range(1, N+1):
#     if i % 3 == 0:
#         sum_ += i
#         num += 1

# print('합', sum_)
# print('개수', num)


# # list 활용

# N = int(input('입력: '))

# li = []

# for i in range(1, N+1):
#     if i % 3 == 0:
#         li.append(i)

# print(sum(li), len(li))



# A-B-C-D가 번갈아가면서 청소를 하기로 했다.
# 만약 첫 날 A가 당번이라면 오늘부터 N일까지 당번을 출력해라.

# N = int(input('입력: '))

# # A, B, C, D가 들어간 리스트를 형성해주되, 1번 인덱스에 A를 위치시킴
# li = ['D', 'A', 'B', 'C']

# for i in range(1, N+1):
#     # 4로 나눈 나머지 1, 2, 3, 0이 돌아가며 li의 요소를 인덱싱
#     print(i, '일 당번은', li[i%4])

# 20 ~ 50일이 궁금하다면 for i in range(20, 51):
# 특정 날짜들이 궁금하다면 for i in [7, 13, 27, 90]:



# 2000 ~ 2999년 중 윤년의 개수를 출력하는 프로그램
# 윤년은 4의 배수이지만, 100의 배수는 아니다.
# 하지만 400의 배수는 윤년이다.

# li = []

# for i in range(2000, 3000):
#     if i % 400 == 0:
#         li.append(i)
#     elif i % 100 == 0:
#         pass
#     elif i % 4 == 0:
#         li.append(i)

# print(len(i))



##### 반복문 실습 문제 모음 #####

# Q1. 1에서 N까지 7의 배수의 합과 개수를 구하는 코드를 작성하세요.

# N = int(input('입력: '))

# li = []

# for i in range(1, N+1):
#     if i % 7 == 0:
#         li.append(i)

# print(sum(li), len(li))



# Q2. 짝수, 홀수 각각의 평균을 구해주세요.

# li = [4434, 8183, 1504, 6296, 9809, 5041, 3024, 1744, 6880, 6007, 2204, 2161, 2650, 9361, 1927, 7400, 8182, 5299, 9814, 6528, 7927, 4055, 2553, 6372, 3044, 6474, 5119, 5049, 8074, 7157, 7669, 3964, 5166, 9871, 4002, 6335, 5424, 2500, 3619, 7977, 1823, 1789, 5834, 3684, 3031, 6877, 6577, 5519, 1980, 7041, 4962, 6163, 7072, 1703, 1061, 1226, 7060, 2261, 6564, 5125, 9702, 1686, 6673, 6368, 9678, 8837, 4211, 5568, 2435, 5500, 4701, 6597, 6334, 4937, 9353, 2365, 1442, 6833, 4375, 6141, 9456, 2249, 6042, 4665, 4494, 6762, 8505, 4967, 7108, 3834, 7079, 1705, 3686, 9907, 5456, 8976, 1266, 9733, 3714, 3734]

# even = []
# odd = []

# for i in li:
#     if i % 2 == 0:
#         even.append(i)
#     else:
#         odd.append(i)

# print('짝수 평균', sum(even)/len(even))
# print('홀수 평균', sum(odd)/len(odd))



# Q3. 1에서 N까지 3의 배수의 개수와 5의 배수의 개수의 차를 구하세요.

# N = int(input('입력: '))

# mul_3 = 0
# mul_5 = 0

# for i in range(1, N+1):
#     if i % 3 == 0:
#         mul_3 += 1
#     if i % 5 == 0:
#         mul_5 += 1

# print(mul_3 - mul_5)



# Q4. 한 반 학생들의 혈액형입니다.
# A, B, AB, O 형이 각각 몇 명인지 프로그래밍 하세요.

# blood = ['O', 'O', 'O', 'O', 'AB', 'B', 'A', 'A', 'O', 'AB', 'B', 'A', 'B', 'AB', 'AB', 'AB', 'O', 'A', 'A', 'AB', 'B', 'AB', 'O', 'B', 'A', 'O', 'A', 'O', 'AB', 'O', 'AB', 'AB', 'O', 'B', 'B', 'O', 'O', 'AB', 'B', 'A']

# A = 0
# B = 0
# AB = 0
# O = 0

# for i in blood:
#     if i == 'A':
#         A += 1
#     elif i == 'B':
#         B += 1
#     elif i == 'AB':
#         AB += 1
#     else:
#         O += 1

# print('A형', A)
# print('B형', B)
# print('AB형', AB)
# print('O형', O)


# count 함수 활용

# for i in ['A', 'B', 'AB', 'O']:
#     print(i, blood.count(i))



# Q5. 현재 당신은 5000원이 있습니다.
# 편의점에 있는 물품들의 가격들이 다음과 같습니다.
# 구매가능한 물품의 개수를 구하세요.

# price = [6600, 4800, 3400, 3200, 4500, 5500, 3200, 7800, 4200, 5300, 7500, 4200, 7200, 5600, 6700, 8000, 7000, 6700, 6200, 6100, 4700, 7200, 7100, 5700, 5900, 4300, 5200, 5600, 5900, 6600, 4900, 5800, 7100, 5800, 4500, 3200, 7800, 5300, 7200, 8000]

# afford = 0

# for i in price:
#     if i <= 5000:
#         afford += 1

# print(afford)


# Q6. 한 반 학생들의 국어 점수이다.
# 80점 미만은 보충수업을 받아야 할 때, 보충수업 대상자는 몇 명일까?

# score = [66.9, 31.3, 88.3, 45.8, 82.3, 34, 60.6, 58, 78.8, 48.8, 37.3, 58.4, 65.7, 73, 34.7, 67.9, 34.9, 97.1, 39.1, 59.7, 73, 50.1, 87, 56.3, 45.4, 65.2, 81.7, 79.8, 79.1, 42.9, 96.5, 97.7, 58.2, 94.4, 96.7, 87, 73.7, 97.9, 38.6, 92, 30.5, 98.3, 91, 56.9, 45.5, 43.1, 55, 31.1, 65, 69.8, 76.2, 37, 88.8, 52.7, 68.6, 47.6, 35, 30.4, 45.5, 69.5, 58.3, 42.1, 70.2, 98.1, 34.6, 92.4, 99.8, 45.9, 92.3, 73.6, 83.7, 51.2, 38.6, 69.9, 82.7, 49.6, 59.7, 50.3, 83.2, 72.9, 32.6, 58.8, 92.5, 79.2, 72.3, 39.5, 52.7, 74.3, 79.4, 79.3, 49.7, 93.3, 43.9, 71.6, 92.9, 55.6, 97.4, 59, 66.7, 56.5]

# cnt = 0

# for i in score:
#     if i < 80:
#         cnt += 1

# print(cnt)


# Q7. 다음 수들의 절대값의 합을 구해주세요.
# (절대값은 0과 떨어져 있는 정도를 나타내는 값입니다.)

# num = [-230, -139, 154, 471, 343, -285, -272, -358, 171, 433, 492, 213, 458, -324, 266, -441, -283, 196, 452, -273, 349, -435, 256, 263, 440, -308, -338, 255, -325, 155, 429, -244, -477, -293, 265, 446, -320, 331, -371, 267, -167, 315, -224, 365, -112, 274, 338, 120, 344, -303, 203, -308, -458, -189, 100, 343, -264, -334, -227, -328, 133, 153, -259, -252, 233, -357, -122, 174, 431, -212, 128, 180, -294, -239, 208, -404, -493, 405, -238, -460, -264, -161, 187, 320, -323, 100, 473, 258, -211, -148, 187, -188, -117, -164, -122, 254, 454, -180, 377, 469]

# abs_val = []

# for i in num:
#     if i >= 0:
#         abs_val.append(i)
#     else:
#         abs_val.append(-i)

# print(sum(abs_val))



# Q8. 단을 입력받고, 구구단을 출력하는 코드를 작성하세요.(하나의 단만)
# ex)  단 입력 : 3
#      3 x 1 = 3
#      3 x 2 = 6
#         ...
#      3 x 9 = 27

# n = int(input('단 입력: '))

# for i in range(1, 10):
#     print(n, 'x', i, '=', n*i)



# (추가 심화 문제)
# o 는 1점, x 는 0점이다.
# 만약 o 가 연속으로 등장할 경우 점수가 배가 되어 계산된다고 한다.
# 하지만, 중간에 x 를 만나게 되면 배수가 끊겨버린다.
# ex) oxooxxo  >  1 + 1 + 2 + 1  > 5 점
#     xoooxoo  >  1 + 2 + 4 + 1 + 2 > 10 점
#     oooooxo  >  1 + 2 + 4 + 8 + 16 + 1 > 32 점

# ox 를 입력받고 점수를 반환하는 프로그램을 작성하세요

# ox = input('입력: ')

# if ox[0] == 'o':
#     score = [1]
# else:
#     score = [0]

# for i in range(1, len(ox)):
#     if ox[i] == 'o':
#         if ox[i-1] == 'o':
#             score.append(score[i-1]*2)
#         else:
#             score.append(1)
#     else:
#         score.append(0)

# print(sum(score))



##### for문 심화 문제 #####

# 4개의 수를 입력 받고 짝수, 홀수를 판별하는 프로그램(1)

# for i in range(4):
#     n = int(input('수 입력: '))
#     if n % 2 == 0:
#         print(n, '짝수')
#     else:
#         print(n, '홀수')



# 4개의 수를 입력 받고 짝수, 홀수를 판별하는 프로그램(2)

# num = []

# for i in range(4):
#     n = int(input('수 입력: '))
#     num.append(n)
    
# for j in num:
#     if j % 2 == 0:
#         print(j, '짝수')
#     else:
#         print(j, '홀수')



# 몇 회 입력하시겠습니까? (ppt 파일 참고)

# n = int(input('몇 회 입력하시겠습니까? '))

# for i in range(n):
    
#     a = int(input('수 입력: '))
#     b = int(input('수 입력: '))
#     op = int(input('연산자 입력(덧셈1, 뺄셈2): '))

#     if op == 1:
#         print(a, '+', b, '=', a+b)
#     elif op == 2:
#         print(a, '-', b, '=', a-b)
#     else:
#         print('입력 오류!!')
    
#     print('='*30)



# 5개의 점수를 입력받고 평균 이하의 수들을 구하는 프로그램

# score = []

# for i in range(5):
#     n = int(input('수 입력: '))
#     score.append(n)

# avg = sum(score)/len(score)

# print('5과목의 평균은', avg)

# for j in score:
#     if j <= avg:
#         print(j, '는 평균 이하')



##### 추가 문제 #####

# Q. 문자열을 입력받고, 괄호가 잘 닫혀 있는지 판단해주는 프로그램
# 예제입력1 : (()
#           잘못 닫혀있습니다.
# 예제입력2 : )()(
#           잘못 닫혀있습니다.
# 예제입력3 : (()))(
#           잘못 닫혀있습니다.
# 예제입력4 : (()(()))
#           잘 닫혀있습니다.

# 좀 더 고민해보기...
# 단순히 (와 )의 개수가 같은 것으로 판단하면 ())(() 이런 예외가 있음
# 특정 시점에 맨 앞에서부터 (의 개수가 )의 개수보다 더 많아야 할까..?

par = input('입력: ')

li = []

for i in par:

    li.append(i)

    if li.count('(') < li.count(')'):
        break

if li.count('(') == li.count(')'):
    print('잘 닫혀있습니다.')
else:
    print('잘못 닫혀있습니다.')






