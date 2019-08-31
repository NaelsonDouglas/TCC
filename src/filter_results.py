import json
import os
from pprint import pprint
from collections import Counter
import matplotlib.pyplot as plt

tags_parent_dir="/home/ndc/repos/TCC/src/contracts/2015 - 204 arquivos"


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



def merge_jsons(jsons):
    merged = {}
    for j in jsons:
        merged = dict(Counter(j)+Counter(merged))
    return merged

def dict_to_array(d,min_freq=5):
    array = []
    for k in d.keys():
        for freq in range(0,d[k]):
            if d[k] >= min_freq:
                array.append(k)
    return array

def plot_entityFreq(directory=tags_parent_dir,entity_class = "PESSOA",min_freq=5):
    j=get_jsons(directory)
    j=extract_categ(j,entity_class)
    j=merge_jsons(j)
    j=dict_to_array(j,min_freq)
    j = sorted(j)
    plt.hist(j, histtype='bar', ec='black')
    plt.ylabel('Frequência',fontsize=20)
    plt.xticks(rotation=90)
    plt.gcf().subplots_adjust(bottom=0.3)
    plt.show()
