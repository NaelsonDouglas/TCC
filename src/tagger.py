import os
from spacy import displacy
import spacy
import pt_core_news_sm


source_dir = "/home/ndc/repos/TCC/src/"
contracts_dir = "/home/ndc/repos/TCC/src/contracts/"


#nlp = spacy.load('/home/ndc/repos/TCC/src/leNER-BR/model/leNERBR')
nlp = spacy.load('pt')

os.chdir(source_dir)


def list_texts(dir=contracts_dir):
    r = []
    for root, dirs, files in os.walk(dir):
        for name in files:
            f = os.path.join(root, name)
            if f.endswith("txt"):
                r.append(f)            
    return r

def get_entities_unformated(text_path):
    directory = os.path.dirname(text_path)
    f = open(text_path,"r")
    raw_text = f.read()
    f.close()
    doc = nlp(raw_text)
    entities = [(i, i.label_, i.label) for i in doc.ents]
    return entities

def get_entities_dict(text_path):
    ents = get_entities_unformated(text_path)
    dic_ents = {}
    for e in ents: #e is an specific entity in the list of entities
        if "\n" not in e[0].text:
            if e[1] in dic_ents:  #Check if it's alreary listed an entity of the same class e = (lemma, class, a number)
                dic_ents[e[1]].add(e[0])
            else:
                dic_ents[e[1]] = {e[0]}
    return dic_ents