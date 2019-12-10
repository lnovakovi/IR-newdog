import duckdb
con = duckdb.connect('robust04db')
c = con.cursor()

c.execute()
print(c.fetchall())

c.close()
con.close()

"WITH qterms AS (SELECT termid, docid, count FROM terms WHERE termid IN (10575, 1285, 191)),                                          subscores AS (SELECT docs.docid, len, term_tf.termid,                         
  tf, count, (log((528155-count+0.5)/(count+0.5))*((tf*(1.2+1)/                          
  (tf+1.2*(1-0.75+0.75*(len/188.33)))))) AS subscore                            
  FROM (SELECT termid, docid, count AS tf FROM qterms) AS term_tf                  
  JOIN (SELECT docid FROM qterms                                                
    GROUP BY docid HAVING COUNT(distinct termid) = 3)                           
    AS cdocs ON term_tf.docid = cdocs.docid                                     
  JOIN docs ON term_tf.docid=docs.docid                                         
  JOIN dict ON term_tf.termid=dict.termid)                                      
SELECT scores.docid, score FROM (SELECT docid, sum(subscore) AS score           
  FROM subscores GROUP BY docid) AS scores JOIN docs ON                         
  scores.docid=docs.docid ORDER BY score DESC;"
