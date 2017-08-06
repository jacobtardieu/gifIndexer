from datetime import datetime
from elasticsearch import Elasticsearch
import json
es = Elasticsearch()

with open('esIndex.json') as json_index_file:
    json_index = json.load(json_index_file)

es.indices.create(index="gifs", body=json_index, ignore=400)

doc = {
    'name': 'lol_monkey',
    'timestamp': datetime.now(),
}
res = es.index(index="gifs", doc_type='gif', body=doc, id = doc["name"])
print(res['created'])

es.indices.refresh(index="gifs")

