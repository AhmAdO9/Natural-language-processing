# import nltk

# nltk.download('stopwords')



corpus = """ I am indeed very happy to be with you on this memorable occasion. I am delighted to speak to you today. This is a day to reflect upon and remind ourselves of what we as a nation have accomplished, where we stand, and where we can go in the future.

Let me start by telling you about my vision for the future of our country. I have seen India's progress in the past, and I have a deep sense of optimism and excitement for the future.

As I look forward, I see India as a country that will be a leader in innovation, technology, and global peace. We are a nation of thinkers, scholars, and creators. We have within us the power to shape the future and lead the world. Every Indian has the potential to contribute to the nation's growth in areas ranging from science and technology to education, culture, and society.

The vision I have for India in the next 20 years is that we will emerge as a knowledge society, a society where innovation is encouraged and knowledge is accessible to all. In this future, the youth of India will become the driving force of change. They will be the leaders, entrepreneurs, and creators of tomorrow. I am confident that India will be one of the most powerful and peaceful nations in the world by the time the next generation steps forward.

I have always believed that it is our collective responsibility to contribute to the country's progress. We need to work together, to not only address our challenges but to turn them into opportunities. Together, we can create a society that is not only prosperous but also just, where there is no place for discrimination, hatred, or injustice.

Each and every one of us, no matter our role, must be committed to this vision. We must dedicate ourselves to progress, innovation, and excellence. With hard work, courage, and the spirit of unity, there is no limit to what we can achieve.

I am very hopeful for the future of India. I see a vibrant nation that will continue to rise to new challenges and achieve new heights. Our greatest asset is our people, and we must empower and encourage each individual to realize their full potential.

Let us all work towards the goal of making India a knowledge-driven, prosperous, and peaceful nation.

Thank you. """

# from nltk.corpus import stopwords
# stopwords = stopwords.words('english')




# from nltk import sent_tokenize

# sentences = sent_tokenize(corpus)

# words = [nltk.word_tokenize(sentence) for sentence in sentences]




# from nltk.stem import PorterStemmer
# stemmer = PorterStemmer()

# for i in range(len(sentences)):
#     words = nltk.word_tokenize(sentences[i])
#     stems = [stemmer.stem(word) for word in words if word not in stopwords]
#     sentences[i] = ' '.join(stems)

# print(sentences)



# from nltk.stem import SnowballStemmer
# snowball_stemmer = SnowballStemmer('english')

# for i in range(len(sentences)):
#     words = nltk.word_tokenize(sentences[i])
#     snowball_stems = [snowball_stemmer.stem(word) for word in words if word not in stopwords]
#     sentences[i] = ' '.join(snowball_stems)

# print(sentences)





# from nltk.stem import WordNetLemmatizer
# lemmatizer = WordNetLemmatizer().lemmatize

# for i in range(len(sentences)):
#     sentences[i] = sentences[i].lower()
#     words = nltk.word_tokenize(sentences[i])
#     lemma = [lemmatizer(word, pos='n') for word in words if word not in stopwords]
#     sentences[i] = ' '.join(lemma)

# print(sentences)





#### Parts of speech:

# import nltk
# from nltk.tokenize import word_tokenize

# nltk.download('averaged_perceptron_tagger_eng')

# for i in range(len(sentences)):
#     sentences[i] = sentences[i].lower()
#     words = word_tokenize(sentences[i])
#     words = [word for word in words if word not in stopwords]
#     pos_tag = nltk.pos_tag(words)
#     print(pos_tag)


# sentence = 'Taj mahal is a beautiful monument'


# sentence = sentence.split(' ')

# print(nltk.pos_tag(sentence))





#### Named Entity Recognition:


import nltk
# nltk.download('maxent_ne_chunker_tab')
# nltk.download('words')

words = nltk.word_tokenize('mukest guastav company india usa uk bristol guildford holiday sunday monday')


tagged_words = nltk.pos_tag(words)

# print(tagged_words)

# named_entities = nltk.ne_chunk(tagged_words).draw()

# print(named_entities)