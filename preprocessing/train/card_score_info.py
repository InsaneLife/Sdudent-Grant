# coding=utf8
import MySQLdb
import pandas as pd

# conn = MySQLdb.connect(host="localhost", user="root", passwd="root", db="student_grant", charset="utf8")

# score
score_train = pd.read_table('D:/Competition/student_grant/train/score_train.txt', sep=',', header=-1)
score_train.columns = ['id', 'college', 'score']

college = pd.DataFrame(score_train.groupby(['college'])['score'].max())
college.to_csv('D:/Competition/student_grant/input/train/college.csv', index=True)
college = pd.read_csv('D:/Competition/student_grant/input/train/college.csv')
college.columns = ['college', 'num']

score_train = pd.merge(score_train, college, how='left', on='college')
score_train['order'] = score_train['score'] / score_train['num']
score_train.to_csv('D:/Competition/student_grant/input/train//score_train.csv',index=False)
print s

# card
card_train = pd.read_table('D:/Competition/student_grant/train/card_train.txt', sep=',', header=-1)
card_train.columns = ['id', 'consume', 'where', 'how', 'time', 'amount', 'remainder']

# # in case memory overflow
# del card_train['where']
# del card_train['how']
# del card_train['time']
# del card_train['remainder']

# card = pd.DataFrame(card_train_test.groupby(['id'])['consume'].count())
# card['consumesum'] = card_train_test.groupby(['id'])['amount'].sum()
# card['consumeavg'] = card_train_test.groupby(['id'])['amount'].mean()
# card['consumemax'] = card_train_test.groupby(['id'])['amount'].max()
# card['remaindersum'] = card_train_test.groupby(['id'])['remainder'].sum()
# card['remainderavg'] = card_train_test.groupby(['id'])['remainder'].mean()
# card['remaindermax'] = card_train_test.groupby(['id'])['remainder'].max()

card = pd.read_csv('D:/Competition/student_grant/input/train/card.csv')

# get school mean consume
card_train = pd.merge(card_train, score_train, how='left', on='id')
card_s = pd.DataFrame()
card_s['school_avg'] = card_train.groupby(['college'])['amount'].mean()
card_s.to_csv('D:/Competition/student_grant/input/temp.csv', index=True)
card_s = pd.read_csv('D:/Competition/student_grant/input/temp.csv')
score_train = pd.merge(score_train, card_s, how='left', on='college')
card_score = pd.merge(card, score_train, how='left', on='id')
card_score['exceed_s_avg'] = card_score['consumeavg'] - card_score['school_avg']

card_score.to_csv('D:/Competition/student_grant/input/train/card_score.csv')
