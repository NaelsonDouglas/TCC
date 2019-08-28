import json
import os
from pprint import pprint
from collections import Counter


#Gets a directory and returns all the entities jsons on the directory subfolders
def get_jsons(contracts_dir):
    jsons = []
    first_loop = True
    for d in os.walk(contracts_dir):
        if not first_loop:            
            entities_json = d[0]+"/entities.json"            
            with open(entities_json) as f:
                entities_json = json.load(f)            
            jsons.append(entities_json)
        else:
            first_loop = False
    return jsons

def extract_categ(jsons,category):
    data = []
    for j in jsons:
        data.append(j[category])
    return data

j=get_jsons("/home/ndc/repos/TCC/src/contracts/2015 - 204 arquivos")

def merge_jsons(jsons):
    merged = {}
    for j in jsons:
        dict(Counter(j)+Counter(j))
    return merged

