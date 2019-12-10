
# coding: utf-8

# In[ ]:


import duckdb
con = duckdb.connect('robust04db')
c = con.cursor()

BM = """ WITH qterms AS (SELECT termid, docid, count as df FROM terms                             
  WHERE termid IN (10575, 1285, 191)),                                          
  subscores AS (SELECT docs.docid, length, term_tf.termid,                         
  tf, df, (log((528155.000000-df+0.5)/(df+0.5))*((term_tf.tf*(1.2+1)/                          
  (term_tf.tf+1.2*(1-0.75+0.75*(length/188.33)))))) AS subscore                            
  FROM (SELECT termid, docid, df AS tf FROM qterms) AS term_tf                  
  JOIN (SELECT docid FROM qterms                                                
    GROUP BY docid )                           
    AS cdocs ON term_tf.docid = cdocs.docid                                     
  JOIN docs ON term_tf.docid=docs.docid                                         
  JOIN dict ON term_tf.termid=dict.termid)                                      
SELECT scores.docid, ROUND(score,6) FROM (SELECT docid, sum(subscore) AS score           
  FROM subscores GROUP BY docid) AS scores JOIN docs ON                         
  scores.docid=docs.docid ORDER BY ROUND(score,6) DESC, scores.docid ASC LIMIT 1000; """
x=c.execute(BM)
print(c.fetchall())
c.close()
con.close()



