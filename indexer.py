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

for complete_name in gifs_names:
    name = complete_name[:-4] # Remove the `.gif` part in the name
    res = es.index(index="gifs", doc_type='gif', body={'timestamp': datetime.now(), 'name': name}, id = name)
    print("Indexed %s and created: %s" % (complete_name, res['created']))

es.indices.refresh(index="gifs")

