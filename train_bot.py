#Text Data Preprocessing Lib
import nltk
nltk.download('punkt')
from nltk.stem import PorterStemmer
import json
import pickle
import numpy as np
stemmer = PorterStemmer()

words = []
classes = []
wordtagslist = []

train_data_file = open("intents.json").read()
intents = json.loads(train_data_file)
ignorewords = ["?",",",".","'s","'m"]

word = "He is my friend"
w=stemmer.stem(word.lower())
print(w)

# function for appending stem words

def getStemWords(words,ignorewords):
    stemwords = []
    for word in words:
        if word not in ignorewords:
            w = stemmer.stem(word.lower())
            stemwords.append(w)
        print(stemwords)

wordlist = ["Running","Walking","Standing","Drawing"]
getStemWords(wordlist,ignorewords)

for intent in intents['intents']:
    
        # Add all words of patterns to list
        for pattern in intent['patterns']:            
            pattern_word = nltk.word_tokenize(pattern)            
            words.extend(pattern_word)                      
            wordtagslist.append((pattern_word, intent['tag']))
        # Add all tags to the classes list
        if intent['tag'] not in classes:
            classes.append(intent['tag'])
            stem_words = getStemWords(words, ignorewords)

print(stem_words)
print(wordtagslist[0]) 
print(classes)   

#Create word corpus for chatbot
def create_bot_corpus(stem_words, classes):

    stemwords = sorted(list(stem_words))
    classes = sorted(list(set(classes)))

    pickle.dump(stemwords, open('words.pkl','wb'))
    pickle.dump(classes, open('classes.pkl','wb'))

    return stem_words, classes

stemwords, classes = create_bot_corpus(stemwords,classes)  

print(stemwords)
print(classes)

    
        # Add all words of patterns to list
        
        # Add all tags to the classes list
         

#Create word corpus for chatbot

