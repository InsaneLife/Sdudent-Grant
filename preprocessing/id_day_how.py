# coding=utf8
import pandas as pd

# card
card_train = pd.read_table('D:/Competition/student_grant/train/card_train.txt', sep=',', header=-1)
card_train.columns = ['id', 'consume', 'where', 'how', 'time', 'amount', 'remainder']
card_test = pd.read_table('D:/Competition/student_grant/test/card_test.txt', sep=',', header=-1)
card_test.columns = ['id', 'consume', 'where', 'how', 'time', 'amount', 'remainder']
card_train_test = pd.concat([card_train, card_test])
del card_train, card_test
card_train_test = card_train_test[card_train_test['how'].notnull()]
del card_train_test['where']
del card_train_test['remainder']

card_train_test['time'] = card_train_test['time'].apply(lambda x: x[:10].replace('/', ''))
card_temp = pd.DataFrame()
card_temp["day_num"] = card_train_test.groupby(['id', 'time', 'how'])['consume'].count()
card_temp["amount_sum"] = card_train_test.groupby(['id', 'time', 'how'])['amount'].sum()
del card_train_test

card_temp.to_csv('D:/Competition/student_grant/input/temp.csv')
card_temp = pd.read_csv('D:/Competition/student_grant/input/temp.csv')
card_day_how = pd.DataFrame()
card_day_how["day_num"] = card_temp.groupby(['id', 'how'])["id"].count()
card_day_how["amount_avg"] = card_temp.groupby(['id', 'how'])["amount_sum"].mean()
card_day_how["amount_max"] = card_temp.groupby(['id', 'how'])["amount_sum"].max()
card_day_how["day_num_maen"] = card_temp.groupby(['id', 'how'])["day_num"].mean()
card_day_how["day_num_max"] = card_temp.groupby(['id', 'how'])["day_num"].max()
card_day_how.to_csv('D:/Competition/student_grant/input/temp.csv')
card_day_how = pd.read_csv('D:/Competition/student_grant/input/temp.csv')
del card_temp

# main
id_day_how = pd.DataFrame()
id_day_how['num'] = card_day_how.groupby(['id'])['id'].count()
id_day_how.to_csv('D:/Competition/student_grant/input/id_day_how.csv')
id_day_how = pd.read_csv('D:/Competition/student_grant/input/id_day_how.csv')

temp = card_day_how[card_day_how['how'] == "食堂"]
del temp['how']
id_day_how = pd.merge(id_day_how, temp, how='left', on='id')

temp = card_day_how[card_day_how['how'] == "开水"]
del temp['how']
id_day_how = pd.merge(id_day_how, temp, how='left', on='id')
del temp['amount_avg'], temp['amount_max'], temp['day_num_max']

temp = card_day_how[card_day_how['how'] == "淋浴"]
del temp['how']
id_day_how = pd.merge(id_day_how, temp, how='left', on='id')
del temp['amount_avg'], temp['amount_max'], temp['day_num_max']

temp = card_day_how[card_day_how['how'] == "超市"]
del temp['how']
id_day_how = pd.merge(id_day_how, temp, how='left', on='id')

id_day_how.to_csv('D:/Competition/student_grant/input/id_day_how.csv', index=False)
