# coding=utf8
import MySQLdb
import pandas as pd


def set_id_how():
    card_train = pd.read_table('D:/Competition/student_grant/train/card_train.txt', sep=',', header=-1)
    card_train.columns = ['id', 'consume', 'where', 'how', 'time', 'amount', 'remainder']
    card_test = pd.read_table('D:/Competition/student_grant/test/card_test.txt', sep=',', header=-1)
    card_test.columns = ['id', 'consume', 'where', 'how', 'time', 'amount', 'remainder']
    card_train_test = pd.concat([card_train, card_test])
    del card_test, card_train
    id_how = pd.DataFrame()
    id_how['a_count'] = card_train_test.groupby(['id', 'how'])['id'].count()
    id_how['a_sum'] = card_train_test.groupby(['id', 'how'])['amount'].sum()
    id_how['a_avg'] = card_train_test.groupby(['id', 'how'])['amount'].mean()
    id_how['a_max'] = card_train_test.groupby(['id', 'how'])['amount'].max()
    id_how.to_csv('D:/Competition/student_grant/input/id_how.csv', index=True)
    id_how = pd.read_csv('D:/Competition/student_grant/input/id_how.csv')
    del card_train_test
    # main
    id_all_how = pd.DataFrame()
    id_all_how['num'] = id_how.groupby(['id'])['id'].count()
    id_all_how.to_csv('D:/Competition/student_grant/input/temp.csv')
    id_all_how = pd.read_csv('D:/Competition/student_grant/input/temp.csv')

    temp = id_how[id_how['how'] == "食堂"]
    del temp['how']
    id_all_how = pd.merge(id_all_how, temp, how='left', on='id')

    temp = id_how[id_how['how'] == "开水"]
    del temp['how']
    id_all_how = pd.merge(id_all_how, temp, how='left', on='id')
    del temp['a_sum'], temp['a_avg'], temp['a_max']

    temp = id_how[id_how['how'] == "淋浴"]
    del temp['how']
    id_all_how = pd.merge(id_all_how, temp, how='left', on='id')
    del temp['a_sum'], temp['a_avg'], temp['a_max']

    temp = id_how[id_how['how'] == "校车"]
    del temp['how']
    id_all_how = pd.merge(id_all_how, temp, how='left', on='id')
    del temp['a_sum'], temp['a_avg'], temp['a_max']

    temp = id_how[id_how['how'] == "超市"]
    del temp['how']
    id_all_how = pd.merge(id_all_how, temp, how='left', on='id')

    temp = id_how[id_how['how'] == "洗衣房"]
    del temp['how']
    id_all_how = pd.merge(id_all_how, temp, how='left', on='id')
    del temp['a_sum'], temp['a_avg'], temp['a_max']

    temp = id_how[id_how['how'] == "图书馆"]
    del temp['how']
    id_all_how = pd.merge(id_all_how, temp, how='left', on='id')

    temp = id_how[id_how['how'] == "文印中心"]
    del temp['how']
    id_all_how = pd.merge(id_all_how, temp, how='left', on='id')

    temp = id_how[id_how['how'] == "校医院"]
    del temp['how']
    id_all_how = pd.merge(id_all_how, temp, how='left', on='id')

    id_all_how = id_all_how.fillna(0)
    id_all_how.to_csv('D:/Competition/student_grant/input/id_all_how.csv')


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
