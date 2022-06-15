##### 반복문 탈출: break #####

# 내반복문에서 숫자 6을 만나면 break
for i in [1, 2, 3]:
    for j in [4, 5, 6]:
        if j == 6:
            break
        print(i, j)



# 짝수 출력 후 break
for i in range(1, 11):
    if i % 2 == 0:
        print(i, '짝수')
        break
else:
    print(i, '홀수')




##### while문 #####

# for문과 while문의 비교

# for문
for i in range(1, 11):
    print(i)

print('='*30)


# while문
i = 1 # A
while i < 11: # a
    print(i) # b
    i += 1 # c
# d

# A a b c a b c a b c ... a b c a d
# 이처럼 while문은 반복의 의미가 강함



# ex) 입력 받은 숫자의 단 출력

N = int(input('입력: '))

i = 1

while i < 10:
    print(f'{N} x {i} = {N*i}')
    i += 1




##### while True #####

# 특정 키(0)를 입력할 때까지 반복되도록 프로그램하세요.

while True:

    n = int(input('입력(종료 0): '))

    if n == 0:
        print('Program 종료')
        break



# 0 입력 시까지 숫자들의 합을 구하세요.

sum_ = 0

while True:

    n = int(input('입력(종료 0): '))

    if n == 0:
        print(f'숫자들의 합은 {sum_}')
        break

    sum_ += n



# 0 입력 시까지 숫자들의 평균을 구하세요.

sum_ = 0
len_ = 0

while True:

    n = int(input('입력(종료 0): '))

    if n == 0:
        avg = sum_ / len_
        print(f'숫자들의 평균은 {avg}')
        break

    sum_ += n
    len_ += 1

# for문에서는 입력, 추가, 판단의 순서로 프로그램 구성
# while문에서는 주로 입력, 판단, 추가의 순서로 구성




##### 사용자 프로그램 #####

# while문은 실제 사용자 프로그램의 큰 틀을 잡을 때 사용되므로,
# 사용자의 입장에서 발생 가능한 모든 경우를 따져보며 프로그램을 작성하는 것이 중요

# 사용자가 입력할 수 있는 값의 경우를 나누기(q 입력 시 종료)

li = []

while True:
    N = input('입력(종료 q): ')

    # 숫자가 입력되었을 때
    if N.isnumeric():
        li.append(int(N))
    
    # 문자가 입력되었을 때
    else:
        # 종료 시그널(q)
        if N == 'q':
            print('프로그램 종료')
            print(sum(li)/len(li))
            # 숫자 입력되기 전에 q를 입력할 경우
            # len(li)가 0이므로 에러가 뜸
            # 아래 코드에서 해당 에러 해결
            break
        else:
            print('숫자를 입력해주세요.')


li = []

while True:
    N = input('입력(종료 q): ')

    # 숫자가 입력되었을 때
    if N.isnumeric():
        li.append(int(N))
    
    # 문자가 입력되었을 때
    else:
        # 종료 시그널(q)
        if N == 'q':
            print('프로그램 종료')
            # 리스트를 bool값 전환할 경우, 리스트가 비어있으면 False
            # 리스트 안에 요소가 하나라도 있으면 True를 반환함
            # ex) bool([]) -> False, bool([1]) -> True
            if li: # if True: 리스트 안에 요소가 존재하는 경우
                print(sum(li)/len(li))
            else: # 리스트가 비어있는 경우
                print('입력된 숫자가 없습니다.')
            break
        # 다른 문자 입력되었을 때
        else:
            print('숫자를 입력해주세요.')




##### 사용자 프로그램 예제 #####

# Q. 종료 시까지 점수를 입력받는 프로그램을 사용자가 사용할 수 있도록 작성해주세요.

# 요구명세서
# 1) 숫자가 입력되었을 경우
#   1-1) 0에서 100까지 입력되었을 경우: 리스트에 담음
#   1-2) 그 외 범위가 입력되었을 경우: 올바른 범위를 입력하라고 안내
# 2) 문자가 입력되었을 경우
#   2-1) 종료 시그널(q)이 입력되었을 경우
#     2-1-1) 입력된 숫자가 있을 경우: 평균을 출력하고 종료
#     2-1-2) 입력된 숫자가 없을 경우: 입력된 값이 없다고 안내
#   2-2) 그 외 입력이 들어올 경우: 숫자를 입력하라고 안내

li = []

while True:
    N = input('입력(종료 q): ')

    # 1) 숫자가 입력되었을 경우
    if N.isnumeric():
        # 1-1) 0에서 100까지 입력되었을 경우
        if 0 <= int(N) <= 100:
            li.append(int(N))
        # 1-2) 그 외 범위가 입력되었을 경우
        else:
            print('0에서 100까지의 숫자를 입력해주세요.')
    
    # 2) 문자가 입력되었을 경우
    else:
        # 2-1) 종료 시그널(q)이 입력되었을 경우
        if N == 'q':
            # 2-1-1) 입력된 숫자가 있을 경우
            if li:
                print(sum(li)/len(li))
            # 2-1-2) 입력된 숫자가 없을 경우
            else:
                print('입력된 값이 없습니다.')
            break
        # 2-2) 그 외 입력이 들어올 경우
        else:
            print('숫자를 입력하세요.')
    

    
    
    
    

