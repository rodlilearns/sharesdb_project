import psycopg2

# connect to the sharesdb
con = psycopg2.connect(
            host = "192.168.20.26",
            database = "sharesdb",
            user = "postgres",
            password = "student")

# cursor
cur = con.cursor()

# execute query
cur.execute("SELECT year, sales FROM retail.bapcor;")

rows = cur.fetchall()

for r in rows:
    print(f"year {r[0]} sales {r[1]}")

# close cursor
cur.close()

# close the connection
con.close()