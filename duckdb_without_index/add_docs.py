import duckdb

con = duckdb.connect('robust04db')
c = con.cursor()

c.execute("COPY docs FROM '../createDB/docs_modified.csv' DELIMITER '|'")

c.close()
con.close()

