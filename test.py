import mysql.connector as mysql

conn = mysql.connect(
    user='worldskills',
    password='worldskills',
    port=3306,
    host='127.0.0.1',
    database='worldskills'
)
cur = conn.cursor()

cur.execute('SELECT CURDATE()')
cur_date, = cur.fetchone()

print(cur_date)

conn.close()
