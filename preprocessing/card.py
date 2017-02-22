# coding=utf8
import pandas as pd

# card
card_train = pd.read_table('D:/Competition/student_grant/train/card_train.txt', sep=',', header=-1)
card_train.columns = ['id', 'consume', 'where', 'how', 'time', 'amount', 'remainder']
card_test = pd.read_table('D:/Competition/student_grant/test/card_test.txt', sep=',', header=-1)
card_test.columns = ['id', 'consume', 'where', 'how', 'time', 'amount', 'remainder']
card_train_test = pd.concat([card_train, card_test])


card = pd.DataFrame()
card['id_count'] = card_train_test.groupby(['id'])['consume'].count()
card['amount_sum'] = card_train_test.groupby(['id'])['amount'].sum()
card['amount_avg'] = card_train_test.groupby(['id'])['amount'].mean()
card['amount_max'] = card_train_test.groupby(['id'])['amount'].max()
card['remain_sum'] = card_train_test.groupby(['id'])['remainder'].sum()
card['remain_avg'] = card_train_test.groupby(['id'])['remainder'].mean()
card['remain_max'] = card_train_test.groupby(['id'])['remainder'].max()

card_train_test = card_train_test[card_train_test['how'].notnull()]
card['p_sum'] = card_train_test.groupby(['id'])['amount'].sum()
card['p_avg'] = card_train_test.groupby(['id'])['amount'].mean()
card['p_max'] = card_train_test.groupby(['id'])['amount'].max()
card['p_r_sum'] = card_train_test.groupby(['id'])['remainder'].sum()
card['p_r_avg'] = card_train_test.groupby(['id'])['remainder'].mean()
card['p_r_max'] = card_train_test.groupby(['id'])['remainder'].max()

# 按照天数来做
card_train_test['time'] = card_train_test['time'].apply(lambda x: x[:10])
card_temp = pd.DataFrame()
card_temp["day_num"] = card_train_test.groupby(['id', 'time'])['consume'].count()
card_temp["amount_sum"] = card_train_test.groupby(['id', 'time'])['amount'].sum()
card_temp["r_avg"] = card_train_test.groupby(['id', 'time'])['remainder'].mean()
card_temp["r_max"] = card_train_test.groupby(['id', 'time'])['remainder'].max()
# 释放内存
del card_train_test
card_temp.to_csv('D:/Competition/student_grant/input/temp.csv')
card_temp = pd.read_csv('D:/Competition/student_grant/input/temp.csv')

card["day_count"] = card_temp.groupby(['id'])['amount_sum'].count()
card["day_amonut_avg"] = card_temp.groupby(['id'])['amount_sum'].mean()
card["day_amonut_max"] = card_temp.groupby(['id'])['amount_sum'].max()
card["day_remain_avg"] = card_temp.groupby(['id'])['r_avg'].mean()
card["day_remain_mavg"] = card_temp.groupby(['id'])['r_max'].mean()

card.to_csv('D:/Competition/student_grant/input/card1.csv', index=True)
