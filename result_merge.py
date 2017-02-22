# -*-coding:utf-8 -*-
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier

r1 = pd.read_csv("D:/Competition/student_grant/17153142_1856.csv")
r25 = pd.read_csv("D:/Competition/student_grant/other/r25_sub.csv")
r25.columns = ['studentid', 'subsidy']
sub_all = pd.merge(r25, r1, on='studentid')

# sub_all.to_csv("D:/Competition/student_grant/sub_all.csv", index=False)

out = open("D:/Competition/student_grant/sub_merge.csv", 'w')
out.write("studentid,subsidy\n")
i, j, k = 0, 0, 0
for index, row in sub_all.iterrows():
    money = row['subsidy_x']
    if row['subsidy_x'] == 0 and row['subsidy_y'] == 2000:
        money = row['subsidy_y']
        i += 1
    if row['subsidy_x'] == 0 and row['subsidy_y'] == 1500 and j<225:
        money = row['subsidy_y']
        j += 1
    if row['subsidy_x'] == 0 and row['subsidy_y'] == 1000 and k < 5:
        money = row['subsidy_y']
        k += 1

    out.write(str(row['studentid']) + "," + str(money) + "\n")
out.close()
print i, j, k
