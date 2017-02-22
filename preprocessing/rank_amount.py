# coding=utf8
import MySQLdb
import pandas as pd

conn = MySQLdb.connect(host="localhost", user="root", passwd="root", db="student_grant", charset="utf8")

sql = 'SELECT * from  rank_amount'
rank_amount = pd.read_sql(sql, conn, index_col=None)
rank_amount['id'] = rank_amount['id'].astype('int')
del rank_amount['college_num']
card_score= pd.read_csv('D:/Competition/student_grant/input/card_score.csv')
card_score_rank = pd.merge(card_score, rank_amount, how='left', on='id')

card_score_rank['a_c_rank_order'] = card_score_rank['amount_sum_college_rank'] / card_score_rank['college_num']
card_score_rank['a_c_rank_order'] = card_score_rank['a_c_rank_order'].fillna(-0.01)
card_score_rank['a_c_rank_order_c'] = card_score_rank['a_c_rank_order'].apply(lambda x: int(round(x * 100, 0)))
card_score_rank['p_c_rank_order'] = card_score_rank['p_sum_college_rank'] / card_score_rank['college_num']
card_score_rank['p_c_rank_order'] = card_score_rank['p_c_rank_order'].fillna(-0.01)
card_score_rank['p_c_rank_order_c'] = card_score_rank['p_c_rank_order'].apply(lambda x: int(round(x * 100, 0)))

card_score_rank.to_csv('D:/Competition/student_grant/input/card_score_rank.csv')
