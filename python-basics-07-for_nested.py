##### 구구단 예제 #####

##### 1 #####
# 구구단 출력하기

for i in range(1, 10):
    for j in range(1, 10):
        print(i, 'x', j, '=', i*j)



##### 2 #####
# 구구단 2~9단 출력 1

for i in range(2, 10):
    
    print(i, '단 출력')

    for j in range(1, 10):
        print(i, 'x', j, '=', i*j)
    
    print()



##### 3 #####
# 구구단 2~9단 출력 2 (가로 출력)

for i in range(1, 10):

    for j in range(2, 10):
        print(j, 'x', i, '=', i*j, end='\t')
        # end를 tab으로 하면 왼쪽 정렬이 맞게 출력됨
    
    print()


# 맨 위에 몇 단 출력인지 나타내기

for k in range(2, 10):
    print(k, '단 출력', end='\t')
print()

for i in range(1, 10):

    for j in range(2, 10):
        print(j, 'x', i, '=', i*j, end='\t')
    
    print()


# 단 출력 응용 풀이
# i가 0인 경우를 추가해 제일 먼저 몇 단인지 출력하도록 함

for i in range(0, 10):

    for j in range(2, 10):

        if i == 0:
            print(j, '단 출력', end='\t')
            # i가 0인 경우에는 구구단 들어가지 말고 몇 단인지만 출력
        else:
            print(j, 'x', i, '=', i*j, end='\t')
    
    print()




##### 반복문의 중첩 심화 문제 #####

##### 1 #####
# 1 ~ N 까지 각각의 수 이하의 짝수의 개수 구하기

# 1. 기획
# A 대상 (ex: 5)
# B 점검 범위 (ex: 1, 2, 3, 4, 5)

# A  B
# 1  1
# 2  1 2
# 3  1 2 3
# 4  1 2 3 4

# A 부분은 i에 대한 반복, B 부분은 j에 대한 반복
# B가 더 많이 바뀌므로 B가 내반복문, A가 외반복문

N = int(input('입력: '))

for i in range(1, N+1):
    
    cnt = 0
    
    for j in range(1, i+1):
    
        if j % 2 == 0:
            cnt += 1
    
    print(i, '이하의 짝수의 개수', cnt)


# 2. 확장
# N 하나를 대상으로: N 이하의 짝수의 개수 구하는 코드

cnt = 0

for i in range(1, N+1):
    if i % 2 == 0:
        cnt += 1
print(N, cnt)


# N에서 1 ~ N 까지의 수로 확장 (k: 1 ~ N)

for k in range(1, N+1):
    # k로 코드를 짜놓고 하나를 대상으로 짰던 코드를 안으로 밀어넣기

    cnt = 0

    # range(1, N+1)은 range(1, k+1)로 바꾸기
    for i in range(1, k+1):
        if i % 2 == 0:
            cnt += 1
    print(N, cnt)



##### 2 #####
# 3 ~ N 까지 각각의 약수를 구하는 프로그램

# 기획

# A  B
# 3  1 2 3
# 4  1 2 3 4
# 5  1 2 3 4 5

# A 외반복문 3 ~ N
# B 내반복문 1 ~ 대상

N = int(input('입력: '))

for i in range(3, N+1):
    
    div = []
    
    for j in range(1, i+1):
    
        if i % j == 0:
            div.append(j)
    
    print(i, div)



##### 3 #####
# 약수의 개수가 4개인 수를 '사약수'라고 합니다.
# Q. 아래 목록 중 사약수들의 합은?

num = [15871, 409, 14871, 12858, 13067, 4592, 236, 1241, 7185, 8158, 16990, 10704, 2510, 11080, 16404, 13927, 19429, 8070, 2725, 742, 17678, 16257, 13797, 9265, 2494, 5162, 862, 16291, 6195, 1302, 11088, 5792, 15489, 2259, 767, 19929, 8506, 7200, 17190, 5766, 19353, 5286, 7488, 2694, 14521, 13862, 6791, 190, 5034, 15198, 11601, 7634, 3504, 4945, 4562, 6663, 16268, 15136, 2942, 7211, 5692, 16386, 4446, 18856, 4952, 15442, 7823, 15118, 15399, 19009, 19272, 19473, 8519, 12747, 5467, 12811, 12935, 18005, 14214, 16204, 18597, 9965, 4122, 20428, 13752, 7506, 1038, 3328, 2791, 2654, 9334, 1428, 6875, 14494, 16783, 16480, 9776, 1226, 13666, 17001, 8308, 5307, 11241, 1074, 2946, 2141, 15732, 20384, 11526, 3056, 3058, 4920, 3761, 12610, 14579, 12372, 11746, 1162, 5859, 13091, 2292, 11427, 7559, 10222, 13441, 13425, 6907, 14249, 3038, 5269, 6486, 1170, 11111, 728, 3884, 10512, 14050, 10193, 16306, 12445, 8813, 3133, 11341, 18949, 10405, 14630, 12818, 9268, 19430, 13654, 9924, 16231, 19250, 8416, 15759, 10251, 11201, 10155, 12645, 16392, 11147, 19986, 12240, 6127, 8349, 13957, 16634, 5639, 18814, 19495, 1975, 16136, 19449, 11407, 10803, 9265, 11684, 20813, 16081, 14707, 6553, 545, 14995, 4482, 10889, 10982, 5466, 12795, 3861, 8141, 1947, 12608, 2066, 7954, 16764, 12271, 17858, 2620, 12241, 3313, 14825, 7892, 4761, 10121, 19943, 20031, 4525, 7128, 6188, 7957, 5075, 9766, 18582, 14824, 6274, 12512, 14559, 19341, 5026, 16408, 15638, 17444, 12596, 11878, 14662, 15970, 1665, 6852, 7257, 8563, 13698, 2884, 2383, 18487, 8466, 19849, 16754, 1766, 7836, 5196, 1143, 8078, 14820, 10391, 3163, 3026, 5065, 6483, 18383, 13239, 9636, 20928, 7399, 2455, 14809, 11343, 7053, 15026, 6970, 11214, 6308, 653, 15722, 16807, 17204, 9403, 18755, 19255, 17010, 6413, 9905, 1154, 1248, 15368, 18301, 8188, 2196, 12079, 6540, 16206, 10317, 4040, 18300, 6656, 15133, 19191, 3369, 4127, 15162, 5822, 13716, 18970, 1632, 13581, 6435, 18025, 5097, 6700, 6590, 10866, 15268, 7984, 18592, 4292, 20214, 17197, 6787, 12360, 17479, 2342, 5923, 14088, 11309, 4966, 8748, 5251, 20740, 17631, 2852, 18862, 13328, 5113, 3698, 7683, 6929, 7971, 5609, 15403, 6886, 9398, 3792, 3397, 19411, 2085, 15386, 13426, 2523, 4514, 18524, 3000, 15945, 3279, 1338, 20847, 1864, 13629, 12333, 19095, 14829, 20113, 13497, 17169, 19668, 11344, 6118, 14723, 19070, 20444, 17687, 5515, 18102, 10768, 12590, 6252, 13303, 165, 7218, 5816, 12777, 14075, 1317, 15681, 16911, 19824, 8791, 12131, 4363, 14901, 12101, 3316, 11967, 850, 422, 16023, 17592, 6228, 20579, 16995, 17982, 6936, 10552, 15730, 10420, 12640, 4191, 17479, 8978, 12840, 11925, 5064, 2602, 20701, 5683, 2093, 17537, 7357, 17759, 19779, 3013, 7714, 16377, 7511, 10785, 2418, 14480, 11791, 4181, 10616, 6030, 6782, 1586, 807, 14271, 12023, 16647, 13981, 1842, 3932, 16213, 20830, 9211, 4602, 3793, 6264, 8360, 18948, 17536, 11452, 4878, 17100, 18184, 15117, 15489, 13966, 4879, 12165, 6308, 4294, 15609, 5211, 3807, 15102, 20441, 2599, 4469, 9021, 13478, 5578, 7850, 5023, 14584, 8532, 19970, 13183, 15824, 18036, 5629, 11295, 18758, 5536, 11323, 9030, 401, 14243, 2493, 14228, 7205, 17084, 8288, 15614, 13393, 17795, 14295, 7853, 19294, 8847, 8639, 7985, 1119, 20438, 11738, 18433, 17874, 18029, 12852, 765, 17646, 6462, 10890, 4150, 19343, 17608, 11931, 842, 4977, 2738, 18830, 14000, 15492, 5222, 5343, 2280, 681, 6973, 7524, 16478, 471, 15946, 9234, 10225, 2725, 2550, 8361, 10138, 12885, 8887, 10682, 9509, 14530, 18867, 13043, 12653, 10742, 7088, 6201, 3537, 4693, 13787, 19345, 4176, 12171, 9786, 1031, 11015, 15433, 5441, 17772, 10297, 16965, 18531, 13673, 10637, 396, 14764, 19284, 13192, 15909, 18431, 10577, 10870, 13997, 10782, 958, 18549, 3685, 17188, 18041, 15785, 11583, 16280, 16655, 10133, 7401, 17426, 6720, 4471, 2946, 9641, 18080, 12544, 4015, 13067, 5416, 10074, 8627, 15566, 5576, 18247, 16811, 5740, 11668, 12028, 1422, 20294, 10271, 11632, 3075, 13120, 11420, 19183, 4422, 4140, 2504, 6343, 16278, 8534, 17397, 17377, 20864, 11424, 599, 20639, 10694, 10158, 13358, 20459, 16448, 19783, 17076, 20032, 14625, 19360, 10275, 7281, 19242, 20395, 9082, 5537, 963, 10443, 15918, 1116, 15811, 8009, 118, 16736, 11969, 6586, 11014, 12108, 12131, 20864, 4110, 11975, 10359, 7751, 1793, 17200, 15370, 3404, 1209, 12586, 9036, 19278, 2129, 16118, 121, 4726, 18605, 15965, 14498, 11786, 20610, 688, 17661, 15989, 12905, 10673, 16054, 7370, 13330, 4159, 14279, 8393, 18881, 1489, 7139, 3616, 8578, 18345, 8981, 252, 7748, 5321, 3316, 20499, 13491, 10166, 1661, 16575, 12838, 15909, 16601, 17415, 5491, 6471, 9046, 11790, 20519, 19376, 2444, 3254, 5318, 8800, 12983, 3775, 8682, 18721, 7168, 5490, 2037, 16774, 19202, 11583, 10590, 2162, 17430, 8525, 18197, 6147, 8270, 15936, 6118, 13767, 11530, 2880, 6361, 12913, 11582, 13081, 12190, 18195, 6873, 8635, 19217, 9183, 12038, 16430, 13719, 14969, 11552, 563, 3231, 4939, 13099, 16934, 3227, 19710, 2399, 6287, 2160, 19181, 5310, 2631, 17150, 15596, 19936, 1584, 19829, 16772, 9235, 7799, 5864, 6184, 1232, 12290, 11744, 9462, 17459, 9969, 2340, 6864, 19533, 18295, 14057, 11629, 19030, 20183, 6688, 11267, 4735, 655, 11301, 13060, 20717, 15589, 5176, 19178, 10850, 11004, 5152, 178, 8219, 14541, 1334, 7334, 10662, 15174, 4425, 444, 17199, 2803, 2860, 10806, 10248, 13266, 19045, 13367, 9074, 12739, 13064, 11266, 7647, 14879, 9399, 11057, 11429, 10278, 18961, 14513, 14921, 12325, 13533, 12268, 10388, 2342, 20643, 12346, 19364, 14476, 15170, 12690, 14921, 19040, 11037, 14063, 5858, 15565, 18116, 19316, 19848, 17920, 5823, 15024, 11326, 6907, 11264, 6108, 10875, 1324, 12511, 13919, 901, 12783, 7257, 10074, 14586, 10386, 5022, 19897, 10138, 18832, 2549, 13623, 20424, 20468, 19737, 1768, 14058, 10924, 16140, 4227, 13473, 9166, 19183, 17927, 15886, 10486, 5196, 1769, 8682, 1317, 20583, 13921, 20470, 7645, 19502, 5055, 14757, 18153, 11914, 5708, 1711, 11887, 6552, 14791, 2862, 19141, 1036, 11691, 2428, 13058, 16263, 6250, 15161, 12073, 3897, 11436, 3776, 14243, 17313, 7993, 8395, 2693, 300, 12597, 7618, 4466, 12642, 11321, 5965, 16852, 11216, 16906, 19094, 3283, 14113, 10834, 16530, 7742, 4009, 11320, 6670, 3534, 12317, 15435, 3327, 3939, 16804, 20903, 17472, 14933, 4693, 6176, 12656, 12748, 17459, 6463, 18120, 10050, 13942, 2170, 3709, 5754, 20888, 14827, 3657, 5743, 19845, 5743, 682, 2688, 2576, 14694, 8214, 16730, 4058, 16468, 20218, 4369, 901, 1366, 20868, 20055, 11296, 16549, 14280, 11897, 17374, 15914, 9512, 14691, 17903, 4023, 5074, 8163, 5357, 6248, 4460, 16530, 8197, 16966, 11981, 6852, 16808, 194, 17895, 16664, 8901, 20864]

div_4 = []

for i in num:
    
    div = []

    for j in range(1, i+1):
        if i % j == 0:
            div.append(j)
    
    if len(div) == 4:
        div_4.append(i)

print(sum(div_4))



##### ox문제 #####

# o 는 1점, x 는 0점이다.
# 만약 o 가 연속으로 등장할 경우 점수가 배가 되어 계산된다고 한다.
# 하지만, 중간에 x 를 만나게 되면 배수가 끊겨버린다.
# ex) oxooxxo  >  1 + 1 + 2 + 1  > 5 점
#     xoooxoo  >  1 + 2 + 4 + 1 + 2 > 10 점
#     oooooxo  >  1 + 2 + 4 + 8 + 16 + 1 > 32 점

# Q. 아래의 리스트를 보고 점수 총합을 구하세요.

ox = ['oooooxooooo', 'xoooooooo', 'xoooooooo', 'oooxxoxxoo', 'ooooooxooooo', 'oxoxooooo', 'oooooooooxo', 'ooooxxooooo', 'ooxooooooo', 'xooxooxoooxo', 'ooxooxoxo', 'ooooooxxoxxx', 'ooooooooxooo', 'ooooxoooo', 'oooxxxoxooo', 'oxoooooxoo', 'oxxooooxooxo', 'ooooxoooooxo', 'ooooooxooxo', 'oooxoxxoxooo', 'ooxooxoooxo', 'ooooooox', 'oxxoxoooxo', 'ooooxxxo', 'ooooooxoxo', 'ooxxoxoxooox', 'oxoooxoo', 'oooxooxooooo', 'oooooooo', 'ooxooxooxo', 'oxoooooo', 'xooxoxox', 'ooooxooo', 'oooooxoxoo', 'ooooooox', 'xoooooooooxo', 'oooooxooooo', 'oooooxooo', 'oooooxoooooo', 'xoooooooxooo', 'xoooooxo', 'xooooooooo', 'oooooooooxxo', 'oooooooooo', 'xooxooooo', 'oooooooooxo', 'xoxooxoo', 'ooxooooo', 'xoooxxox', 'ooxxooooox', 'xooooooo', 'ooooooooooox', 'oooooooooo', 'oooxooooxxox', 'oooooooox', 'ooooxooooooo', 'oooooooooo', 'ooxxooooxooo', 'oxoxoxooo', 'oxoxooooxox', 'oooxoooxo', 'ooooxoxxooo', 'xooooooo', 'xooxoxoxo', 'ooooooxoxo', 'oooxoooxoooo', 'ooxooooo', 'oxooxxoooo', 'oooooxxx', 'xxoooxoox', 'ooooooooo', 'xoooooxxo', 'oooooooooo', 'ooooooxoo', 'oooxxooo', 'oooooooxo', 'oooxoooxoo', 'oooooxxo', 'ooxxooooooo', 'ooooxxooo', 'oooooxoooo', 'ooxxoxooo', 'oooxooxxo', 'oooooooooxo', 'oxooxooox', 'ooxooooooo', 'xxooxxoooooo', 'oooooooooo', 'oxxxoooooo', 'xoooooxoooo', 'ooooxooooo', 'oxoooxxoo', 'ooxooxoo', 'oooooooo', 'oxxooooo', 'xoooxxxoox', 'oooooooooxo', 'ooooooox', 'ooooooooo', 'oooxooooooox']

# ox 리스트 안 문자열 각각의 점수가 추가될 리스트
total = []

for i in ox:

    # ox 리스트 안 개별 문자열의 점수 구하기
    if i[0] == 'o':
        score = [1]
    else:
        score = [0]

    for j in range(1, len(i)):
        if i[j] == 'o':
            if i[j-1] == 'o':
                score.append(score[j-1]*2)
            else:
                score.append(1)
        else:
            score.append(0)

    # total 리스트에 현재 문자열의 점수 추가하기
    total.append(sum(score))

print(sum(total))






