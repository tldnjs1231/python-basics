# Q. 이어적기2+  
# 1에서 N까지 이어적는다. 만약 적어야하는 수가 5 라고 한다면 12345 를 적는다. 따라서, N 이 7이면 1121231234123451234561234567 로 이어적어야한다.

# PASS : N이 2000 일때 총 길이


N = int(input('입력: '))

num = ''

for i in range(1, N+1):
    for j in range(1, i+1):
        num += str(j)
        

print(len(num))






