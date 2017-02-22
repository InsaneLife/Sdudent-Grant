# coding=utf8
import MySQLdb
import pandas as pd

conn = MySQLdb.connect(host="localhost", user="root", passwd="root", db="student_grant", charset="utf8")


def dorm_moring_in_out():
    sql = 'SELECT id id FROM id_how group by id '
    d_s_info = pd.read_sql(sql, conn, index_col=None)
    #s_info.colums = ['id']

    sql = "SELECT d.sid id FROM dorm_train d WHERE d.direction=1 and REPLACE(SUBSTR(d.date,12,20),':','')>60000 AND REPLACE(SUBSTR(d.date,12,20),':','')<83000"
    test = pd.read_sql(sql, conn, index_col=None)
    dm_out = pd.DataFrame()
    dm_out['num'] = test.groupby(['id'])['id'].count()
    dm_out.to_csv('D:/Competition/student_grant/input/temp.csv', index=True)
    dm_out = pd.read_csv('D:/Competition/student_grant/input/temp.csv')
    d_s_info = pd.merge(d_s_info, dm_out, how='left', on='id')

    sql = "SELECT d.sid id FROM dorm_train d WHERE d.direction=0 and REPLACE(SUBSTR(d.date,12,20),':','')>60000 AND REPLACE(SUBSTR(d.date,12,20),':','')<90000"
    test = pd.read_sql(sql, conn, index_col=None)
    dm_in = pd.DataFrame()
    dm_in['num'] = test.groupby(['id'])['id'].count()
    dm_in.to_csv('D:/Competition/student_grant/input/temp.csv', index=True)
    dm_in = pd.read_csv('D:/Competition/student_grant/input/temp.csv')
    d_s_info = pd.merge(d_s_info, dm_in, how='left', on='id')

    # fill null as 0
    d_s_info = d_s_info.fillna(0)
    d_s_info['num_a'] = d_s_info['num_x'] - d_s_info['num_y']
    d_s_info.to_csv('D:/Competition/student_grant/input/d_s_info.csv', index=False)



dorm_moring_in_out()
# d_s_info = pd.read_csv('D:/Competition/student_grant/input/d_s_info.csv')