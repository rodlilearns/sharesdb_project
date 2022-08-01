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

years = []
nopats =[]
debts = []
equities = []
roics = []

for r in rows:
    years.append(r[0])
    nopats.append(r[1])
    debts.append(r[2])
    equities.append(r[3])
    roics.append(r[1]/(r[3]-r[2]))

print(roics)

for i, year in enumerate(years):
    roic = roics[i]
    print(str(year) + ": " + str(roic))

# class roic:
#     def roic_for_the_year(self):
#         print(self.year + ": " + self.roic)

# for r in rows:
#     year = r[0]
#     nopat = r[1]
#     debt = r[2]
#     equity = r[3]
#     object1 = roic()
#     object1.year = year
#     object1.roic = nopat/(equity-debt)
#     object1.roic_for_the_year()

# close cursor
cur.close()

# close the connection
con.close()