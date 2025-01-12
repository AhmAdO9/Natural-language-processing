""" Stemming is the process of reducing a word to it's stem. Stemming is important in natural language understanding (NLU) and natural language processing (NLP). E.g; eat, eating, eaten --> eat, i.e,  all three words refer to the same thing which is; eat. Similarly, [going, gone,goes --> go]"""


words = ['eating', 'eats', 'eaten', 'writing', 'writes', 'programming', 'programs', 'history', 'finally', 'finalized']

# PorterStemmer: 
from nltk.stem import PorterStemmer


porter_stemmer = PorterStemmer()

# for word in words:
#     stem = porter_stemmer.stem(word)
#     print(word+"---->"+stem)
    

stem = porter_stemmer.stem('congratulations')

# print(stem)


# RegexpStemmer class: with the help of regular expressions, we apply stemming.


from nltk.stem import RegexpStemmer
import re

reg_stemmer = RegexpStemmer('ing$|s$|able$', min=4)

# print(reg_stemmer.stem('congratulations'))


# print(reg_stemmer.stem('ingeating'))


# Snowball Stemmer

from nltk.stem import SnowballStemmer

snowball_stemmer = SnowballStemmer('english')

# for word in words:
#     print(word+"----->"+snowball_stemmer.stem(word))




