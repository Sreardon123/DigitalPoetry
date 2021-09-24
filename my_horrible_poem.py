# -*- coding: utf-8 -*-

from textblob import TextBlob
import nltk
nltk.download('punkt')

blob = TextBlob(text)

poem = ''
with open('/content/The Tay Bridge Disaster.txt') as f:
  text = f.read()

  words = text.split (" ")

  import random

  random.shuffle(words)

for w in range(len(words)):
  poem += " " + words.pop(0) 

print(poem)
