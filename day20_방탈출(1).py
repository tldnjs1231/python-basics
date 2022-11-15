# Q. 오늘은 금요일~ N 일후 요일에 대한 요일코드를 조합해서 탈출하세요.
# 월M 화T 수W 목T 금F 토S 일S
# PASS : 요일코드 조합(대문자8자리)

# - 40일 후
# - 47일 후
# - 70일 후
# - 130일 후
# - 170일 후
# - 637일 후
# - 663일 후
# - 747일 후

day = ''

N = [40, 47, 70, 130, 170, 637, 663, 747]

for i in N:

    if i % 7 == 0:
        day += 'F'
    elif i % 7 == 1:
        day += 'S'
    elif i % 7 == 2:
        day += 'S'
    elif i % 7 == 3:
        day += 'M'
    elif i % 7 == 4:
        day += 'T'
    elif i % 7 == 5:
        day += 'W'
    else:
        day += 'T'

print(day)








