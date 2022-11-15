##### 파일 이름 바꾸기 #####

import os


# os.listdir(x): x 폴더 아래 파일 및 폴더 이름들의 리스트
# print(os.listdir('poke'))


# os.rename(A, B): A 이름/경로/형식을 B로 바꿈
# ex)
# os.rename('a', 'b'): 이름 변경
# os.rename('b', 'abc/b'): 경로 변경
# os.rename('abc/b', 'c.png'): 경로, 이름, 형식 변경



# 파일번호.포켓몬이름 .png 형태의 현재 파일 제목을 아래와 같이 변경
# 1.이상해씨 .png  >  001_이상해씨.png
# 단, os.rename은 원본을 변경하는 함수이므로 신중하게 사용하기
# 바꿀 이름의 형태가 확실할 때 제일 마지막에 사용

# 1) zfill 사용
# 문자열.zfill(x): x 자리를 다 채우지 못하면 0으로 채움

# 2) 이상해씨 뒤의 공백 없애기: strip()


for i in os.listdir('poke'):
    
    num = i.split('.')[0].zfill(3)
    name = i.split('.')[1].strip()
    ext = i.split('.')[-1]

    new_file_name = f'{num}_{name}.{ext}'
    
    os.rename(f'poke/{i}', f'poke/{new_file_name}')














