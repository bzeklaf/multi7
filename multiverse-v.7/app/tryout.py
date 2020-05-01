import re

from difflib import SequenceMatcher
import difflib
import nltk
from nltk.tokenize import sent_tokenize
# nltk.download('punkt')
def similar(a,b):
    return SequenceMatcher(None, a, b).ratio()
def anticipation_func(body_of_text):
    small_dictionary = {'Found2':['Any obligation on a party not to do something includes an obligation not to allow that thing to be done.']}
    # body_of_text = 'Here is the large body of text. Each sentence in this body, should be compared to each of the values in the dictionary. If the comparision ration is above certain treshold, corresponding key should be printed.'
    sentencing = sent_tokenize(body_of_text)
    list_of_keys = []
    for key,value in small_dictionary.items():
        for item in value:
            for token in sentencing:
                resulting = similar(item,token)
                if resulting >= 1:
                    list_of_keys.append(key)
    if(len(list_of_keys)>0):
        list_of_keys = set(list_of_keys)
    return list_of_keys

#CW
def cw_processing(text):
   wording = text
   a = {'Found1':['Consultant']}
   for key,value in a.items():
       for item in value:
           if item in wording:
               yield (key)
               break

def reg_pro(text):
    patterns = ['this', 'tits']
    rs=['This','Tits']
    wording = text
    little_box = []
    for pattern in patterns:
        #print('Looking for "%s" in "%s" ->' % (pattern, text), end=' ')
        if re.search(pattern, wording):
            #print('found a match!')
            little_box.append((rs[patterns.index(pattern)]))
    return(little_box)

    

    
   #b = {'gigli':['bubu'], 'buba':['warrants'], 'hoojo':['yoooha']}
   #for key,value in b.items():
   #    for item in value:
   #        if item not in wording:
   #            yield (key)
   #            break           
#APP
def appoint_processing(text):
   wording = text
   a = {'adios muchachos':['John', 'consultant', 'consultant']}
   for key,value in a.items():
       for item in value:
           if item in wording:
               yield (key)
               break
   b = {'gigli':['bubu'], 'buba':['warrants'], 'hoojo':['yoooha']}
   for key,value in b.items():
       for item in value:
           if item not in wording:
               yield (key)
               break 

def regular(text):
    wording = text
    pattern = re.compile(r'[1-5]')#values beetween 1-5 
    matches = pattern.finditer(wording)#extra functionality of a match object
    for match in matches:
        yield(match)
    