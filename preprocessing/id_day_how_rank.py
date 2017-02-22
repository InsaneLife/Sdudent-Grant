# coding=utf8
import MySQLdb
import pandas as pd


def id_day_how_c():
    id_day_how = pd.read_csv('D:/Competition/student_grant/input/id_day_how.csv')

    # score
    score_train = pd.read_table('D:/Competition/student_grant/train/score_train.txt', sep=',', header=-1)
    score_train.columns = ['id', 'college', 'score']
    score_test = pd.read_table('D:/Competition/student_grant/test/score_test.txt', sep=',', header=-1)
    score_test.columns = ['id', 'college', 'score']
    score_train_test = pd.concat([score_train, score_test])
    del score_train, score_test, score_train_test['score']

    id_day_how = pd.merge(id_day_how, score_train_test, how='left', on='id')
    id_day_how.to_csv('D:/Competition/student_grant/input/id_day_how_c.csv', index=False)


# score
score_train = pd.read_table('D:/Competition/student_grant/train/score_train.txt', sep=',', header=-1)
score_train.columns = ['id', 'college', 'score']
score_test = pd.read_table('D:/Competition/student_grant/test/score_test.txt', sep=',', header=-1)
score_test.columns = ['id', 'college', 'score']
score_train_test = pd.concat([score_train, score_test])
del score_train, score_test, score_train_test['score']
college = pd.read_csv('D:/Competition/student_grant/input/college.csv')
college.columns = ['college', 'college_num']
score_train_test = pd.merge(score_train_test, college, how='left', on='college')

conn = MySQLdb.connect(host="localhost", user="root", passwd="root", db="student_grant", charset="utf8")
sql = 'SELECT * from  id_day_how_c1'
rank_amount = pd.read_sql(sql, conn, index_col=None)
rank_amount['id'] = rank_amount['id'].astype('int')
id_day_how = pd.read_csv('D:/Competition/student_grant/input/id_day_how.csv')
id_day_how_rank = pd.merge(id_day_how, score_train_test, how='left', on='id')
id_day_how_rank = pd.merge(id_day_how_rank, rank_amount, how='left', on='id')

id_day_how_rank['a_dsum_st_c_rank_c'] = id_day_how_rank['a_dsum_st_c_rank'] / id_day_how_rank['college_num']
id_day_how_rank['a_dsum_cs_c_rank_c'] = id_day_how_rank['a_dsum_cs_c_rank'] / id_day_how_rank['college_num']

del id_day_how_rank['college'], id_day_how_rank['college_num']
id_day_how_rank.to_csv('D:/Competition/student_grant/input/id_day_how_rank.csv')
