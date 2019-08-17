import os
from evaluateText import get_fileEntities
import json

#source_dir = "/home/ndc/repos/TCC/src/"
contracts_dir = "./contracts/"


#nlp = spacy.load('/home/ndc/repos/TCC/src/leNER-BR/model/leNERBR')
#os.chdir(source_dir)


def list_texts(dir=contracts_dir):
    r = []
    for root, dirs, files in os.walk(dir):
        for name in files:
            f = os.path.join(root, name)
            if f.endswith("txt"):
                r.append(f)            
    return r

def get_entities(text_path):
    directory = os.path.dirname(text_path)    
    entities = get_fileEntities(text_path)
    f = open(directory+"/entities.json","w")
    ents = json.dumps(entities)
    f.write(ents)
    f.close()
    return entities


texts = list_texts()

for t in range(0,len(texts)):
    get_entities(texts[t])
    print(t,"/",len(texts))
    print(texts[t])
    print("\n")
    

