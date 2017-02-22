# -*-coding:utf-8 -*-
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier

# train_test D:/Competition/student_grant
train = pd.read_table('D:/Competition/student_grant/train/subsidy_train.txt',sep=',',header=-1)
train.columns = ['id','money']
test = pd.read_table('D:/Competition/student_grant/test/subsidy_test.txt',sep=',',header=-1)
test.columns = ['id']
test['money'] = np.nan
train_test = pd.concat([train,test])

# score
score_train = pd.read_table('D:/Competition/student_grant/train/score_train.txt',sep=',',header=-1)
score_train.columns = ['id','college','score']
score_test = pd.read_table('D:/Competition/student_grant/test/score_test.txt',sep=',',header=-1)
score_test.columns = ['id','college','score']
score_train_test = pd.concat([score_train,score_test])

college = pd.DataFrame(score_train_test.groupby(['college'])['score'].max())
college.to_csv('D:/Competition/student_grant/input/college_t.csv',index=True)
college = pd.read_csv('D:/Competition/student_grant/input/college_t.csv')
college.columns = ['college','num']

score_train_test = pd.merge(score_train_test, college, how='left',on='college')
score_train_test['order'] = score_train_test['score']/score_train_test['num']
train_test = pd.merge(train_test,score_train_test,how='left',on='id')

# card
card_train = pd.read_table('D:/Competition/student_grant/train/card_train.txt',sep=',',header=-1)
card_train.columns = ['id','consume','where','how','time','amount','remainder']
card_test = pd.read_table('D:/Competition/student_grant/test/card_test.txt',sep=',',header=-1)
card_test.columns = ['id','consume','where','how','time','amount','remainder']
card_train_test = pd.concat([card_train,card_test])

card = pd.DataFrame(card_train_test.groupby(['id'])['consume'].count())
card['consumesum'] = card_train_test.groupby(['id'])['amount'].sum()
card['consumeavg'] = card_train_test.groupby(['id'])['amount'].mean()
card['consumemax'] = card_train_test.groupby(['id'])['amount'].max()
card['remaindersum'] = card_train_test.groupby(['id'])['remainder'].sum()
card['remainderavg'] = card_train_test.groupby(['id'])['remainder'].mean()
card['remaindermax'] = card_train_test.groupby(['id'])['remainder'].max()

card.to_csv('D:/Competition/student_grant/input/card_t.csv',index=True)
card = pd.read_csv('D:/Competition/student_grant/input/card_t.csv')
train_test = pd.merge(train_test, card, how='left',on='id')

train = train_test[train_test['money'].notnull()]
test = train_test[train_test['money'].isnull()]

train = train.fillna(-1)
test = test.fillna(-1)
target = 'money'
IDcol = 'id'
ids = test['id'].values
predictors = [x for x in train.columns if x not in [target]]

# Oversample
Oversampling1000 = train.loc[train.money == 1000]
Oversampling1500 = train.loc[train.money == 1500]
Oversampling2000 = train.loc[train.money == 2000]
for i in range(5):
    train = train.append(Oversampling1000)
for j in range(8):
    train = train.append(Oversampling1500)
for k in range(10):
    train = train.append(Oversampling2000)

# model
# (n_estimators=200,random_state=2016)
clf = GradientBoostingClassifier(n_estimators=200, learning_rate=0.1, max_depth=4, random_state=2016)
# clf = RandomForestClassifier(n_estimators=500,random_state=2016)
clf = clf.fit(train[predictors],train[target])
result = clf.predict(test[predictors])

# Save results
test_result = pd.DataFrame(columns=["studentid","subsidy"])
test_result.studentid = ids
test_result.subsidy = result
test_result.subsidy = test_result.subsidy.apply(lambda x:int(x))

print '1000--'+str(len(test_result[test_result.subsidy==1000])) + ':741'
print '1500--'+str(len(test_result[test_result.subsidy==1500])) + ':465'
print '2000--'+str(len(test_result[test_result.subsidy==2000])) + ':354'

test_result.to_csv("D:/Competition/student_grant/s_2016.csv",index=False)

# '''