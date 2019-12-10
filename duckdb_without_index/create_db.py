import duckdb

con = duckdb.connect('robust04db') #stores db info in filename
c = con.cursor()

c.execute("CREATE TABLE dict (termid INTEGER,term VARCHAR(100), df INTEGER)")
c.execute("CREATE TABLE terms (termid INTEGER,docid INTEGER, count INTEGER)")
c.execute("CREATE TABLE docs (name VARCHAR(50), docid INTEGER, length INTEGER)")

c.close()
con.close()

