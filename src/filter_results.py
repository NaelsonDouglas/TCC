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
    for root, folders, files in os.walk(contracts_dir):
        if not first_loop:
            print(root)
            inner_files = os.listdir(root)
            entities_json = "-1"
            for i in inner_files:
                if i.endswith(".json"):
                    entities_json = root+"/"+i            
            if entities_json.endswith(".json"):
                with open(entities_json) as f:
                    entities_json = json.load(f)            
                jsons.append(entities_json)
        else:
            first_loop = False
    return jsons

get_jsons(f2016)

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

#Not actually being used.Marked for deletion
def dict_to_array(d,_min_freq= 0,_max_freq = 9999999999999999,_exclude=[]):
    array = []
    for k in d.keys():
        for freq in range(0,d[k]):
            if  k not in _exclude:                               
                if ((d[k] >= _min_freq) and (d[k] <= _max_freq)):                                        
                    array.append(k)
                else:
                    print(str(_min_freq)+" "+str(d[k])+" "+str(_max_freq))                    
    return array

def filter_dict(d,min_freq,max_freq,exclude=[]):
    new_dict = {}
    for k in d.keys():
        value = d[k]
        if value<=max_freq:
            if value>=min_freq:
                if k not in exclude:
                    new_dict[k]=value
    return new_dict


def plot_entityFreq(directory=tags_parent_dir,entity_class = "PESSOA",min_freq=0,max_freq = 9999999999999999,exclude=[]):
    if not (max_freq < min_freq):
        j=get_jsons(directory)
        j=extract_categ(j,entity_class)
        j=merge_jsons(j)
        j = filter_dict(j,min_freq,max_freq,exclude)

        labels = list(j.values())
        plt.bar(range(len(j)), labels, align='center')
        plt.xticks(range(len(j)), list(j.keys()))
        plt.ylabel('Frequência',fontsize=20)
        plt.xticks(rotation=90)
        plt.gcf().subplots_adjust(bottom=0.3)
        plt.show()
        return True       
    else:
        print("max_freq must be higher or equal to min_freq")
        return False

plot_entityFreq(f2016,entity_class = "ORGANIZACAO",min_freq=10,max_freq=150)


