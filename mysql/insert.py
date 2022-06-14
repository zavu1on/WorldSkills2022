import mysql.connector as mysql

conn = mysql.connect(
    user='worldskills',
    password='worldskills',
    port=3306,
    host='127.0.0.1',
    database='worldskills'
)
cur = conn.cursor()

cur.execute("INSERT INTO users (username, password) VALUES ('John', 'J0hn');")
conn.commit()
cur.execute("""INSERT INTO newspapers (title, user_id) VALUES ('Hello World!', 1);""")
conn.commit()

cur.execute('SELECT username, title FROM users JOIN newspapers ON users.id = newspapers.user_id;')

resp = cur.fetchall()
print(resp)

conn.close()
