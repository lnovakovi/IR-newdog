import duckdb

con = duckdb.connect('robust04db_indexed') #stores db info in filename
c = con.cursor()

c.execute("CREATE TABLE dict (termid INTEGER NOT NULL,term VARCHAR, df INTEGER)")
c.execute("CREATE TABLE terms (termid INTEGER,docid INTEGER, count INTEGER)")
c.execute("CREATE TABLE docs (name VARCHAR, docid INTEGER NOT NULL, length INTEGER)")

c.close()
con.close()

