
import duckdb

con = duckdb.connect('robust04db_pk') 
c = con.cursor()

c.execute("SELECT COUNT(*) FROM dict")
print("Number of rows in dict: ")
print(c.fetchall())

c.execute("SELECT COUNT(*) FROM docs")
print("Number of rows in docs: ")
print(c.fetchall())

c.execute("SELECT COUNT(*) FROM terms")
print("Number of rows in terms: ")
print(c.fetchall())

c.close()
con.close()
