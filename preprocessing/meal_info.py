# coding=utf8
import MySQLdb
import pandas as pd

conn = MySQLdb.connect(host="localhost", user="root", passwd="root", db="student_grant", charset="utf8")


def meal_info():
    # breakfast_info 选取了8点作为吃早餐的数据
    sql = "SELECT t.sid AS id,REPLACE(SUBSTR(t.date,1,10),'-','') AS days,t.u_fee,t.r_fee FROM card_train t WHERE t.c3='食堂' AND REPLACE(SUBSTR(t.date,12,5),':','')<0800"
    breakfast_train = pd.read_sql(sql, conn, index_col=None)

    sql = "SELECT t.sid AS id,REPLACE(SUBSTR(t.date,1,10),'-','') AS days,t.u_fee,t.r_fee FROM card_test t WHERE t.c3='食堂' AND REPLACE(SUBSTR(t.date,12,5),':','')<0800"
    breakfast_test = pd.read_sql(sql, conn, index_col=None)
    print "sql completed"

    breakfast_all = pd.concat([breakfast_train, breakfast_test])
    breakfast_all['u_fee'] = breakfast_all['u_fee'].apply(lambda x: float(x))
    breakfast_temp = pd.DataFrame(breakfast_all.groupby(['id', 'days'])['r_fee'].count())
    breakfast_temp['u_fee'] = breakfast_all.groupby(['id', 'days'])['u_fee'].sum()
    breakfast_temp.to_csv('D:/Competition/student_grant/input/temp.csv')
    breakfast_temp = pd.read_csv('D:/Competition/student_grant/input/temp.csv')

    breakfast_info = pd.DataFrame(breakfast_temp.groupby(['id'])['u_fee'].count())
    breakfast_info['fee_sum'] = breakfast_temp.groupby(['id'])['u_fee'].sum()
    breakfast_info['fee_avg'] = breakfast_temp.groupby(['id'])['u_fee'].mean()
    breakfast_info['fee_max'] = breakfast_temp.groupby(['id'])['u_fee'].max()

    breakfast_info.to_csv('D:/Competition/student_grant/input/breakfast_info.csv')

    # lunch_info 选取了11-13点作为吃午饭的数据
    sql = "SELECT t.sid AS id,REPLACE(SUBSTR(t.date,1,10),'-','') AS days,t.u_fee,t.r_fee FROM card_train t WHERE t.c3='食堂' AND REPLACE(SUBSTR(t.date,12,5),':','')>1100 AND REPLACE(SUBSTR(t.date,12,5),':','')<1300"
    lunch_train = pd.read_sql(sql, conn, index_col=None)

    sql = "SELECT t.sid AS id,REPLACE(SUBSTR(t.date,1,10),'-','') AS days,t.u_fee,t.r_fee FROM card_test t WHERE t.c3='食堂' AND REPLACE(SUBSTR(t.date,12,5),':','')>1100 AND REPLACE(SUBSTR(t.date,12,5),':','')<1300"
    lunch_test = pd.read_sql(sql, conn, index_col=None)
    print "sql completed"
    lunch_all = pd.concat([lunch_train, lunch_test])
    lunch_all['u_fee'] = lunch_all['u_fee'].apply(lambda x: float(x))
    lunch_temp = pd.DataFrame(lunch_all.groupby(['id', 'days'])['r_fee'].count())
    lunch_temp['u_fee'] = lunch_all.groupby(['id', 'days'])['u_fee'].sum()
    lunch_temp.to_csv('D:/Competition/student_grant/input/temp.csv')
    lunch_temp = pd.read_csv('D:/Competition/student_grant/input/temp.csv')

    lunch_info = pd.DataFrame(lunch_temp.groupby(['id'])['u_fee'].count())
    lunch_info['fee_sum'] = lunch_temp.groupby(['id'])['u_fee'].sum()
    lunch_info['fee_avg'] = lunch_temp.groupby(['id'])['u_fee'].mean()
    lunch_info['fee_max'] = lunch_temp.groupby(['id'])['u_fee'].max()

    lunch_info.to_csv('D:/Competition/student_grant/input/lunch_info.csv')

    # dinner_info 选取了17-19点作为吃午饭的数据
    sql = "SELECT t.sid AS id,REPLACE(SUBSTR(t.date,1,10),'-','') AS days,t.u_fee,t.r_fee FROM card_train t WHERE t.c3='食堂' AND REPLACE(SUBSTR(t.date,12,5),':','')>1700 AND REPLACE(SUBSTR(t.date,12,5),':','')<1900"
    dinner_train = pd.read_sql(sql, conn, index_col=None)

    sql = "SELECT t.sid AS id,REPLACE(SUBSTR(t.date,1,10),'-','') AS days,t.u_fee,t.r_fee FROM card_test t WHERE t.c3='食堂' AND REPLACE(SUBSTR(t.date,12,5),':','')>1700 AND REPLACE(SUBSTR(t.date,12,5),':','')<1900"
    dinner_test = pd.read_sql(sql, conn, index_col=None)
    print "sql completed"
    dinner_all = pd.concat([dinner_train, dinner_test])
    dinner_all['u_fee'] = dinner_all['u_fee'].apply(lambda x: float(x))
    dinner_temp = pd.DataFrame(dinner_all.groupby(['id', 'days'])['r_fee'].count())
    dinner_temp['u_fee'] = dinner_all.groupby(['id', 'days'])['u_fee'].sum()
    dinner_temp.to_csv('D:/Competition/student_grant/input/temp.csv')
    dinner_temp = pd.read_csv('D:/Competition/student_grant/input/temp.csv')

    dinner_info = pd.DataFrame(dinner_temp.groupby(['id'])['u_fee'].count())
    dinner_info['fee_sum'] = dinner_temp.groupby(['id'])['u_fee'].sum()
    dinner_info['fee_avg'] = dinner_temp.groupby(['id'])['u_fee'].mean()
    dinner_info['fee_max'] = dinner_temp.groupby(['id'])['u_fee'].max()

    dinner_info.to_csv('D:/Competition/student_grant/input/dinner_info.csv')

    # late_night_info 选取了19-22点作为吃午饭的数据
    sql = "SELECT t.sid AS id,REPLACE(SUBSTR(t.date,1,10),'-','') AS days,t.u_fee,t.r_fee FROM card_train t WHERE t.c3='食堂' AND REPLACE(SUBSTR(t.date,12,5),':','')>1900 AND REPLACE(SUBSTR(t.date,12,5),':','')<2200"
    late_night_train = pd.read_sql(sql, conn, index_col=None)

    sql = "SELECT t.sid AS id,REPLACE(SUBSTR(t.date,1,10),'-','') AS days,t.u_fee,t.r_fee FROM card_test t WHERE t.c3='食堂' AND REPLACE(SUBSTR(t.date,12,5),':','')>1900 AND REPLACE(SUBSTR(t.date,12,5),':','')<2200"
    late_night_test = pd.read_sql(sql, conn, index_col=None)
    print "sql completed"
    late_night_all = pd.concat([late_night_train, late_night_test])
    late_night_all['u_fee'] = late_night_all['u_fee'].apply(lambda x: float(x))
    late_night_temp = pd.DataFrame(late_night_all.groupby(['id', 'days'])['r_fee'].count())
    late_night_temp['u_fee'] = late_night_all.groupby(['id', 'days'])['u_fee'].sum()
    late_night_temp.to_csv('D:/Competition/student_grant/input/temp.csv')
    late_night_temp = pd.read_csv('D:/Competition/student_grant/input/temp.csv')

    late_night_info = pd.DataFrame(late_night_temp.groupby(['id'])['u_fee'].count())
    late_night_info['fee_sum'] = late_night_temp.groupby(['id'])['u_fee'].sum()
    late_night_info['fee_avg'] = late_night_temp.groupby(['id'])['u_fee'].mean()
    late_night_info['fee_max'] = late_night_temp.groupby(['id'])['u_fee'].max()

    late_night_info.to_csv('D:/Competition/student_grant/input/late_night_info.csv')


meal_info()
# d_s_info = pd.read_csv('D:/Competition/student_grant/input/d_s_info.csv')
