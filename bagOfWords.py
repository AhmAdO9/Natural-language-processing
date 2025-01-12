import pandas as pd
import os


df = pd.read_csv('spam_collection/SMSSpamCollection', sep='\t', names=['label', 'message'])


documents = [message for message in df['message']]


from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize

# corpus = '. '.join(documents)

# word_tokens = word_tokenize(corpus)

# print(corpus)

import re

word_tokens = [word_tokenize(re.sub("[^a-zA-Z.' ]", '', sentence)) for sentence in documents]


# print(word_tokens)

from nltk.stem import WordNetLemmatizer


lemmatizer = WordNetLemmatizer()

lemma = lemmatizer.lemmatize

from nltk.corpus import stopwords

stopwords = stopwords.words('english')

lemmatized_docs = []
for words in word_tokens:
    w = []
    for word in words:
        if word not in stopwords:
            w.append(lemma(word.lower( ), pos='v'))
    joined_words = ' '.join(w)
    lemmatized_docs.append(joined_words)

# print(df['message'][20])
# print(lemmatized_docs[:10])



from sklearn.feature_extraction.text import CountVectorizer

## for binary BOW, enable binary:
countVector = CountVectorizer(max_features=2500, binary=False)
# max_features limit vocabulary size, keeps only the words with relatively higher frequency.

X = countVector.fit_transform(lemmatized_docs)

# print(X.toarray()[:2])

# print(countVector.vocabulary_)
