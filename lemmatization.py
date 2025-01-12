import nltk

# nltk.download('wordnet')

""" Lemmatization is the process of reducing a word to it's dictionary form (lemma), rather than, to it's stem."""


from nltk.stem import WordNetLemmatizer


lemmatizer = WordNetLemmatizer()

lemma = lemmatizer.lemmatize

words = ['eating', 'eats', 'eaten', 'writing', 'writes', 'programming', 'programs', 'history', 'finally', 'finalized']

# part of speech : 'n'->noun
# pos : 'v'->verb
# pos : 'a'->adjective
# pos : 'r'->adverb

for word in words:
    print(word+"---->"+lemma(word, pos='v'))
