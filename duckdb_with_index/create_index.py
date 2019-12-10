import duckdb
con = duckdb.connect('robust04db_indexed')
c = con.cursor()

c.execute("CREATE INDEX dict_index ON dict (termid)")
c.execute("CREATE INDEX docs_index ON docs (docid)")
c.execute("CREATE INDEX terms_index ON terms (termid)")

c.close()
con.close()


