import duckdb

con = duckdb.connect('robust04db') 
c = con.cursor()

c.execute("COPY dict FROM '../createDB/dict.csv'  DELIMITER '|'")

c.close()
con.close()

