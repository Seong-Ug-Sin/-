#파일명 == 'C0SE_1201_2024320092'

import csv

def read_file(name) :
    f = open(name, "r", encoding = 'cp949')
    read = csv.reader(f)
    read = list(read)
    return read

def organize_subject (content_list) :
    mylist = []
    for line in content_list:
        if line[1] not in mylist and line[1] != '유형': mylist.append(line[1])

    return mylist

content = read_file("20231231.csv")
subjects = organize_subject(content)

print(subjects)