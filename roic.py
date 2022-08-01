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
cur.execute("SELECT year, nopat, debt, equity FROM retail.bapcor;")

rows = cur.fetchall()

for r in rows:
    year = r[0]
    nopat = r[1]
    debt = r[2]
    equity = r[3]
    roic = nopat/(equity-debt)
    print(str(year) + ": " + str(roic))

# close cursor
cur.close()

# close the connection
con.close()