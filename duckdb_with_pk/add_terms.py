import duckdb

con = duckdb.connect('robust04db_pk') 
c = con.cursor()

for i in range(1,996):
    query = "COPY terms FROM 'terms" + str(i) + ".csv' DELIMITER '|'"
    c.execute(query)
    print("Completed " + str(i) + " of 995")

c.close()
con.close()

