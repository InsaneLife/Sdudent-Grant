# coding=utf8
import MySQLdb
import pandas as pd

conn = MySQLdb.connect(host="localhost", user="root", passwd="root", db="student_grant", charset="utf8")

sql = 'SELECT * from  id_all_how_2_1'
rank_amount = pd.read_sql(sql, conn, index_col=None)
rank_amount['id'] = rank_amount['id'].astype('int')
id_all_how = pd.read_csv('D:/Competition/student_grant/input/id_all_how.csv')
id_all_how_rank = pd.merge(id_all_how, rank_amount, how='left', on='id')

id_all_how_rank['a_st_c_rank_order'] = id_all_how_rank['a_sum_st_c_rank'] / id_all_how_rank['college_num']
id_all_how_rank['a_st_c_rank_order'] = id_all_how_rank['a_st_c_rank_order'].fillna(-1)
# id_all_how_rank['a_st_c_rank_order_c'] = id_all_how_rank['a_st_c_rank_order'].apply(lambda x: int(round(x * 100, 0)))

id_all_how_rank['a_cs_c_rank_order'] = id_all_how_rank['a_sum_cs_c_rank'] / id_all_how_rank['college_num']
id_all_how_rank['a_cs_c_rank_order'] = id_all_how_rank['a_cs_c_rank_order'].fillna(-1)
# id_all_how_rank['a_cs_c_rank_order_c'] = id_all_how_rank['a_cs_c_rank_order'].apply(lambda x: int(round(x * 100, 0)))


del id_all_how_rank['college_num']

id_all_how_rank.to_csv('D:/Competition/student_grant/input/id_all_how_rank.csv')
