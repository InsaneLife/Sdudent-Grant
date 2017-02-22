# coding = utf8
import pandas as pd


# card
card_test = pd.read_table('D:/Competition/student_grant/test/card_test.txt',sep=',',header=-1)
card_test.columns = ['id','consume','where','how','time','amount','remainder']




card = pd.DataFrame(card_test.groupby(['id'])['consume'].count())
card['consumesum'] = card_test.groupby(['id'])['amount'].sum()
card['consumeavg'] = card_test.groupby(['id'])['amount'].mean()
card['consumemax'] = card_test.groupby(['id'])['amount'].max()
card['remaindersum'] = card_test.groupby(['id'])['remainder'].sum()
card['remainderavg'] = card_test.groupby(['id'])['remainder'].mean()
card['remaindermax'] = card_test.groupby(['id'])['remainder'].max()

card.to_csv('D:/Competition/student_grant/input/test/card.csv')