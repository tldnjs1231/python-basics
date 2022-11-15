from PIL import Image
import os
from tqdm import tqdm


# Mission 1) 사용
# img = Image.open('poke500/001_이상해씨.png')

# Mission 2) 사용
# img = Image.open('poke500/491_다크라이.png')

# 사진은 무수히 많은 픽셀이라는 점으로 이루어져 있음
# img.getpixel((x, y))
# (x, y) 좌표의 색상정보 반환

# img.putpixel((x, y), (r, g, b, a))
# (x, y) 좌표에 r, g, b, a 색상을 넣어줌

# 색상정보: RGB, RGBA(투명도!)
# print(img.mode)

# r, g, b (0, 0, 0)  >  검은색
# r, g, b, a (0, 0, 0, 0)  >  흰색
# r, g, b, a (0, 0, 0, 255)  >  검은색 255 선명(a 클수록 선명)



# Mission) 이상해씨 검은색으로 만들기

# for x in range(500):
#     for y in range(500):
#         if img.getpixel((x, y)) != (0, 0, 0, 0):
#             img.putpixel((x, y), (0, 0, 0, 255))

# img.show()

# range(500) 대신 range(img.size) 사용해도 됨



# Mission 2) 다크라이 검은색으로 만들었을 때 주변에 이상한 무늬 없애기

# for x in range(500):
#     for y in range(500):
#         if img.getpixel((x, y)) != (0, 0, 0, 0):
#             img.putpixel((x, y), (0, 0, 0, 255))

# 이상해씨처럼 위 코드 사용하면 다크라이는 깔끔하게 검은색 되지 않음
# 사람 눈으로는 구분할 수 없지만 완전 흰색이 아닌 색들이 존재하는 것
# 예를 들면 (0, 0, 0, 1)
# 육안으로 구분할 수 있으려면 투명도가 20, 30 정도 이상은 되어야 함
# 따라서 아래와 같은 코드로 문제를 해결할 수 있음


# for x in range(500):
#     for y in range(500):
#         r = img.getpixel((x, y))
#         if r[3] > 30:
#             img.putpixel((x, y), (0, 0, 0, 255))

# img.show()



# Mission 3) shadow 폴더 생성 후 모든 포켓몬 검은색으로 저장

for k in os.listdir('poke500'):

    img = Image.open(f'poke500/{k}')

    for x in range(500):
        for y in range(500):
            r = img.getpixel((x, y))
            if r[3] > 30:
                img.putpixel((x, y), (0, 0, 0, 255))
    
    img.save(f'shadow/{k}')


## 3교시 녹강 보면서 놓친 부분 코드 옮기고 필기하기
#(아직 미션 3 코드 완성 안 돼서 코드 안 돌림)

