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

* Use the Python script `indexer.py` to index documents. By default it will index all gif files in the `example_gifs` folder of this repository.
* Use the flask app to search: `export FLASK_APP=search.py && flask run`. To search for `bla`, go to `localhost:5000/search?name=bla`

