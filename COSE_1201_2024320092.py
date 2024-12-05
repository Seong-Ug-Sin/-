#파일명 == 'C0SE_1201_2024320092'

import csv

def read_file(name) :
    filepath = './ver 1.1/'+name
    f = open(filepath, "r", encoding = 'cp949')
    read = csv.reader(f)
    read = list(read)
    return read

def select_year():
    num = int(input('1. 2020 / 2. 2021 / 3. 2022 / 4. 2023 중 그래프로 표현할 연도의 번호를 고르세요: '))
    while True:
        if num == 1 or num == 2 or num == 3 or num == 4: break
        else: num = input(('숫자 1,2,3,4 중 다시 입력하세요'))
    return str(2019+num)