from datetime import datetime
from elasticsearch import Elasticsearch
import json
import glob
import os

es = Elasticsearch()

with open('esIndex.json') as json_index_file:
    json_index = json.load(json_index_file)

es.indices.create(index="gifs", body=json_index, ignore=400)

gifs_names = map(os.path.basename, glob.glob("example_gifs/*.gif"))

for name in gifs_names:
    es.index(index="gifs", doc_type='gif', body={'name': name}, id = name)

#res = es.index(index="gifs", doc_type='gif', body=doc, id = doc["name"])
#print(res['created'])

es.indices.refresh(index="gifs")

