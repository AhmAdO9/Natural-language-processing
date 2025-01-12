import nltk

# nltk.download("punkt_tab")


corpus = """Hello Welcome    , to Krish Naiks's NLP Tutorials.



Please do watch the entire. course. to become expert in NLP


."""


from nltk.tokenize import sent_tokenize

# Corpus into sentences
sent_tokens = sent_tokenize(corpus)

# print(sent_tokens)
# for i in tokens:
    # print(i)


# Paragraph into words
from nltk.tokenize import word_tokenize

word_tokens = word_tokenize(corpus)

# print(word_tokens)
# for i in word_tokens:
#     print(i)

from nltk.tokenize import wordpunct_tokenize

wordpunct_tokens = wordpunct_tokenize(corpus)

# print(wordpunct_tokens)


from nltk.tokenize import TreebankWordTokenizer

tokenizer = TreebankWordTokenizer()

treebank_word_tokens = tokenizer.tokenize(corpus)

print(treebank_word_tokens)



