from elasticsearch import Elasticsearch
import json
import subprocess
import sys
import requests


es = Elasticsearch([{'host': 'localhost', 'port': 9200}])


def validate_pokemon_json(json_string):
    types = ["ELECTRIC", "GROUND", "FIRE", "WATER", "WIND", "PSYCHIC", "GRASS", 'NORMAL', 'ROCK', 'POISON', 'BUG', 'ICE', 'GHOST', 'DRAGON']
    try:
        json_obj = json.loads(json_string)
    except ValueError as e:
        print e
        return False
    if not isinstance(json_obj.get('name'), unicode):
        return False
    if not isinstance(json_obj.get('level'), int) or json_obj['level'] < 0:
        return False
    if not isinstance(json_obj.get('skills'), list):
        return False
    if not isinstance(json_obj.get('type'), unicode) or json_obj['type'] not in types:
        return False
    if not isinstance(json_obj.get('nickname'), unicode):
        return False
    if not isinstance(json_obj.get('pokadex_id'), int) or json_obj['pokadex_id'] < 0:
        return False
    return True


def new_pokemon(pokemon_json):
    if validate_pokemon_json(pokemon_json):
        pokemon_json_object = json.loads(pokemon_json)
        es.index(index='exercise', doc_type='pokemon', id=pokemon_json_object['pokadex_id'], body=pokemon_json_object)
        return True
    return False


def search(string):
    query = {
        "query": {
            "multi_match": {
                "query": string,
                "type": "phrase_prefix",
                "fields": []
            }
        }
    }
    query2 = {
        "query": {
            "match" : {
                "message" : {
                    "query" : string,
                    "operator" : "and"
                }
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
