# coding=utf8
import MySQLdb
import pandas as pd


# test_test D:/Competition/student_grant
test = pd.read_table('D:/Competition/student_grant/test/subsidy_test.txt',sep=',',header=-1)
test.columns = ['id']

# score
# score_test = pd.read_table('D:/Competition/student_grant/test/score_test.txt',sep=',',header=-1)
# score_test.columns = ['id','college','score']
#
# college = pd.DataFrame(score_test.groupby(['college'])['score'].max())
# college.to_csv('D:/Competition/student_grant/input/test/college.csv',index=True)
# college = pd.read_csv('D:/Competition/student_grant/input/test/college.csv')
# college.columns = ['college','num']
#
# score_test = pd.merge(score_test, college, how='left', on='college')
# score_test['order'] = score_test['score'] / score_test['num']
# score_test.to_csv('D:/Competition/student_grant/input/score_test.csv', index=True)
# test = pd.merge(test, score_test, how='left', on='id')


# card_score
card_score = pd.read_csv('D:/Competition/student_grant/input/test/card_score.csv')
test = pd.merge(test, card_score, how='left',on='id')


# card of student info
id_info = pd.read_csv('D:/Competition/student_grant/input/id_info.csv')
test = pd.merge(test, id_info, how='left', on='id')

test.to_csv('D:/Competition/student_grant/input/test/test.csv',index=False)