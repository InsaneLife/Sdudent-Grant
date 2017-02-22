#coding=utf8
import pandas as pd

card_train = pd.read_table('D:/Competition/student_grant/train/card_train.txt',sep=',',header=-1)
card_train.columns = ['id','consume','where','how','time','amount','remainder']
card_test = pd.read_table('D:/Competition/student_grant/test/card_test.txt',sep=',',header=-1)
card_test.columns = ['id','consume','where','how','time','amount','remainder']
card_train_test = pd.concat([card_train,card_test])

test = pd.DataFrame(card_train_test.groupby(['id','how'])['how'].count())
test['amount_sum'] = card_train_test.groupby(['id','how'])['amount'].sum()
test['amount_avg'] = card_train_test.groupby(['id','how'])['amount'].mean()
test['amount_max'] = card_train_test.groupby(['id','how'])['amount'].max()

test.to_csv('D:/Competition/student_grant/input/id_how.csv',index=True)