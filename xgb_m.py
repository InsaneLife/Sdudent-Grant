# coding=utf8
import pandas as pd
import numpy as np
import time
from sklearn.ensemble import GradientBoostingClassifier
from sklearn import preprocessing
from sklearn.cross_validation import train_test_split
from sklearn.metrics import classification_report
import xgboost as xgb
from sklearn.preprocessing import MinMaxScaler
import cPickle

# train_test D:/Competition/student_grant
train = pd.read_table('D:/Competition/student_grant/train/subsidy_train.txt', sep=',', header=-1)
train.columns = ['id', 'money']
test = pd.read_table('D:/Competition/student_grant/test/subsidy_test.txt', sep=',', header=-1)
test.columns = ['id']
test['money'] = np.nan
train_test = pd.concat([train, test])
del train, test

# other
train_other = pd.read_csv('D:/Competition/student_grant/other/alltr.csv')
test_other = pd.read_csv('D:/Competition/student_grant/other/allte.csv')
del train_other['subsidy']
train_test_other = pd.concat([train_other, test_other])
train_test = pd.merge(train_test, train_test_other, how='left', left_on='id', right_on='std_id')
print train_test_other.shape
del train_other, test_other, train_test_other, train_test['std_id']

# card_score
card_score = pd.read_csv('D:/Competition/student_grant/input/card_score_rank.csv')
train_test = pd.merge(train_test, card_score, how='left', on='id')
del card_score

# id_all_how #card of student info
id_all_how = pd.read_csv('D:/Competition/student_grant/input/id_all_how.csv')
train_test = pd.merge(train_test, id_all_how, how='left', on='id')
del id_all_how

# meal_info
# meal_info_rank = pd.read_csv('D:/Competition/student_grant/input/meal_info_rank.csv')
# train_test = pd.merge(train_test, meal_info_rank, how='left', on='id')
# del meal_info_rank

breakfast_info = pd.read_csv('D:/Competition/student_grant/input/breakfast_info.csv')
train_test = pd.merge(train_test, breakfast_info, how='left', on='id')
del breakfast_info
lunch_info = pd.read_csv('D:/Competition/student_grant/input/lunch_info.csv')
train_test = pd.merge(train_test, lunch_info, how='left', on='id')
del lunch_info
dinner_info = pd.read_csv('D:/Competition/student_grant/input/dinner_info.csv')
train_test = pd.merge(train_test, dinner_info, how='left', on='id')
del dinner_info
late_night_info = pd.read_csv('D:/Competition/student_grant/input/late_night_info.csv')
train_test = pd.merge(train_test, late_night_info, how='left', on='id')
del late_night_info

# lib_info
# lib_info = pd.read_csv('D:/Competition/student_grant/input/lib_info.csv')
# train_test = pd.merge(train_test, lib_info, how='left', on='id')




# dorm info
# d_s_info = pd.read_csv('D:/Competition/student_grant/input/d_s_info.csv')
# train_test = pd.merge(train_test, d_s_info, how='left',on='id')

train_test.to_csv('D:/Competition/student_grant/input/train_test.csv', index=False)

train = train_test[train_test['money'].notnull()]
test = train_test[train_test['money'].isnull()]

# merge
# train_p = pd.read_csv('D:/Competition/student_grant/input/train/train.csv')
# del train_p['money']
# train = pd.merge(train, train_p, how='left', on='id')
# test_p = pd.read_csv('D:/Competition/student_grant/input/test/test.csv')
# test = pd.merge(test, test_p, how='left', on='id')


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
# params = {'booster': 'gbtree',
#           'objective': 'multi:softmax',
#           'num_class': 4,
#           # 'eval_metric': 'auc',
#           'gamma': 0.1,
#           'min_child_weight': 1.1,
#           'max_depth': 5,
#           'lambda': 10,
#           'subsample': 0.7,
#           'colsample_bytree': 0.7,
#           'colsample_bylevel': 0.7,
#           'eta': 0.01,
#           'tree_method': 'exact',
#           'seed': 2016,
#           'nthread': 12
#           }
params = {
    'num_class': 4,
    'nthread': 4,
    'max_depth': 6,
    'eta': 0.1,
    'silent': 1,
    'seed': 2016,
    'objective': 'multi:softmax',
}

train[target] = train[target].replace(1000, 1)
train[target] = train[target].replace(1500, 2)
train[target] = train[target].replace(2000, 3)

dataset12 = xgb.DMatrix(train[predictors], label=train[target])
dataset3 = xgb.DMatrix(test[predictors])

watchlist = [(dataset12, 'train')]
model = xgb.train(params, dataset12, num_boost_round=1500, evals=watchlist)

# save model
model_name = "xgb_1500"
with open("model//" + model_name, 'wb') as f_handle:
    print 'Saving model...'
    cPickle.dump(model, f_handle, protocol=cPickle.HIGHEST_PROTOCOL)

# reload model
with open("model//" + model_name, 'rb') as f:
    model = cPickle.load(f)

# predict test set
predict_label = model.predict(dataset3)
result = predict_label
predict_label = MinMaxScaler().fit_transform(predict_label)

# Save results
test_result = pd.DataFrame(columns=["studentid", "subsidy"])
test_result.studentid = ids
test_result.subsidy = result
test_result.subsidy = test_result.subsidy.apply(lambda x: int(x))

test_result.subsidy = test_result.subsidy.replace(1, 1000)
test_result.subsidy = test_result.subsidy.replace(2, 1500)
test_result.subsidy = test_result.subsidy.replace(3, 2000)

print '1000--' + str(len(test_result[test_result.subsidy == 1000])) + ':741'
print '1500--' + str(len(test_result[test_result.subsidy == 1500])) + ':465'
print '2000--' + str(len(test_result[test_result.subsidy == 2000])) + ':354'

test_result.to_csv("D:/Competition/student_grant/xgb_2.csv", index=False)

# '''
