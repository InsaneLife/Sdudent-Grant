# coding=utf8
import MySQLdb
import pandas as pd

conn = MySQLdb.connect(host="localhost", user="root", passwd="root", db="student_grant", charset="utf8")


def set_id_how():
    card_test = pd.read_table('D:/Competition/student_grant/test/card_test.txt', sep=',', header=-1)
    card_test.columns = ['id', 'consume', 'where', 'how', 'time', 'amount', 'remainder']
    id_how = pd.DataFrame(card_test.groupby(['id', 'how'])['consume'].count())
    id_how['a_sum'] = card_test.groupby(['id', 'how'])['amount'].sum()
    id_how['a_avg'] = card_test.groupby(['id', 'how'])['amount'].mean()
    id_how['a_max'] = card_test.groupby(['id', 'how'])['amount'].max()
    id_how.to_csv('D:/Competition/student_grant/input/test/id_how.csv', index=True)


def card_how():
    sql = 'SELECT id FROM id_how_te group by id '
    id_info = pd.read_sql(sql, conn, index_col=None)

    sql = "SELECT i.* FROM id_how_te i WHERE i.how = '食堂'"
    s_st = pd.read_sql(sql, conn, index_col=None)
    del s_st['how']
    id_info = pd.merge(id_info, s_st, how='left', on='id')

    sql = "SELECT * FROM id_how_te i WHERE i.how = '开水'"
    s_ks = pd.read_sql(sql, conn)
    del s_ks['how']
    id_info = pd.merge(id_info, s_ks, how='left', on='id')

    sql = "SELECT * FROM id_how_te i WHERE i.how = '淋浴'"
    s_ks = pd.read_sql(sql, conn)
    del s_ks['how']
    id_info = pd.merge(id_info, s_ks, how='left', on='id')

    sql = "SELECT * FROM id_how_te i WHERE i.how = '校车'"
    s_ks = pd.read_sql(sql, conn)
    del s_ks['how']
    id_info = pd.merge(id_info, s_ks, how='left', on='id')

    sql = "SELECT * FROM id_how_te i WHERE i.how = '超市'"
    s_ks = pd.read_sql(sql, conn)
    del s_ks['how']
    id_info = pd.merge(id_info, s_ks, how='left', on='id')

    sql = "SELECT * FROM id_how_te i WHERE i.how = '洗衣房'"
    s_ks = pd.read_sql(sql, conn)
    del s_ks['how']
    id_info = pd.merge(id_info, s_ks, how='left', on='id')

    sql = "SELECT * FROM id_how_te i WHERE i.how = '图书馆'"
    s_ks = pd.read_sql(sql, conn)
    del s_ks['how']
    id_info = pd.merge(id_info, s_ks, how='left', on='id')

    sql = "SELECT * FROM id_how_te i WHERE i.how = '文印中心'"
    s_ks = pd.read_sql(sql, conn)
    del s_ks['how']
    id_info = pd.merge(id_info, s_ks, how='left', on='id')


    # id_info.columns = ['id',"h0","h1","h2","h3","h4","h5","h6","h7","h8","h9","h10","h11","h12","h13","h14","h15","h16","h17","h18","h19","h20","h21","h22","h23","h24","h25","h26","h27","h28","h29","h30","h31"]
    # print id_info
    id_info.to_csv('D:/Competition/student_grant/input/test/id_info.csv', index=False)
    return id_info





set_id_how()

# id_info = card_how()


# s_info= pd.read_csv('D:/Competition/student_grant/input/s_info.csv')
# print s_info


# card_train = pd.read_table('D:/Competition/student_grant/train/card_train.txt',sep=',',header=-1)
# card_train.columns = ['id','consume','where','how','time','amount','remainder']
# card_test = pd.read_table('D:/Competition/student_grant/test/card_test.txt',sep=',',header=-1)
# card_test.columns = ['id','consume','where','how','time','amount','remainder']
# card_train_test = pd.concat([card_train,card_test])
#
# test = pd.DataFrame(card_train_test.groupby(['id','how'])['how'].count())
# test['amount_sum'] = card_train_test.groupby(['id','how'])['amount'].sum()
# test['amount_avg'] = card_train_test.groupby(['id','how'])['amount'].mean()
# test['amount_max'] = card_train_test.groupby(['id','how'])['amount'].max()
#
# test.to_csv('D:/Competition/student_grant/input/id_how.csv',index=True)
