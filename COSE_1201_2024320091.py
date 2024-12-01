#파일명 == 'COSE_1201_2024320091'

import numpy as np
#numpy가 설치되어 있지 않으시다면, 터미널에 pip install numpy를 입력해 실행해주세요

import matplotlib.pyplot as plt
#matplotlib이 설치되어 있지 않으시다면, 터미널에 pip install matplotlib을 입력해 실행해주세요
from matplotlib import rcParams
rcParams["font.family"] = "Malgun Gothic"
rcParams["axes.unicode_minus"] = False
# 한글 사용을 위한 폰트설정

import COSE_1201_2024320092 as f1
import COSE_1201_2024320120 as f2

data = f1.read_file('20231231.csv')
subs = f1.organize_subject(data)

selected = f2.print_subjects(subs)

rslt_M = f2.create_dict(data, '남자')
rslt_F = f2.create_dict(data, '여자')

X_axis = list(rslt_M.keys())
Y_Male = []
Y_FeMale = []

for pts in X_axis:
  Y_FeMale.append(rslt_F[pts])
  Y_Male.append(rslt_M[pts])

plt.title('2023학년도 수능시험 {} 성적'.format(selected))
plt.plot(X_axis, Y_FeMale, 'r-', label=  '여자')
plt.plot(X_axis, Y_Male, 'b-', label = '남자')
plt.legend()
plt.show()  