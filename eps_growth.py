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
cur.execute("SELECT year, eps FROM retail.bapcor;")

rows = cur.fetchall()

years = []
epss = []
eps_growth_rates = []

for r in rows:
    years.append(r[0])
    epss.append(r[1])

for i in 1, 2, 3, 4, 5:
    eps_growth_rates.append((epss[i]-epss[i-1])/epss[i-1])
        
for i, eps_growth_rate in enumerate(eps_growth_rates):
    
    print(str(year) + ": " + str(eps_growth_rate))

# for i, year in enumerate(years):
#     eps_growth_rate = eps_growth_rates[i]
#     print(str(year) + ": " + str(eps_growth_rate))
#not getting the right match between year and growth rate.

#eps = (eps[x]-eps[x-1])/eps[x-1]

# close cursor
cur.close()

# close the connection
con.close()