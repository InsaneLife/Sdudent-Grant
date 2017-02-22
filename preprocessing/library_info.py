# coding=utf8
import MySQLdb
import pandas as pd

conn = MySQLdb.connect(host="localhost", user="root", passwd="root", db="student_grant", charset="utf8")


def library_in_out():
    # 选取了开学前两个月的进出图书馆的数据。
    sql = 'SELECT l.sid AS id,l.c2 FROM library_train l  WHERE SUBSTR(l.date,6,2) IN (2,3,9,10)'
    lib_train = pd.read_sql(sql, conn, index_col=None)

    sql = 'SELECT l.sid AS id,l.c2 FROM library_test l  WHERE SUBSTR(l.date,6,2) IN (2,3,9,10)'
    lib_test = pd.read_sql(sql, conn, index_col=None)

    lib_all = pd.concat([lib_train, lib_test])
    lib_info = pd.DataFrame(lib_all.groupby(['id'])['c2'].count())
    lib_info.to_csv('D:/Competition/student_grant/input/lib_info.csv')


library_in_out()
# d_s_info = pd.read_csv('D:/Competition/student_grant/input/d_s_info.csv')
