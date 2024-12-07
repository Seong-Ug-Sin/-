#파일명 == 'COSE_1201_2024320091(MAIN)'

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

yr = f1.select_year()
data = f1.read_file("{}1231.csv".format(yr))
category = f2.organize_category(data)

selected = f2.organize_subject(data, category)

rslt_M = f2.create_array(data, selected, '남자')
rslt_F = f2.create_array(data, selected, '여자')
bins = max(rslt_F[0], rslt_M[0])-min(rslt_F[-1], rslt_M[-1])
minimum = min(rslt_F[-1], rslt_M[-1])

tick_pos = list(range(minimum, minimum+bins+1, 5))
plt.figure(figsize=(10,7))
plt.xticks(tick_pos, fontsize = 10)
plt.title('{}학년도 수능시험 {} 성적'.format(yr,selected), fontsize=18)
plt.hist(rslt_M, bins=bins, label= '남자',  alpha = 0.5)
plt.hist(rslt_F, bins=bins, label= '여자',  alpha = 0.5)
plt.xlabel("표준점수", fontsize=14)
plt.ylabel("인원 수", fontsize=14)
plt.legend()
plt.show()
