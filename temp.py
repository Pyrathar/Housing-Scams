import numpy as np
from difflib import SequenceMatcher
import re, math
from collections import Counter

result=[]
match=0


WORD = re.compile(r'\w+')

def get_cosine(vec1, vec2):
     intersection = set(vec1.keys()) & set(vec2.keys())
     numerator = sum([vec1[x] * vec2[x] for x in intersection])

     sum1 = sum([vec1[x]**2 for x in vec1.keys()])
     sum2 = sum([vec2[x]**2 for x in vec2.keys()])
     denominator = math.sqrt(sum1) * math.sqrt(sum2)

     if not denominator:
        return 0.0
     else:
        return float(numerator) / denominator

def text_to_vector(text):
     words = WORD.findall(text)
     return Counter(words)

def comparebyarray(array):

    with open("Lies.txt") as f:
        content = f.readlines()
        content = [x.strip() and x.split() for x in content]
        #Lies array
        for j in content:
          str1 = ' '.join(array)
          str2 = ' '.join(j)

          vector1 = text_to_vector(str1)
          vector2 = text_to_vector(str2)

          cosine = get_cosine(vector1, vector2)

          matcher = SequenceMatcher(None, str1,str2).ratio()


          if matcher>=0.80:
              print str1+"|matcher"
              print matcher
          if cosine >= 0.80:
              print str1+"|cosine"
              print cosine


def expressionhunt(array):
    match=0

    with open("Lies.txt") as f:
        content = f.readlines()
        content = [x.strip() and x.split() for x in content]
        #Lies array
        for j in content:#para cada alerta
          np.array_equal(array, j)
           #para cada palavra alerta
          for index2,y in enumerate(j):
            for index,x in enumerate(array):  #para palavra do scam

                 print y,index2



file = open("scam3.txt")
file = file.read()
words = file.split()
limit = len(words)
samplearray=[]
match=0


for index, value in enumerate(words):
     if index<=(limit-6):
        for i in range(6):

          word = words[index+i]
          samplearray.append(word)


          if i==5:
            comparebyarray(samplearray)
            samplearray=[]

