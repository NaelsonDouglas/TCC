# TCC
TODO



# spaCy Highlights

* Source: https://www.dataquest.io/blog/tutorial-text-classification-in-python-using-spacy/


## Tokenization by word
```Python
from spacy.lang.en import English

nlp = English()
text = """When learning data science, you shouldn't get discouraged!
Challenges and setbacks aren't failures, they're just part of the journey. You've got this!"""
my_doc = nlp(text)

# Create list of word tokens
token_list = []
for token in my_doc:
    token_list.append(token.text)
print(token_list)
```
## Tokenization by sentence
```Python
#The difference from word tokenization to it is that we use a sentencizer pipe

nlp = English()
# Create the pipeline 'sentencizer' component
sbd = nlp.create_pipe('sentencizer')

# Add the component to the pipeline
nlp.add_pipe(sbd)

text = """When learning data science, you shouldn't get discouraged!
Challenges and setbacks aren't failures, they're just part of the journey. You've got this!"""


doc = nlp(text)

sents_list = []
for sent in doc.sents:
    sents_list.append(sent.text)
print(sents_list)
```



## Removing STOP WORDS
```Python
from spacy.lang.en.stop_words import STOP_WORDS

#Lists the english stop words
import spacy
spacy_stopwords = spacy.lang.en.stop_words.STOP_WORDS

#Implementation of stop words:
filtered_sent=[]

#  "nlp" Object is used to create documents with linguistic annotations.
doc = nlp(text)

# filtering stop words
for word in doc:
    if word.is_stop==False:
        filtered_sent.append(word)
print("Filtered Sentence:",filtered_sent)
```
## Lemmatization
```Python
# Implementing lemmatization
lem = nlp("run runs running runner")
# finding lemma for each word
for word in lem:
    print(word.text,word.lemma_)
```

## Word Vector representation

```Python

import en_core_web_sm
nlp = en_core_web_sm.load()
mango = nlp(u'mango')
print(mango.vector.shape)
print(mango.vector)
```