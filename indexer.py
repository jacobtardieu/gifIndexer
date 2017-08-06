from datetime import datetime
from elasticsearch import Elasticsearch
es = Elasticsearch()

doc = {
    'text': 'sta_bloum',
    'timestamp': datetime.now(),
}
res = es.index(index="test-index", doc_type='gif', id=1, body=doc)
print(res['created'])

res = es.get(index="test-index", doc_type='gif', id=1)
print(res['_source'])

es.indices.refresh(index="test-index")

res = es.search(index="test-index", body={"query": {"match_all": {}}})
print("Got %d Hits:" % res['hits']['total'])
for hit in res['hits']['hits']:
    print("%(timestamp)s %(author)s: %(text)s" % hit["_source"])
