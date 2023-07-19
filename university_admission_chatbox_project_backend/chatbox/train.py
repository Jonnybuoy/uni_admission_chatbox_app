import json
import numpy as np
import torch
import torch.nn as nn
import torch.utils.data import Dataset, DataLoader

from chatbox.nltk_utils import tokenize, stem, bag_of_words

with open('chatbox/intents.json', 'r') as f:
    intents = json.load(f)

all_words = []
tags = []
patterns_and_tags = []

for intent in intents['intents']:
    tag = intent['tag']
    tags.append(tag)
    for pattern in intent['patterns']:
        w = tokenize(pattern)
        all_words.extend(w)
        patterns_and_tags.append((w, tag))

ignore_words = ['?', '!', ',', '.']
all_words = [stem(w) for w in all_words if w not in ignore_words]
all_words = sorted(set(all_words))
tags = sorted(set(tags))

x_train = [] # will hold all the bag of words
y_train = [] # associated number for each tag

for (pattern_sentence, tag) in patterns_and_tags:
    bag = bag_of_words(pattern_sentence, all_words)
    x_train.append(bag)
    
    label = tags.index(tag)
    y_train.append(label)

x_train = np.array(x_train)
y_train = np.array(y_train)


class ChatDataset(DataSet):
    def __init__(self):
        self.n_samples = len(x_train)
        self.x_data = x_train
        self.y_data = y_train
    
    # to access dataset with an index
    def __getitem__(self, index):
        return self.x_data[index], self.y_data[index]
    
    def __len__(self):
        return self.n_samples

# Hyperparams
batch_size = 8

dataset = ChatDataset()
train_loader = DataLoader(dataset=dataset, batch_size=batch_size, shuffle=True, num_workers=2)
