import psycopg2
import csv
import sys

# setting_data = '../../data/db_setting.csv'
setting_data = 'test_settiong.csv'
dic = {}

with open(setting_data, 'r') as f:
    reader = csv.reader(f, delimiter=',')
    for row in reader:
        dic[row[0]] = row[1]
    f.close

try:
    con = psycopg2.connect(host=dic['host'], dbname=dic['dbname'], port=dic['port'], user=dic['user'], password=dic['password'])
    print('Connection succeeded!')
    cur = con.cursor()

    con.close()
    cur.close()

except:
    print('Connection failed...')
    sys.exit()
