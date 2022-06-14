import mysql.connector as mysql

conn = mysql.connect(
    user='worldskills',
    password='worldskills',
    port=3306,
    host='127.0.0.1',
    database='worldskills'
)
cur = conn.cursor()

cur.execute('SELECT username, title FROM users JOIN newspapers ON users.id = newspapers.user_id;')

resp = cur.fetchall()
print(resp)

conn.close()
