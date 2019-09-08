import ocr
import tagger
import filter_results


geral = "/home/ndc/repos/TCC/src/contracts/"
f2015 = "/home/ndc/repos/TCC/src/contracts/2015 - 204 arquivos"
f2016 = "/home/ndc/repos/TCC/src/contracts/2016 - 1199 arquivos"
f2017 = "/home/ndc/repos/TCC/src/contracts/2017 - 641 arquivos"
f2018 = "/home/ndc/repos/TCC/src/contracts/2018 - 771 arquivos"
f2019 = "/home/ndc/repos/TCC/src/contracts/2019 - 417 arquivos"   

entity_classes = ['ORGANIZACAO','PESSOA','LOCAL','JURISPRUDENCIA','TEMPO','LEGISLACAO']

year = [f2015,f2016,f2017,f2018,f2019]
year_label =[[f2015,"2015"],[f2016,"2016"],[f2017,"2017"],[f2018,"2018"],[f2019,"2019"],[geral,"todos"]]

#texts = tagger.list_texts(f2017)

def ocr_all(year):
        for f in year:
                ocr.wipe_pdfs_dir(f)

def tag_all(year):
        for t in range(0,len(texts)):       
                tagger.store_entities(texts[t])
                print(t,"/",len(texts))
                print(str((100*t)/len(texts))+"% done")
                print(texts[t])
                print("-----------------------\n")

def plot_all(year_label):
        for c in entity_classes:
                for y in year_label:
                        filter_results.plot_entityFreq(y[0],entity_class=c,min_freq=20,max_freq=200,custom_name = y[1])
                        filter_results.plot_entityFreq(y[0],entity_class=c,min_freq=1,max_freq=10,custom_name = y[1])
                        filter_results.plot_entityFreq(y[0],entity_class=c,min_freq=1,max_freq=2,custom_name = y[1])
                        filter_results.plot_entityFreq(y[0],entity_class=c,min_freq=5,max_freq=10,custom_name = y[1])
                        filter_results.plot_entityFreq(y[0],entity_class=c,min_freq=200,max_freq=350,custom_name = y[1])
                        filter_results.plot_entityFreq(y[0],entity_class=c,min_freq=150,max_freq=800,custom_name = y[1])
                        filter_results.plot_entityFreq(y[0],entity_class=c,min_freq=10,max_freq=300,custom_name = y[1])
                        filter_results.plot_entityFreq(y[0],entity_class=c,min_freq=150,max_freq=350,custom_name = y[1])