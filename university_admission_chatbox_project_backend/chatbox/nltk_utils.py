import nltk
import numpy as np

from nltk.stem.porter import PorterStemmer

nltk.download('punkt')

stemmer = PorterStemmer()

def tokenize(sentence):
    return nltk.word_tokenize(sentence)

def stem(word):
    return stemmer.stem(word.lower())

def bag_of_words(tokenized_sentence, all_words):
    """
    Basically this function takes in an incoming tokenized sentence,
    and checks for the occurrence of the words in the sentence in the
    all_words collection. If there is an occurrence, it is represented by
    a 1 in the bag. Example:
    
    sentence = ["hello", "how", "are", "you"]
    all_words = ["hi", "hello", "I", "you", "bye", "thank", "cool"]
    bag = [    0,     1,     0,     1,    0,     0,      0]
    """
    tokenized_sentence = [stem(w) for w in tokenized_sentence]
    bag = np.zeros(len(all_words), dtype=np.float32)
    for idx, w in enumerate(all_words):
        if w in tokenized_sentence:
            bag[idx] = 1.0
    
    return bag
    