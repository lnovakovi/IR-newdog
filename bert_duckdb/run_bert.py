
'''
def model_rank(self, query: bytes, choices: List[Choice]) -> List[int]:
        """Rank the query and choices and return the argsorted indices"""
        return self.model.rank(query, choices)

#Create BertModel object
#use the "rank" function

from threading import Thread
from typing import List
import tensorflow as tf
from queue import Queue
import numpy as np
import nboost.model.bert_model as bm
from nboost.model.bert_model import modeling, tokenization
from nboost.model.base import BaseModel
from nboost.types import Choice




c1 = Choice(1,b'Try')
c2 = Choice(2,b'Try3Tryyy')
c3 = Choice(3,b'Try3Try')
c4 = Choice(4,b'Try2')
choices = [c1,c2,c3,c4]
m = bm.BertModel()
print(m.rank(b'Try',choices))
'''
import json 

keys = []
values = []
new_dict
with open('all.json') as json_file:
	contents = json_file.read()
	json_data = json.loads(contents)
	new_dict = {item['id']:item for item in json_data}
	print(new_dict['LA031289-0155.000003']['contents'])
''''''''''''''''