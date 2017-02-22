# coding=utf8
import MySQLdb
import pandas as pd
import time

s_pro = pd.read_csv('D:/Competition/student_grant//20143858.csv')

s_pro.index = s_pro['studentid']
s_pro.drop('studentid', axis=1, inplace=True)

s_rank = s_pro.rank(axis=0, method='dense', ascending=False)
print s_rank.head(5)

tt = str(time.strftime('%d%H%M%S', time.localtime(time.time())))
# tt = 's'
out = open("D:/Competition/student_grant/rank/" + tt + ".csv", 'w')
out.write("studentid,subsidy\n")
i = [0, 0, 0, 0]
for index, row in s_rank.iterrows():
    money = 0
    if row['s3'] < 300:
        money = 2000
        i[3] += 1
    elif row['s2'] < 490:
        money = 1500
        i[2] += 1
    elif row['s3'] < 1525:
        money = 1000
        i[1] += 1
    else:
        i[0] += 1
    out.write(str(index) + "," + str(money) + "\n")
out.close()
print i
