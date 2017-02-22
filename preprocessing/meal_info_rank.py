# coding=utf8
import MySQLdb
import pandas as pd

conn = MySQLdb.connect(host="localhost", user="root", passwd="root", db="student_grant", charset="utf8")


def gen_meal_info_t():
    # breakfast_info 选取了8点作为吃早餐的数据


    breakfast_info = pd.read_csv('D:/Competition/student_grant/input/breakfast_info.csv')

    # lunch_info 选取了11-13点作为吃午饭的数据

    lunch_info = pd.read_csv('D:/Competition/student_grant/input/lunch_info.csv')

    # dinner_info 选取了17-19点作为吃午饭的数据

    dinner_info = pd.read_csv('D:/Competition/student_grant/input/dinner_info.csv')

    # late_night_info 选取了19-22点作为吃午饭的数据
    # late_night_info = pd.DataFrame(late_night_temp.groupby(['id'])['u_fee'].count())
    # late_night_info['fee_sum'] = late_night_temp.groupby(['id'])['u_fee'].sum()
    # late_night_info['fee_avg'] = late_night_temp.groupby(['id'])['u_fee'].mean()
    # late_night_info['fee_max'] = late_night_temp.groupby(['id'])['u_fee'].max()

    late_night_info = pd.read_csv('D:/Competition/student_grant/input/late_night_info.csv')

    meal_info = pd.merge(breakfast_info, lunch_info, how='outer', on='id')
    meal_info = pd.merge(meal_info, dinner_info, how='outer', on='id')
    meal_info = pd.merge(meal_info, late_night_info, how='outer', on='id')

    # score
    score_train = pd.read_table('D:/Competition/student_grant/train/score_train.txt', sep=',', header=-1)
    score_train.columns = ['id', 'college', 'score']
    score_test = pd.read_table('D:/Competition/student_grant/test/score_test.txt', sep=',', header=-1)
    score_test.columns = ['id', 'college', 'score']
    score_train_test = pd.concat([score_train, score_test])
    del score_train, score_test, score_train_test['score']

    meal_info = pd.merge(meal_info, score_train_test, how='outer', on='id')

    meal_info.to_csv('D:/Competition/student_grant/input/meal_info_t.txt')


def gen_meal_info():
    # breakfast_info 选取了8点作为吃早餐的数据
    breakfast_info = pd.read_csv('D:/Competition/student_grant/input/breakfast_info.csv')
    # lunch_info 选取了11-13点作为吃午饭的数据
    lunch_info = pd.read_csv('D:/Competition/student_grant/input/lunch_info.csv')
    # dinner_info 选取了17-19点作为吃午饭的数据
    dinner_info = pd.read_csv('D:/Competition/student_grant/input/dinner_info.csv')
    # late_night_info 选取了19-22点作为吃午饭的数据
    late_night_info = pd.read_csv('D:/Competition/student_grant/input/late_night_info.csv')
    meal_info = pd.merge(breakfast_info, lunch_info, how='outer', on='id')
    meal_info = pd.merge(meal_info, dinner_info, how='outer', on='id')
    meal_info = pd.merge(meal_info, late_night_info, how='outer', on='id')

    sql = 'SELECT * from  meal_info_t1'
    rank_amount = pd.read_sql(sql, conn, index_col=None)
    rank_amount['id'] = rank_amount['id'].astype('int')
    meal_info = pd.merge(meal_info, rank_amount, how='left', on='id')

    del meal_info['college']
    meal_info.to_csv('D:/Competition/student_grant/input/meal_info_rank.csv')


gen_meal_info()
# d_s_info = pd.read_csv('D:/Competition/student_grant/input/d_s_info.csv')
