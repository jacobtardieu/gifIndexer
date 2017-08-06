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
* Run `search.py` to start a web server handling the search requests.
* Run `serve_files.py` to start a web server serving the HTML page and all the gifs. In production, it should be replaced by Nginx or Apache. You can then go to localhost:5000 and search for gifs.

API
===

`/search`
--------

Allows to search for a gif by name.

Query parameter:
* `name`: The name or a part of the name. The default is an empty string.
The result will be a json object containing all the gif names which matched the query.

Example `/search?name=scared`
