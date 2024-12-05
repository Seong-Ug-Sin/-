#파일명 == 'C0SE_1201_2024320120'

#영역 선택 함수, return 영역
def organize_category (content_list) :
    category = []
    for line in content_list:
        if line[0] not in category and line[0] != '영역': category.append(line[0])
    print('영역 목록')
    print('/'.join(category))
    while(True):
        search=input('영역을 선택하세요: ')
        if search in category: break
        else: print('다시 입력하세요.')
    return search

#과목 선택 함수, return 과목
def organize_subject (content_list, category):
    subjects = []
    for line in content_list:
        if line[0] == category and line[1] not in subjects : subjects.append(line[1])
    print('<과목 목록>')
    print('/'.join(subjects))
    while(True):
        search=input('과목을 선택하세요: ')
        if search in subjects: break
        else: print('다시 입력하세요.')
    return search

#점수 배열 생성 함수, return np배열
def create_array(Data,subject,key):
    idx=Data[0].index(key)
    result=[]

    for type in Data[1:]:
        if type[1]==subject:
            result.append(type[idx])

    return np.array(result)

def read_file(name) :
    f = open(name, "r", encoding = 'cp949')
    read = csv.reader(f)
    read = list(read)
    return read

def select_year():
    num = int(input('1. 2020 / 2. 2021 / 3. 2022 / 4. 2023 중 그래프로 표현할 연도의 번호를 고르세요: '))
    while True:
        if num == 1 or num == 2 or num == 3 or num == 4: break
        else: num = input(('숫자 1,2,3,4 중 다시 입력하세요'))
    return str(2019+num)
