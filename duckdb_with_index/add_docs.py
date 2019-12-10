import duckdb

con = duckdb.connect('robust04db_indexed')
c = con.cursor()

c.execute("COPY docs FROM 'docs_modified.csv' DELIMITER '|'")

c.close()
con.close()

