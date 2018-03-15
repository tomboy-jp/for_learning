import psycopg2
import csv
import sys

'''
test_settingの二列目の値をご使用のDBに合わせてご使用ください。
PostgreSQLでの使用を想定しているため、他のDBだとport番号も異なるかと思います。
'''

# setting_data = '../../data/db_setting.csv'
setting_data = 'test_settiong.csv'
dic = {}
result = []

with open(setting_data, 'r') as f:
    reader = csv.reader(f, delimiter=',')
    for row in reader:
        dic[row[0]] = row[1]
    f.close

try:
    con = psycopg2.connect(host=dic['host'], dbname=dic['dbname'], port=dic['port'], user=dic['user'], password=dic['password'])
    print('Connection succeeded!\n')

except:
    print('Connection failed...')
    sys.exit()

sql = "select complete_date, title from nobels where complete_date between '2018/01/01' and '2018/02/28'"
cur = con.cursor()
cur.execute(sql)

data = cur.fetchall

con.close()
cur.close()

for row in data:
    result.append(row)
