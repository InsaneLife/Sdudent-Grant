# coding=utf8
import MySQLdb
import pandas as pd

# train_test D:/Competition/student_grant
train = pd.read_table('D:/Competition/student_grant/train/subsidy_train.txt',sep=',',header=-1)
train.columns = ['id','money']

# score
# score_train = pd.read_table('D:/Competition/student_grant/train/score_train.txt',sep=',',header=-1)
# score_train.columns = ['id','college','score']
#
# college = pd.DataFrame(score_train.groupby(['college'])['score'].max())
# college.to_csv('D:/Competition/student_grant/input/train/college.csv',index=True)
# college = pd.read_csv('D:/Competition/student_grant/input/train/college.csv')
# college.columns = ['college','num']
#
# score_train = pd.merge(score_train, college, how='left', on='college')
# score_train['order'] = score_train['score'] / score_train['num']
# score_train.to_csv('D:/Competition/student_grant/input/score_train.csv', index=True)
# train = pd.merge(train, score_train, how='left', on='id')


# card_score
card_score = pd.read_csv('D:/Competition/student_grant/input/train/card_score.csv')
train = pd.merge(train, card_score, how='left',on='id')


# card of student info
id_info = pd.read_csv('D:/Competition/student_grant/input/id_info.csv')
train = pd.merge(train, id_info, how='left', on='id')

train.to_csv('D:/Competition/student_grant/input/train/train.csv',index=False)