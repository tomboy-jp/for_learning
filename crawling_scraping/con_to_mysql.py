import MySQLdb

con = MySQLdb.connect(db='scraping', user='scraper', passwd='password', charset='utf8mb4')
cur = con.cursor()

cur.execute('DROP TABLE IF EXISTS cities')
cur.execute("CREATE TABLE cities (rank integer, city text, population integer)")
cur.execute('INSERT INTO cities VALUES (%s, %s, %s)', (1, '上海', 24150000))
cur.execute("INSERT INTO cities VALUES (%(rank)s, %(city)s, %(population)s)", {'rank': 2, 'city': 'カラチ', 'population': 23500000})

cur.executemany("INSERT INTO cities VALUES (%(rank)s, %(city)s, %(population)s)",[
    {'rank': 3, 'city': '北京', 'population': 21516000},
    {'rank': 4, 'city': '天津', 'population': 14722100},
    {'rank': 5, 'city': 'イスタンブル', 'population': 14160467}
    ])
con.commit()

cur.execute("SELECT * FROM cities")

for row in cur.fetchall():
    print(row)

con.close()
