import re
import subprocess
import duckdb
import numpy as np
import time


from threading import Thread
from typing import List
import tensorflow as tf
from queue import Queue
import nboost.model.bert_model as bm
from nboost.model.bert_model import modeling, tokenization
from nboost.model.base import BaseModel
from nboost.types import Choice

import json



class TopicReader:
	
	def __init__(self, topics_file_name):
		self.filename = topics_file_name
		self.file = open(self.filename)
		self.topics = []
		print("Read topics...",flush=True)
		self._read_topics_file()
		print("Preprocess topics...",flush=True)
		self._preprocess_titles()
	
	def return_topics(self):
		return self.topics

	def _read_topics_file(self):
		while True:
			line = self.file.readline()
			if not line:
				break

			if not line.strip():
				continue
			
			while line and not line.startswith('<top>'):
				line = self.file.readline()
			if not line:
				break
			
			while not line.startswith('<num>'):
				line = self.file.readline()
			topic_no = int(re.search('Number: (\d+)', line.strip()).group(1))
			
			# print("Parsing topic {}".format(topic_no),flush=True)

			while not line.startswith('<title>'):
				line = self.file.readline()

			# Robust04 specific:
			topic_title = line.strip()[8:]

			line = self.file.readline().strip()
			while not line.startswith('</title>') and not line.startswith('<desc>'):
				topic_title += line
				line = self.file.readline().strip()
			
			while not line.startswith('<desc>'):
				line = self.file.readline().strip()
			
			topic_desc = ""
			line = self.file.readline().strip()			
			while not line.startswith('</desc>') and not line.startswith('<narr>'):
				topic_desc += line
				line = self.file.readline().strip()

			while not line.startswith('<narr>'):
				line = self.file.readline().strip()
			
			topic_nar = ""
			line = self.file.readline().strip()
			
			while not line.startswith('</narr>') and not line.startswith('</top>'):
				topic_nar += line
				line = self.file.readline().strip()
				
			while not line.startswith('</top>'):
				line = self.file.readline().strip()
				
			topic = {   
						'number' : topic_no,
						'title' : topic_title,
						'description' : topic_desc,
						'narrative' :  topic_nar 
					}
			self.topics.append(topic)
				
	
	def _preprocess_titles(self):
		for i, topic in enumerate(self.topics):
			title = topic['title']
			process = subprocess.Popen("""../target/appassembler/bin/nl.ru.preprocess.ProcessQuery {}""".format(title).split(), stdout=subprocess.PIPE)
			stdout = process.communicate()[0].decode("utf-8").strip()
			self.topics[i]['title'] = stdout


	def get_topics(self):
		return self.topics

if __name__ == "__main__" :
	tr = TopicReader("topics.robust04.301-450.601-700.txt")
	topics = tr.return_topics()

	keys = []
	values = []
	contents = {}
	with open('all.json') as json_file:
		contents = json_file.read()
		json_data = json.loads(contents)
		contents = {item['id']:item for item in json_data}
		
	con = duckdb.connect('robust04db_indexed')
	c = con.cursor()
	times = []
	for item in topics:
		start_time = time.time() 
		query_no = item['number']
		query = item["title"]
		query_words= ""
		for word in query.split():
				query_words = query_words + "'" + word.lower() + "',"
		query_words = query_words[:-1]
		c.execute("SELECT termid FROM dict WHERE term IN (" + query_words + ")")
		id_list = c.fetchall()
		query_ids= ""
		for ids in id_list:
				query_ids = query_ids + str(ids[0]) + ","
		query_ids = query_ids[:-1]
		BM = """ WITH qterms AS (SELECT termid, docid, count as df FROM terms							 
		WHERE termid IN ("""+ query_ids +""")),										  
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
		scores.docid=docs.docid ORDER BY ROUND(score,6) DESC, scores.docid ASC LIMIT 100; """
		c.execute(BM)
		end_time = time.time()
		times.append(end_time-start_time)
		docids =str(list(c.fetchnumpy()['docid']))[1:-1]
		c.execute("SELECT name FROM docs WHERE docid IN (" + docids + ")")
		candidate_docs = c.fetchnumpy()['name']
		choices = []
		for i in range(len(candidate_docs)):
			print(contents[candidate_docs[i] + '.000000']['contents'])
			

		break
	c.close()
	con.close()

