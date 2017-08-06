GIF Indexer
===========

This small program aims to index gif names so they can be queried in Elasticsearch.

It splits the name on any non letter character and uses ngram for autocomplete research.

Requirements
------------

* Python 2.7 (pip requirement file is `requirements.txt`)
* Elasticsearch

How to use
----------

* Create the Elasticsearch index with the json in `esIndex.json`
* Use the Python script `indexer.py` to try indexing documents
* Use the Python script or ES REST API to query documents

