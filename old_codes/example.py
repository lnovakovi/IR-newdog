import duckdb
import numpy as np
con = duckdb.connect('robust04db_new')
c = con.cursor()
print("here1")
c.execute("DROP INDEX IF EXISTS dict_index")
print("here2")
print(c.fetchall())

c.close()
con.close()

'''
c.execute("SELECT avg(length) FROM docs");
avgdl = c.fetchall()[0][0]
k1 = 1.2
b = 0.75
query_term = 'car'


c.execute("SELECT COUNT(*) FROM docs");
N = c.fetchall()[0][0]

c.execute("SELECT df FROM dict WHERE term='car'");
df = c.fetchall()[0][0]

idf = np.log2((N-df+0.5)/(df+0.5))


c.execute("SELECT ("+str(idf)+"*(table2.count*"+ str(k1+1) +")/(table2.count+("+str(k1)+"*("+str(1-b) +" +("+str(b)+"*(table2.length/"+ str(avgdl) +")))))) AS score, table2.docid FROM (SELECT table1.count, table1.docid, (SELECT length FROM docs WHERE table1.docid = docs.docid) AS length FROM (SELECT docid, count FROM terms WHERE terms.termid = (SELECT termid FROM dict WHERE term = '"+ query_term +"')) AS table1) AS table2 ORDER BY score DESC LIMIT 5")
print(c.fetchall())





table1 = docid-count (how many times the query term occur in document with docid)
(SELECT docid, count FROM terms WHERE terms.termid = (SELECT termid FROM dict WHERE term = 'car')) AS table1

table2 = docid-count-doclength
(SELECT table1.count, table1.docid, (SELECT length FROM docs WHERE table1.docid = docs.docid) AS length FROM table1) AS table2

select the one with highest score
SELECT ((table2.count*2.2)/(table2.count+(1.2*(0.25 +(0.75*(table2.length/330)))))) AS score, table2.docid FROM table2
ORDER BY score DESC LIMIT 5




#c.execute("SELECT count, (SELECT length FROM docs WHERE K.docid = docs.docid) AS length, docid FROM (SELECT docid, count FROM terms WHERE terms.termid = (SELECT termid FROM dict WHERE term = 'car')) AS K")
#c.execute("SELECT ((P.count*2.2)/(P.count+(1.2*(0.25 +(0.75*(P.length/330)))))) AS score, P.docid FROM (SELECT count, (SELECT length FROM docs WHERE K.docid = docs.docid) AS length, docid FROM (SELECT docid, count FROM terms WHERE terms.termid = (SELECT termid FROM dict WHERE term = 'car')) AS K) AS P ORDER BY score DESC LIMIT 1")
#c.execute("SELECT ((table2.count*2.2)/(table2.count+(1.2*(0.25 +(0.75*(table2.length/330)))))) AS score, table2.docid FROM (SELECT table1.count, table1.docid, (SELECT length FROM docs WHERE table1.docid = docs.docid) AS length FROM (SELECT docid, count FROM terms WHERE terms.termid = (SELECT termid FROM dict WHERE term = 'car')) AS table1) AS table2 ORDER BY score DESC LIMIT 5")
#c.execute("SELECT ((table2.count*"+ str(k1+1) +")/(table2.count+("+str(k1)+"*("+str(1-b) +" +("+str(b)+"*(table2.length/"+ str(avgdl) +")))))) AS score, table2.docid FROM (SELECT table1.count, table1.docid, (SELECT length FROM docs WHERE table1.docid = docs.docid) AS length FROM (SELECT docid, count FROM terms WHERE terms.termid = (SELECT termid FROM dict WHERE term = '"+ query_term +"')) AS table1) AS table2 ORDER BY score DESC LIMIT 5")
'''
