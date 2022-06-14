import mysql.connector as mysql

conn = mysql.connect(
    user='worldskills',
    password='worldskills',
    port=3306,
    host='127.0.0.1',
    database='worldskills'
)
cur = conn.cursor()

cur.execute("DELETE FROM newspapers WHERE id > 1")
cur.execute("DELETE FROM users WHERE id > 1")
conn.commit()

conn.close()
