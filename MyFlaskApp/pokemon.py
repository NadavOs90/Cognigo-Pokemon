from elasticsearch import Elasticsearch
import json
import subprocess
import sys
import requests


es = Elasticsearch([{'host': 'localhost', 'port': 9200}])


def new_pokemon(pokemon_json):
    es.index(index='exercise', doc_type='pokemon', id=pokemon_json['pokadex_id'], body=pokemon_json)


def search(string):
    query = {
        "query": {
            "multi_match": {
                "query": string,
                "type": "phrase_prefix",
                "fields": [],
            }
        }
    }
    res = es.search(index="exercise", body=query)['hits']['hits']
    if len(res) == 0:
        return []
    else:
        ans = []
        for hit in res:
            ans.append(hit['_source'])
        return ans
