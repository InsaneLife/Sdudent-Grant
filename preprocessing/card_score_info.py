# coding=utf8
import MySQLdb
import pandas as pd

# conn = MySQLdb.connect(host="localhost", user="root", passwd="root", db="student_grant", charset="utf8")

# score
score_train = pd.read_table('D:/Competition/student_grant/train/score_train.txt', sep=',', header=-1)
score_train.columns = ['id', 'college', 'score']
score_test = pd.read_table('D:/Competition/student_grant/test/score_test.txt', sep=',', header=-1)
score_test.columns = ['id', 'college', 'score']
score_train_test = pd.concat([score_train, score_test])

college = pd.DataFrame(score_train_test.groupby(['college'])['score'].max())
college.to_csv('D:/Competition/student_grant/input/college.csv', index=True)
college = pd.read_csv('D:/Competition/student_grant/input/college.csv')
college.columns = ['college', 'college_num']

score_train_test = pd.merge(score_train_test, college, how='left', on='college')
score_train_test['order'] = score_train_test['score'] / score_train_test['college_num']
score_train_test['order_c'] = score_train_test['order'].apply(lambda x: int(round(x * 10, 0)))
score_train_test.to_csv('D:/Competition/student_grant/input/score_train_test.csv')

# card
card_train = pd.read_table('D:/Competition/student_grant/train/card_train.txt', sep=',', header=-1)
card_train.columns = ['id', 'consume', 'where', 'how', 'time', 'amount', 'remainder']
card_test = pd.read_table('D:/Competition/student_grant/test/card_test.txt', sep=',', header=-1)
card_test.columns = ['id', 'consume', 'where', 'how', 'time', 'amount', 'remainder']
card_train_test = pd.concat([card_train, card_test])
card_train_test = card_train_test[card_train_test['how'].notnull()]
# in case memory overflow
del card_train_test['where']
del card_train_test['how']
del card_train_test['consume']

# card = pd.DataFrame(card_train_test.groupby(['id'])['consume'].count())
# card['consumesum'] = card_train_test.groupby(['id'])['amount'].sum()
# card['consumeavg'] = card_train_test.groupby(['id'])['amount'].mean()
# card['consumemax'] = card_train_test.groupby(['id'])['amount'].max()
# card['remaindersum'] = card_train_test.groupby(['id'])['remainder'].sum()
# card['remainderavg'] = card_train_test.groupby(['id'])['remainder'].mean()
# card['remaindermax'] = card_train_test.groupby(['id'])['remainder'].max()

card = pd.read_csv('D:/Competition/student_grant/input/card1.csv')

# get school mean consume
card_train_test = pd.merge(card_train_test, score_train_test, how='left', on='id')
card_s = pd.DataFrame()
card_s['school_avg'] = card_train_test.groupby(['college'])['amount'].mean()
card_s['school_sum'] = card_train_test.groupby(['college'])['amount'].sum()
card_s['school_max'] = card_train_test.groupby(['college'])['amount'].max()
card_s['school_r_max'] = card_train_test.groupby(['college'])['remainder'].max()
card_s['school_r_mean'] = card_train_test.groupby(['college'])['remainder'].mean()
card_s.to_csv('D:/Competition/student_grant/input/temp.csv', index=True)
card_s = pd.read_csv('D:/Competition/student_grant/input/temp.csv')
score_train_test = pd.merge(score_train_test, card_s, how='left', on='college')

card_score = pd.merge(card, score_train_test, how='left', on='id')
del card, score_train_test, card_s
card_score['exceed_s_avg'] = card_score['p_avg'] - card_score['school_avg']

# get school day mean consume
card_train_test['time'] = card_train_test['time'].apply(lambda x: x[:10])
card_temp = pd.DataFrame()
card_temp["amount_sum"] = card_train_test.groupby(['college', 'time'])['amount'].sum()
del card_train_test
card_temp.to_csv('D:/Competition/student_grant/input/temp.csv')
card_temp = pd.read_csv('D:/Competition/student_grant/input/temp.csv')
card_s = pd.DataFrame()
card_s['school_day_avg'] = card_temp.groupby(['college'])['amount_sum'].mean()
card_s['school_day_max'] = card_temp.groupby(['college'])['amount_sum'].max()
card_s.to_csv('D:/Competition/student_grant/input/temp.csv')
card_s = pd.read_csv('D:/Competition/student_grant/input/temp.csv')
card_score = pd.merge(card_score, card_s, how='left', on='college')
card_score['exceed_s_day_avg'] = card_score['day_amonut_avg'] - card_score['school_day_avg']

card_score.to_csv('D:/Competition/student_grant/input/card_score.csv', index=False)
