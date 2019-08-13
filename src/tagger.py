import os
from spacy import displacy
import pt_core_news_sm


source_dir = "/home/ndc/repos/TCC/src/"
contracts_dir = "/home/ndc/repos/TCC/src/contracts/"


nlp = spacy.load('pt')

os.chdir(source_dir)


def list_files(dir=contracts_dir):
    r = []
    for root, dirs, files in os.walk(dir):
        for name in files:
            f = os.path.join(root, name)
            if f.endswith("txt"):
                r.append(f)            
    return r

def get_entities(text_path):
    f = open(text_path,"r")
    raw_text = f.read()
    f.close()
    doc = nlp(raw_text)
    entities = [(i, i.label_, i.label) for i in doc.ents]
    return entities

x=get_entities(texts[1])

for i in x:
    print(i)




texts = list_files()