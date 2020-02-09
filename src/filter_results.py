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

#get_jsons(f2016)

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

def plot_entityFreq(directory=tags_parent_dir,entity_class = "PESSOA",min_freq=1,max_freq = 9999999999999999,exclude=[],to_file=True,custom_name=''):
    if not (max_freq < min_freq):
        j=get_jsons(directory)
        j=extract_categ(j,entity_class)
        j=merge_jsons(j)
        j = filter_dict(j,min_freq,max_freq,exclude)

        labels = list(j.values())
        
        plt.barh(range(len(j)), labels, align='center',color='cornflowerblue')
        plt.yticks(range(len(j)), list(j.keys()))
        

        min_label = "="
        max_label = "="

        if min_freq >0:
            min_label = str(min_freq)
        if max_freq < 9999999999999999:
            max_label = str(max_freq)

        plt.xlabel('Frequência '+custom_name+' ['+min_label+'-'+max_label+']',fontsize=15)        
        if  to_file:   
            name = os.path.basename(directory)
            if len(custom_name) > 0:
                name = custom_name
            

            #We cant add the excluded entities to the filename since there may be characters on the entity whose can't be used as filenaes. Like 's/a', we can't put it in a filename
            exclude_list = ''
            if len(exclude) > 0:
                exclude_list = '[FILTERED]'
            print("Exclude: "+exclude_list)
            fname = str('plots/'+entity_class+'/'+name.upper()+'-['+min_label+'-'+max_label+']'+exclude_list)
            print("Generated: "+fname)
            plt.tight_layout(pad=0)            
            #plt.tick_params(labelsize=4)
            plt.savefig(fname,dpi=500)   
            amount_labels = len(labels)
            yticks_size = 15
            if amount_labels > 10:
                yticks_size = round(amount_labels/7)
            plt.tick_params(axis='y', which='major', labelsize=8)
        else:   
           plt.show()
        plt.cla()
        return True       
    else:
        print("max_freq must be higher or equal to min_freq")
        return False




geral = "/home/ndc/repos/TCC/src/contracts/"
f2015 = "/home/ndc/repos/TCC/src/contracts/2015 - 204 arquivos"
f2016 = "/home/ndc/repos/TCC/src/contracts/2016 - 1199 arquivos"
f2017 = "/home/ndc/repos/TCC/src/contracts/2017 - 641 arquivos"
f2018 = "/home/ndc/repos/TCC/src/contracts/2018 - 771 arquivos"
f2019 = "/home/ndc/repos/TCC/src/contracts/2019 - 417 arquivos"   
year =[[f2015,"2015"],[f2016,"2016"],[f2017,"2017"],[f2018,"2018"],[f2019,"2019"],[geral,"todos"]]

year =[[f2015,"2015"],[f2016,"2016"],[f2017,"2017"],[f2018,"2018"],[f2019,"2019"]]


entity_classes = ['ORGANIZACAO','PESSOA','LOCAL','JURISPRUDENCIA','TEMPO','LEGISLACAO']
for c in entity_classes:
    for y in year:        
        #plot_entityFreq(y[0],entity_class=c,min_freq=150,max_freq=800,custom_name = y[1],exclude=["s/a"])
        #plot_entityFreq(y[0],entity_class=c,min_freq=20,max_freq=200,custom_name = y[1])
        #plot_entityFreq(y[0],entity_class=c,min_freq=1,max_freq=10,custom_name = y[1])
        plot_entityFreq(y[0],entity_class=c,min_freq=1,max_freq=300,custom_name = y[1])
        #plot_entityFreq(y[0],entity_class=c,min_freq=1,max_freq=2,custom_name = y[1])
        #plot_entityFreq(y[0],entity_class=c,min_freq=5,max_freq=10,custom_name = y[1])
        #plot_entityFreq(y[0],entity_class=c,min_freq=200,max_freq=350,custom_name = y[1])
        #plot_entityFreq(y[0],entity_class=c,min_freq=150,max_freq=800,custom_name = y[1])
        #plot_entityFreq(y[0],entity_class=c,min_freq=10,max_freq=300,custom_name = y[1])
        #plot_entityFreq(y[0],entity_class=c,min_freq=150,max_freq=350,custom_name = y[1])

