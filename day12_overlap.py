# Q. overlap()
# 사용자로부터 두 문자열 A, B를 입력으로 받도록 하자.
# A의 뒷부분과 B의 앞부분을 가장 길게 일치시켜 둘을 겹치게 만든 새로운 문자열 C를 만드는 프로그램을 작성하시오.
# 만약 A의 뒷부분과 B의 앞부분이 다르면 B를 A뒤에 바로 붙여야 한다.
# 이를 위하여 C = oversap(A, B)와 같이 A, B를 인자로 받아 C를 반환하는 함수 overlap()를 구현하여라.


A = input('문자열 A: ')
B = input('문자열 B: ')

overlap = 0

if len(A) <= len(B):

    for i in range(1, len(A)+1):

        if A[-i:] == B[:i]:
            overlap = i

else:

    for j in range(1, len(B)+1):

        if A[-j:] == B[:j]:
            overlap = j


C = A + B[overlap:]

print(f'문자열 C: {C}')



# 슬라이싱, break 활용





