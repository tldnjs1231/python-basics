##### 나만의 단어장(dictionary 자료형 활용 실습) #####

import time
import os

f = open('단어장.txt', 'r', encoding='utf-8')
st = f.read().split()

vocab = {}

for i in st:
    words = i.split(':')
    vocab[words[0]] = words[1]


while True:

    print('='*30)
    print('1. 단어목록보기')
    print('2. 단어검색')
    print('3. 단어추가')
    print('4. 단어수정')
    print('5. 단어삭제')
    print('6. 프로그램 종료')
    print('='*30)

    menu = input('메뉴입력: ')
    print()

    if menu.isnumeric():

        if menu == '1':
            for i in vocab:
                print(i)
            time.sleep(2)
            os.system('cls')
        
        elif menu == '2':
            search = input('단어를 검색해주세요: ')
            if search in vocab:
                print(f"{search} 의 뜻은 '{vocab[search]}' 입니다.")
                time.sleep(2)
                os.system('cls')
            else:
                print(f'{search} 는 없는 단어입니다.')
                time.sleep(2)
                os.system('cls')
        
        elif menu == '3':
            add_ = input('추가할 단어를 입력하세요: ')
            if add_ in vocab:
                print('단어가 이미 존재합니다.')
                time.sleep(2)
                os.system('cls')
            else:
                meaning = input(f'{add_} 의 뜻을 입력하세요: ')
                vocab[add_] = meaning
                print(f'{add_} 가 추가되었습니다.')
                time.sleep(2)
                os.system('cls')
        
        elif menu == '4':
            edit = input('수정할 단어를 검색해주세요: ')
            if edit in vocab:
                meaning = input(f'{edit} 의 뜻을 입력하세요: ')
                vocab[edit] = meaning
                print(f'{edit} 의 뜻이 수정되었습니다.')
                time.sleep(2)
                os.system('cls')
            else:
                print('등록되어있지 않은 단어입니다.')
                time.sleep(2)
                os.system('cls')

        elif menu == '5':
            delete_ = input('삭제할 단어를 검색해주세요: ')
            if delete_ in vocab:
                del vocab[delete_]
                print(f'{delete_} 가 삭제됩니다.')
                time.sleep(2)
                os.system('cls')
            else:
                print('등록되어있지 않은 단어입니다.')
                time.sleep(2)
                os.system('cls')

        elif menu == '6':
            print('단어장이 종료됩니다.')
            f = open('단어장.txt', 'w', encoding='utf-8')
            for i in vocab:
                f.write(f'{i}:{vocab[i]}\n')
            break

        else:
            print('1에서 6까지의 숫자를 입력해주세요.')
            time.sleep(2)
            os.system('cls')    
    
    else:
        print('1에서 6까지의 숫자를 입력해주세요.')
        time.sleep(2)
        os.system('cls')



        



