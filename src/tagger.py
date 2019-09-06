import os
from evaluateText import get_fileEntities
import json
from pathlib import Path

source_dir = "/home/ndc/repos/TCC/src/"
os.chdir(source_dir)
contracts_dir = "./contracts/"


#nlp = spacy.load('/home/ndc/repos/TCC/src/leNER-BR/model/leNERBR')



def list_texts(d=contracts_dir):
    r = []
    for root, dirs, files in os.walk(d):
        for name in files:
            f = os.path.join(root, name)
            if f.endswith("txt"):
                r.append(f)            
    return r


def store_entities(text_path):
    file_basename = Path(text_path).stem
    directory = os.path.dirname(text_path)    
    entities = get_fileEntities(text_path)
    f = open(directory+"/"+file_basename+".json","w")
    ents = json.dumps(entities)
    f.write(ents)
    f.close()
    return entities


#f2015 = "/home/ndc/repos/TCC/src/contracts/2015 - 204 arquivos"
#f2016 = "/home/ndc/repos/TCC/src/contracts/2016 - 1199 arquivos"
#f2017 = "/home/ndc/repos/TCC/src/contracts/2017 - 641 arquivos"
#f2018 = "/home/ndc/repos/TCC/src/contracts/2018 - 771 arquivos"
f2019 = "/home/ndc/repos/TCC/src/contracts/2019 - 417 arquivos"


texts = list_texts(f2019)

for t in range(0,len(texts)):       
    store_entities(texts[t])
    print(t,"/",len(texts))
    print(str((100*t)/len(texts))+"% done")
    print(texts[t])
    print("-----------------------\n")
    
    

    