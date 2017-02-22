# coding=utf8
import pandas as pd
import numpy as np
from sklearn.ensemble import GradientBoostingClassifier
from sklearn import preprocessing

# train_test D:/Competition/student_grant
train = pd.read_csv('D:/Competition/student_grant/input/train/train.csv')
test = pd.read_csv('D:/Competition/student_grant/input/test/test.csv')

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
clf = GradientBoostingClassifier(n_estimators=450, learning_rate=0.01, max_depth=8, random_state=2016)
# (n_estimators=300, learning_rate=0.01,max_depth=5,loss='exponential', random_state=2016)

# data preprocessing ...
# scaler = preprocessing.StandardScaler().fit(train[predictors])
# train[predictors] = scaler.transform(train[predictors])
# test[predictors] = scaler.transform(test[predictors])

# training
clf = clf.fit(train[predictors], train[target])
result = clf.predict(test[predictors])

# Save results
test_result = pd.DataFrame(columns=["studentid", "subsidy"])
test_result.studentid = ids
test_result.subsidy = result
test_result.subsidy = test_result.subsidy.apply(lambda x: int(x))

print '1000--' + str(len(test_result[test_result.subsidy == 1000])) + ':741'
print '1500--' + str(len(test_result[test_result.subsidy == 1500])) + ':465'
print '2000--' + str(len(test_result[test_result.subsidy == 2000])) + ':354'

test_result.to_csv("D:/Competition/student_grant/s_part_2.csv", index=False)

# '''
