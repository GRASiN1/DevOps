import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="abcd",
    port=5432
)

cur = conn.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS users (id SERIAL PRIMARY KEY, name VARCHAR(255), age INTEGER)")

cur.execute("INSERT INTO users (name, age) VALUES (%s, %s)", ("John", 25))
cur.execute("INSERT INTO users (name, age) VALUES (%s, %s)", ("Jane", 30))

conn.commit()

cur.execute("SELECT * FROM users")
rows = cur.fetchall()
for row in rows:
    print(row)

conn.close()