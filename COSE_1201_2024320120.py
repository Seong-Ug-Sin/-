#파일명 == 'C0SE_1201_2024320120'

#과목 선택 함수, return 과목
def print_subjects(subjects):
    print('<과목 목록>')
    print('/'.join(subjects))
    while(True):
        search=input('과목을 선택하세요: ')
        if search in subjects: break
        else: print('다시 입력하세요.')
    return search

#점수 딕셔너리 생성 함수, return 딕셔너리
def create_dict(Data,subject,key):

    result={}
    idx=Data[0].index(key)

    for score in Data:
        if score[1]==subject:
            result[int(score[2])]=int(score[idx])

    return result