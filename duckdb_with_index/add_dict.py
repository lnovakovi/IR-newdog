import duckdb

con = duckdb.connect('robust04db_indexed') 
c = con.cursor()

c.execute("COPY dict FROM 'dict.csv'  DELIMITER '|'")

c.close()
con.close()

