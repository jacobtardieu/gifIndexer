from datetime import datetime
from elasticsearch import Elasticsearch
import json

es = Elasticsearch()

query_string = "sta"

result = {}
res = es.search(index="gifs", body={"query": {"match": {"name": query_string}}})
result['took'] = res['took']
result['hits'] = res['hits']['total']
result['results'] = []
for hit in res['hits']['hits']:
    result['results'].append({'name': hit["_source"]["name"], 'score': hit["_score"]})

json_result = json.dumps(result)
print(json_result)
