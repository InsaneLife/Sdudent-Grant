# coding=utf8
import MySQLdb
import pandas as pd

# conn = MySQLdb.connect(host="localhost", user="root", passwd="root", db="student_grant", charset="utf8")


# score
score_test = pd.read_table('D:/Competition/student_grant/test/score_test.txt', sep=',', header=-1)
score_test.columns = ['id', 'college', 'score']

college = pd.DataFrame(score_test.groupby(['college'])['score'].max())
college.to_csv('D:/Competition/student_grant/input/test/college.csv', index=True)
college = pd.read_csv('D:/Competition/student_grant/input/test/college.csv')
college.columns = ['college', 'num']

score_test = pd.merge(score_test, college, how='left', on='college')
score_test['order'] = score_test['score'] / score_test['num']

# card
card_test = pd.read_table('D:/Competition/student_grant/test/card_test.txt', sep=',', header=-1)
card_test.columns = ['id', 'consume', 'where', 'how', 'time', 'amount', 'remainder']

# # in case memory overflow
# del card_test['where']
# del card_test['how']
# del card_test['time']
# del card_test['remainder']

# card = pd.DataFrame(card_test_test.groupby(['id'])['consume'].count())
# card['consumesum'] = card_test_test.groupby(['id'])['amount'].sum()
# card['consumeavg'] = card_test_test.groupby(['id'])['amount'].mean()
# card['consumemax'] = card_test_test.groupby(['id'])['amount'].max()
# card['remaindersum'] = card_test_test.groupby(['id'])['remainder'].sum()
# card['remainderavg'] = card_test_test.groupby(['id'])['remainder'].mean()
# card['remaindermax'] = card_test_test.groupby(['id'])['remainder'].max()

card = pd.read_csv('D:/Competition/student_grant/input/test/card.csv')

# get school mean consume
card_test = pd.merge(card_test, score_test, how='left', on='id')
card_s = pd.DataFrame()
card_s['school_avg'] = card_test.groupby(['college'])['amount'].mean()
card_s.to_csv('D:/Competition/student_grant/input/temp.csv', index=True)
card_s = pd.read_csv('D:/Competition/student_grant/input/temp.csv')
score_test = pd.merge(score_test, card_s, how='left', on='college')
card_score = pd.merge(card, score_test, how='left', on='id')
card_score['exceed_s_avg'] = card_score['consumeavg'] - card_score['school_avg']

card_score.to_csv('D:/Competition/student_grant/input/test/card_score.csv')