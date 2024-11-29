import csv

f = open("20231231.csv", "r", encoding = 'cp949')
reader = csv.reader(f)
read = list(reader)
f.close()

subjects = []
for line in read :
    if line[1] not in subjects and line[1] != '유형': subjects.append(line[1])