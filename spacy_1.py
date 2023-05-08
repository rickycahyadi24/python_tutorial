import spacy

nlp = spacy.load("en_core_web_sm")
doc = nlp("Apple is looking at buying U.K. startup for $1 billion")
nonstopcounter = 0
stopcounter = 0

for token in doc:
    print (token.text, token.pos_, token.dep_, token.lemma_, token.is_stop)
    if token.is_stop == False:
        nonstopcounter += 1
    else:
        stopcounter +=1
    

length = len(doc)

print(f'Number of token: {length}')
print(f'Number of stopwords: {stopcounter}, Number of non stopword: {nonstopcounter}')