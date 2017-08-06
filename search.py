from datetime import datetime
from elasticsearch import Elasticsearch
import json
from flask import Flask, request
app = Flask(__name__)

es = Elasticsearch()

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/search")
def search():
    queried_name = request.args.get('name', "")
    result = {}
    res = es.search(index="gifs", body={"query": {"match": {"name": queried_name}}})
    result['took'] = res['took']
    result['hits'] = res['hits']['total']
    result['results'] = []
    for hit in res['hits']['hits']:
        result['results'].append({'name': hit["_source"]["name"], 'score': hit["_score"]})
    return json.dumps(result)

