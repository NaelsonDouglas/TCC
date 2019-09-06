import json
import os
from pprint import pprint
import collections
import operator
from collections import Counter
import matplotlib.pyplot as plt

tags_parent_dir="/home/ndc/repos/TCC/src/contracts/2015 - 204 arquivos"


#Gets a directory and returns all the entities jsons on the directory subfolders
def get_jsons(contracts_dir):
    jsons = []
    first_loop = True
    for root, folders, files in os.walk(contracts_dir):
        if not first_loop:
            #print(root)
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
                    #I'm breaking the key in 2 lines for big entities in order for it to fit on the barplot xticks. Otherwise it will overlap the screen
                    #It won't interfer on the 'exclude' arg tho
                    break_size = 20
                    if len(k) > break_size:                        
                        temp=[k[i:i+break_size] for i in range(0, len(k), break_size)]
                        k=''
                        for  i in temp:
                            k=k+i+'\n'
                        #k = k[0:40]+"\n"+k[40:len(k)]                    
                    new_dict[k]=value
    new_dict=sorted(new_dict.items(), key=operator.itemgetter(1))
    return collections.OrderedDict(new_dict)




entity_classes = ['ORGANIZACAO','PESSOA','LOCAL','JURISPRUDENCIA','TEMPO','LEGISLACAO']
f2015 = "/home/ndc/repos/TCC/src/contracts/2015 - 204 arquivos"
f2016 = "/home/ndc/repos/TCC/src/contracts/2016 - 1199 arquivos"
f2017 = "/home/ndc/repos/TCC/src/contracts/2017 - 641 arquivos"
f2018 = "/home/ndc/repos/TCC/src/contracts/2018 - 771 arquivos"
f2019 = "/home/ndc/repos/TCC/src/contracts/2019 - 417 arquivos"   

def plot_entityFreq(directory=tags_parent_dir,entity_class = "PESSOA",min_freq=0,max_freq = 9999999999999999,exclude=[],to_file=False):
    if not (max_freq < min_freq):
        j=get_jsons(directory)
        j=extract_categ(j,entity_class)
        j=merge_jsons(j)
        j = filter_dict(j,min_freq,max_freq,exclude)

        labels = list(j.values())
        
        plt.barh(range(len(j)), labels, align='center',color='cornflowerblue')
        plt.yticks(range(len(j)), list(j.keys()))
        plt.xlabel('Frequência',fontsize=20)        
        if  to_file:            
            fname = str('plots/'+entity_class+'/'+os.path.basename(directory)+'['+str(min_freq)+'-'+str(max_freq)+']'+str(exclude))            
            plt.tight_layout(pad=0.1)            
            plt.tick_params(labelsize=4)
            plt.savefig(fname,dpi=160)                         
        else:   
           plt.show()
        return True       
    else:
        print("max_freq must be higher or equal to min_freq")
        return False

plot_entityFreq(f2018,entity_class = "ORGANIZACAO",min_freq=11,max_freq=150,exclude=["anvisa"],to_file=True)