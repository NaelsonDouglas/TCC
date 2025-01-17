'''
Code entirely written by the authors of leNER-Br paper
'''

# This file was developed as part of the project reported in the paper below.
# We kindly request that users cite our paper in any publication that is 
# generated as a result of the use of our source code or our dataset.
# 
# Pedro H. Luz de Araujo, Teófilo E. de Campos, Renato R. R. de Oliveira, Matheus Stauffer, Samuel Couto and Paulo Bermejo.
# LeNER-Br: a Dataset for Named Entity Recognition in Brazilian Legal Text.
# International Conference on the Computational Processing of Portuguese (PROPOR),
# September 24-26, Canela, Brazil, 2018. 
#
#    @InProceedings{luz_etal_propor2018,
#          author = {Pedro H. {Luz de Araujo} and Te\'{o}filo E. {de Campos} and
#          Renato R. R. {de Oliveira} and Matheus Stauffer and
#          Samuel Couto and Paulo Bermejo},
#          title = {LeNER-Br: a Dataset for Named Entity Recognition in Brazilian Legal Text},
#          booktitle = {International Conference on the Computational Processing of Portuguese
#          ({PROPOR})},
#          year = {2018},
#          month = {September 24-26},
#          address = {Canela, RS, Brazil},
#          note = {Available from \url{https://cic.unb.br/~teodecampos/LeNER-Br/}}
#      }      


#os.chdir("/home/ndc/repos/TCC/src/LeNER-BR/LeNER-Br/model")


from model.ner_model import NERModel
from model.config import Config
from nltk import word_tokenize
from nltk import data
from nltk.tokenize.punkt import PunktSentenceTokenizer
import sys

bcolors = {
    "PESSOA": '\033[94m',
    "TEMPO": '\033[92m',
    "LOCAL": '\033[93m',
    "ORGANIZACAO": '\033[91m',
    "JURISPRUDENCIA": '\033[35m',
    "LEGISLACAO": '\033[36m',
    "ENDC": '\033[0m',
    "O": ""
}



# create instance of config
config = Config()

# build model
model = NERModel(config)
model.build()
model.restore_session(config.dir_model)

#filename = sys.argv[1]

def get_fileEntities(filename):
    tokenizer = PunktSentenceTokenizer()

    with open(filename, 'r') as file:
        text = file.read()

    tokenizer.train(text)
    sentences = tokenizer.tokenize(text)


    loading_word = False
    acumulator = ""
    pred_acumulator = ""


    tags = {
        "PESSOA": {},
        "TEMPO": {},
        "LOCAL": {},
        "ORGANIZACAO": {},
        "JURISPRUDENCIA": {},
        "LEGISLACAO": {},    
    }

    for sentence in sentences:
        words = word_tokenize(sentence, language='portuguese')
        words = [x.lower() for x in words]
        
        preds = model.predict(words)    
        for index, word in enumerate(words):

            if preds[index][0:2] in ['B-', 'I-', 'E-', 'S-']:
                if preds[index][0:2] == 'B-':
                    if loading_word:
                        #print(acumulator)
                        #print(pred_acumulator)

                        if acumulator in tags[pred_acumulator]:
                            tags[pred_acumulator][acumulator] = tags[pred_acumulator][acumulator]+1
                        else:
                            tags[pred_acumulator][acumulator] = 1

                        #print("--------")
                        acumulator = word
                    else:
                        loading_word = True
                if preds[index][0:2] == 'I-':
                    acumulator = acumulator+" "+word


                preds[index] = preds[index][2:]
                pred_acumulator = preds[index]
                #print(preds[index]+"\n")




            #print(bcolors[preds[index]] + 
                #word + bcolors["ENDC"], end=' ')
        #print('\n')

    #print(tags)
    return tags