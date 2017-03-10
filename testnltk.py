from nltk.tag import pos_tag
from nltk.tokenize import word_tokenize
from pandas import Series, DataFrame
import collections
from nltk import wordnet
import re

#print (re.split(r'(\s*)', 'Here are some words'))
#print (re.split(r'[a-fA-F]','asdasdAsd',
#               re.I|re.M))

file = open("scam2.txt")
file = file.read()
words = file.split()
print file
print (re.findall(r'((.){1,}(\d){1,}(.){0,})$',file))

#re.I = caga para maisculo e minisculo
#re.M = Multiline
#\s = space
