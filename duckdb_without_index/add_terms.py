import duckdb

con = duckdb.connect('robust04db') 
c = con.cursor()

for i in range(1,996):
    query = "COPY terms FROM '../createDB/terms" + str(i) + ".csv' DELIMITER '|'"
    c.execute(query)
    print("Completed " + str(i) + " of 995")

c.close()
con.close()

