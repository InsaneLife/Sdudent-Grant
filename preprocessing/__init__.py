# coding = utf8
import MySQLdb
import pandas as pd

# conn = MySQLdb.connect(host="localhost", user="root", passwd="root", db="student_grant", charset="utf8")
data = {
        'year':[2000,2001,2002,2001,2002],
        'pop':[1.5,1.7,3.6,2.4,2.9]}
df = pd.DataFrame(data)

print df
print df.rank(axis=0, method='dense', ascending=False)
