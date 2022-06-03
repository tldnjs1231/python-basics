##### 이스케이프 문자 #####

print('Mother\'s Birthday')

# "\('.')/"
print('"\\(\'.\')/"')
print("\"\\('.')/\"")



##### print() #####

# 여러 자료 동시 출력
print('제 나이는', 25, '입니다.')


# 변수 출력
x = 10
print('x의 값은', x, '입니다.')

A = 20
B = 3
print('A 는', A, '입니다.')
print('B 는', B, '입니다.')


# 실습) 자신의 이름, 나이, 이메일을 변수에 담아서 출력
name = 'gool'
age = 25
email = 'gool@naver.com'

print('제 이름은', name)
print('제 나이는', age)
print('제 이메일은', email, '입니다.')



##### type() #####

print(type(10))
print(type("hello"))



##### 연산자 #####

print('A + B =', A+B)
print('A - B =', A-B)
print('A x B =', A*B)
print('A / B =', A/B)
print('A // B =', A//B)
print('A % B =', A%B)
print('A ** B =', A**B)


# 문자열 자료형의 연산
A = '대한독립'
B = '만세'
C = '~'
D = A + ' ' + B*3 + C*5
print(D)

print('='*30)
print('자판기')
print('='*30)


# %, // 연산자를 활용한 자리 검출
a = 738

a_100 = a//100
a_10 = (a%100)//10
a_1 = a%10

print(a_100, a_10, a_1)




