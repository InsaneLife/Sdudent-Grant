# coding=utf8
import pandas as pd
import numpy as np
from sklearn.ensemble import GradientBoostingClassifier
from sklearn import preprocessing

train = pd.read_table('D:/Competition/student_grant/train/subsidy_train.txt', sep=',', header=-1)
train.columns = ['id', 'money']

score_train = pd.read_csv('D:/Competition/student_grant/input/train/score_train.csv')

train = pd.merge(train, score_train, how='left', on='id')

train.to_csv('D:/Competition/student_grant/input/train/train_score.csv')
