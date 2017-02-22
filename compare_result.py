# -*-coding:utf-8 -*-
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier

train = pd.read_csv("D:/Competition/student_grant/train/subsidy_train.txt")
train.columns = ['id', 'subsidy']
r1 = pd.read_csv("D:/Competition/student_grant/20103839_ohter39.csv")
r2 = pd.read_csv("D:/Competition/student_grant/sub_merge.csv")
r25 = pd.read_csv("D:/Competition/student_grant/results_25.csv")

# (741, 2)
# (465, 2)
# (354, 2)

print train[train['subsidy'] == 0].shape
print train[train['subsidy'] == 1000].shape
print train[train['subsidy'] == 1500].shape
print train[train['subsidy'] == 2000].shape
print '---------------------------'
print r1[r1['subsidy'] == 1000].shape
print r1[r1['subsidy'] == 1500].shape
print r1[r1['subsidy'] == 2000].shape
print '---------------------------'
print r2[r2['subsidy'] == 1000].shape
print r2[r2['subsidy'] == 1500].shape
print r2[r2['subsidy'] == 2000].shape
print '---------------------------'
print r25[r25['subsidy'] == 1].shape
print r25[r25['subsidy'] == 2].shape
print r25[r25['subsidy'] == 3].shape
print '---------------------------'

r25.subsidy = r25.subsidy.replace(1, 1000)
r25.subsidy = r25.subsidy.replace(2, 1500)
r25.subsidy = r25.subsidy.replace(3, 2000)

r25['std_id'] = r25['std_id'].apply(lambda x:int(x))
r25['subsidy'] = r25['subsidy'].apply(lambda x:int(x))
r25.to_csv('D:/Competition/student_grant/other/r25_sub.csv',index=False)