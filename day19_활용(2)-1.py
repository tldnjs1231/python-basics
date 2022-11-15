##### 사진 관리 #####

from PIL import Image
import os

# 이미지 열기
# img = Image.open('poke/001_이상해씨.png')

# 이미지 확인
# img.show()

# 이미지 크기 조정 (img 원본 자체를 바꾸지는 않음)
# img = img.resize((500, 500))

# 이미지 저장 (상대경로)
# img.save('거대이상해씨.png')



# Mission 1) poke500 폴더 생성 후 poke 포켓몬들 전부 500x500으로 저장
# 파일 이름은 그대로 유지

# for i in os.listdir('poke'):

#     img = Image.open(f'poke/{i}')
#     img_500 = img.resize((500, 500))

#     img_500.save(f'poke500/{i}')






