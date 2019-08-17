import json
import os
os.chdir("/home/ndc/repos/TCC/src/leNER-BR")
f = open("train.json")
raw_data = json.loads(f.read())


#TRAIN_DATA = [
#    ("Who is Shaka Khan?", {"entities": [(7, 17, "PERSON")]}),
#    ("I like London and Berlin.", {"entities": [(7, 13, "LOC"), (18, 24, "LOC")]}),
#]


TRAIN_DATA = []

for r in raw_data:
    content = r['content']
    annotations = r['annotation']
    label = -1
    points_vec = []
    for a in annotations:
        points = a['points']            
        for p in points:
                point_cell = (p['start'],p['end'],a['label'][0])
                points_vec.append(point_cell)
    result = (content, {"entities":points_vec})
    TRAIN_DATA.append(result)