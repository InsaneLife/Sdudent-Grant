# coding=utf8
import pandas as pd
from pandas import Series, DataFrame
import numpy as np

ser = Series([3, 2, 0, 3], index=list('abcd'))
df2 = DataFrame(np.arange(16).reshape((4, 4)), columns=['one', 'two', 'three', 'four'])

print df2
df3 = df2.loc[:, ['two']]
df3 = df3.rank(axis=0, method='min', ascending=False)
df3['one'] = df2['one']
print df3
df4 = pd.merge(df2, df3, how='left',on='one')
print df4

# card
card_train = pd.read_table('D:/Competition/student_grant/train/card_train.txt', sep=',', header=-1)
card_train.columns = ['id', 'consume', 'where', 'how', 'time', 'amount', 'remainder']
card_test = pd.read_table('D:/Competition/student_grant/test/card_test.txt', sep=',', header=-1)
card_test.columns = ['id', 'consume', 'where', 'how', 'time', 'amount', 'remainder']
card_train_test = pd.concat([card_train, card_test])
del card_train, card_test

cc = DataFrame(card_train_test.groupby(['id'])['consume'].count())
print cc.shape