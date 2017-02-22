# coding = utf8
import pandas as pd


# card
card_train = pd.read_table('D:/Competition/student_grant/train/card_train.txt',sep=',',header=-1)
card_train.columns = ['id','consume','where','how','time','amount','remainder']




card = pd.DataFrame(card_train.groupby(['id'])['consume'].count())
card['consumesum'] = card_train.groupby(['id'])['amount'].sum()
card['consumeavg'] = card_train.groupby(['id'])['amount'].mean()
card['consumemax'] = card_train.groupby(['id'])['amount'].max()
card['remaindersum'] = card_train.groupby(['id'])['remainder'].sum()
card['remainderavg'] = card_train.groupby(['id'])['remainder'].mean()
card['remaindermax'] = card_train.groupby(['id'])['remainder'].max()

card.to_csv('D:/Competition/student_grant/input/train/card.csv')