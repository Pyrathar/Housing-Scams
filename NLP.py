import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.tokenize import PunktSentenceTokenizer
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet

#tokenizing organize by word or sentence
#lexicon
#corpora - body of text
#lexicon - dictionary
#stemming = ride riding = ride
#speech taging = divide text by verb noun etc..

example_test =" Hello Carolina and Paulo,Good day and thanks for the response. the apartment is still free the address is Denmark Lyngsby Hestegangen 6 and you can start to rent as soon as possible but sorry viewing the flat will not be possible for now because i have left the country already and i have the flat keys here with me, I just relocated here in England due to my new job and that is the main reason I am renting outthe flat but I can only send you some of the flat pictures to see and have an idea  of the flat. I will be waiting to hear from you soon. Where are you now and what date do you intend to start renting and move into the flat?, payment has to be made in Western Union"


#Chunking = removing a piece we want
#Chinking = something we dont want
#lemmatizing= sinonyms



stop_words = word_tokenize(example_test)

custom_sent = PunktSentenceTokenizer(example_test)
tokenized = custom_sent.tokenize(example_test)

lemmatizer = WordNetLemmatizer()

def process_content():
    try:
        for i in tokenized:
            words= nltk.word_tokenize(i)
            tagged = nltk.pos_tag(words)

            namedEnt = nltk.ne_chunk(tagged)

            print namedEnt
    except Exception as e:
        print(str(e))

def process_content2():
    try:
        for i in tokenized:
            words= nltk.word_tokenize(i)
            tagged = nltk.pos_tag(words)

            chunkGram = r"""Anyname:{<RB.?>*<VB.?>*<NNP><NN>?} """
            chunkParser = nltk.RegexpParser(chunkGram)
            chunked = chunkParser.parse(tagged)
            chunked.draw()

    except Exception as e:
        print(str(e))


process_content2()
