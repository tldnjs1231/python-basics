##### set #####

# set 자료형은 중괄호 사용
s1 = {1, 2, 3, 4}
print(type(s1))



# set 자료형의 특징

# 1. 중복이 없는 자료형
li = [1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2]
print(set(li))


# 2. 순서가 없는 자료형
st = "abcdabcdabcdasdfsdfsdfhjsdjflksdjflsdkfjsklj"
for i in range(10):
    print(set(st))


# 3. 집합 연산에 용이
li1 = [1, 2, 3, 4, 5]
li2 = [3, 4, 5, 6, 7]

# 교집합 &
print(set(li1) & set(li2))

# 합집합 |
print(set(li1) | set(li2))

# 차집합 -
print(set(li) - set(li2))



# 자료 추가 add
s = {1, 2}
for i in range(100):
    s.add(3) # set는 중복이 없는 자료형이므로 3은 한 번만 추가됨
print(s)


# 자료 삭제 remove
s.remove(3)
print(s)



# set 활용 예시
li = [1, 2, 3, 4, 1, 2, 3, 4, 1, 1, 1, 2, 1, 1]

for i in li:
    print(f'{i}의 등장횟수 = {li.count(i)}')

print('='*30)

for i in set(li):
    print(f'{i}의 등장횟수 = {li.count(i)}')




##### dictionary #####

# {key : value}
# dictionary 자료형을 사용할 때 헷갈리지 않도록
# key, value에 각각 어떤 값이 들어가는지 주석으로 메모하는 것이 좋음


# 중괄호 사용: set, dictionary

# 빈 자료형 생성
s = set()
d1 = {}
print(type(d1))
print(type(s))



# 키 인덱싱(dictionary) vs. 인덱싱(list, str)

# 키 인덱싱: key 값을 이용하여 value 값에 접근
d1 = {1:'one', 2:'two', '3':'three'}

print(d1[1])
print(d1['3'])

d1[1] = '일'
print(d1)


# 인덱싱: 인덱스를 이용하여 자료에 접근
li = [10, 20, 30]
print(li[0])

li[0] = 'ten'
print(li)



# 기본단위 in iter
# iter 안에 기본단위 존재하면 True, 아니면 False

print('one' in {1:'one'}) # False
print(1 in {1:'one'}) # True



# 예제) 사용자가 새로운 단어를 입력할 때만 사전에 추가해주는 프로그램
# 이미 있는 단어인 경우 '단어가 이미 존재합니다.' 출력

dic = {'apple':'사과', 'banana':'바나나'}

user = input('추가할 단어 입력: ')

if user in dic:
    print('단어가 이미 존재합니다.')
else:
    k = input(f'{user} 의 뜻은?')
    dic[user] = k

print(dic)



# dictionary 자료 삭제

dic = {'apple':'사과', 'banana':'바나나'}

del dic['apple']

print(dic)



# for문의 iter에 dictionary 사용
# 변수 i에 key 값이 차례로 할당

d = {1:'one', 2:'two', 3:'three'}

for i in d:
    print(f'key 값: {i}, value 값: {d[i]}')






