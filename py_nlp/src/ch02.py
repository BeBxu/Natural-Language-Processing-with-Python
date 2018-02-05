#!/usr/bin/python
# -*- coding: utf-8 -*-

# Accessing Text Corpora
import nltk
# file identifiers in this corpus
nltk.corpus.gutenberg.fileids()
emma = nltk.corpus.gutenberg.words('austen-emma.txt')
len(emma)
#  perform concordancing
emma = nltk.Text(nltk.corpus.gutenberg.words('austen-emma.txt'))
emma.concordance("surprize")
# But since it is cumbersome to type such long names all the time
from nltk.corpus import gutenberg
gutenberg.fileids()
emma = gutenberg.words('austen-emma.txt')
# display other information about each text
from __future__ import division
for fileid in gutenberg.fileids():
#     the contents of the file without any linguistic processing
    num_chars = len(gutenberg.raw(fileid))
    num_words = len(gutenberg.words(fileid))
# divides the text up into its sentences, where each sentence is a list of words
    num_sents = len(gutenberg.sents(fileid))
    num_vocab = len(set(w.lower() for w in gutenberg.words(fileid)))
# average word length, average sentence length,
# and the number of times each vocabulary item appears in the text on average (our lexical diversity score)
    print(round(num_chars/num_words), round(num_words/num_sents), round(num_words/num_vocab), fileid)

# Observe that average word length appears to be a general property of English,
#  since it has a recurrent value of 4. 
# (In fact, the average word length is really 3 not 4, 
# since the num_chars variable counts space characters.) 
# By contrast average sentence length and lexical diversity appear to be characteristics of particular authors.
# Richer linguistic content is available from some corpora, 
# such as part-of-speech tags, dialogue tags, syntactic trees, and so forth

macbeth_sentences = gutenberg.sents('shakespeare-macbeth.txt')
macbeth_sentences
macbeth_sentences[1116]
longest_len = max(len(s) for s in macbeth_sentences)
[s for s in macbeth_sentences if len(s) == longest_len]

# NLTK's small collection of web text
from nltk.corpus import webtext
for fileid in webtext.fileids():
    print(fileid, webtext.raw(fileid)[:65], '...')
    
from nltk.corpus import nps_chat
chatroom = nps_chat.posts('10-19-20s_706posts.xml')  # @UndefinedVariable
chatroom[123]

# Brown Corpus: the sources have been categorized by genre, such as news, editorial, and so on.
# a complete list, see http://icame.uib.no/brown/bcm-los.html
from nltk.corpus import brown
brown.categories()
# access the corpus as a list of words
brown.words(categories='news')
brown.words(fileids=['cg22'])
# OR a list of sentences(where each sentence is itself just a list of words)
brown.sents(categories=['news', 'editorial', 'reviews'])
# The Brown Corpus is a convenient resource for studying systematic differences between genres, a kind of linguistic inquiry known as stylistics. 
# compare genres in their usage of modal verbs
# 1. produce the counts for a particular genre
import nltk
from nltk.corpus import brown
news_text = brown.words(categories='news')
fdist = nltk.FreqDist(w.lower() for w in news_text)
modals = ['can', 'could', 'may', 'might', 'must', 'will']
from __future__ import print_function
for m in modals:
    print(m + ':', fdist[m], end=' ')

# Your Turn: Choose a different section of the Brown Corpus, and adapt the previous example
#  to count a selection of wh words, such as what, when, where, who, and why.
reviews_text = brown.words(categories='reviews')
reviews_fdist = nltk.FreqDist(w.lower() for w in reviews_text)
whs = ['what', 'when', 'where', 'who', 'why']
for wh in whs:
    print(wh + ':', reviews_fdist[wh], end=' ')
    
# Next, we need to obtain counts for each genre of interest
# conditional frequency distributions
cfd = nltk.ConditionalFreqDist(
           (genre, word)
           for genre in brown.categories()
           for word in brown.words(categories=genre))
genres = ['news', 'religion', 'hobbies', 'science_fiction', 'romance', 'humor']
modals = ['can', 'could', 'may', 'might', 'must', 'will']
cfd.tabulate(conditions=genres, samples=modals)
# Observe that the most frequent modal in the news genre is will, while the most frequent modal in the romance genre is could. 

# Reuters Corpus
# The Reuters Corpus contains 10,788 news documents totaling 1.3 million words. 
# The documents have been classified into 90 topics, and grouped into two sets, 
# called "training" and "test";
from nltk.corpus import reuters
reuters.fileids()
# Unlike the Brown Corpus, categories in the Reuters corpus overlap with each other
# , simply because a news story often covers multiple topics.
reuters.categories()

# ask for the topics covered by one or more documents
reuters.categories('training/9865')
reuters.categories(['training/9865', 'training/9880'])

# or for the documents included in one or more categories
reuters.fileids('barley')
reuters.fileids(['barley', 'corn'])

# Similarly, we can specify the words or sentences we want in terms of files or categories.
# The first handful of words in each of these texts are the titles, which by convention are stored as upper case.
reuters.words('training/9865')[:14]
reuters.words(['training/9865', 'training/9880'])
reuters.words(categories='barley')
reuters.words(categories=['barley', 'corn'])

# Inaugural Address Corpus:a collection of 55 texts, one for each presidential address.

# time dimension
from nltk.corpus import inaugural
inaugural.fileids()
# that the year of each text appears in its filename. To get the year out of the filename, we extracted the first four characters
[fileid[:4] for fileid in inaugural.fileids()]

# look at how the words America and citizen are used over time
cfd = nltk.ConditionalFreqDist(
           (target, fileid[:4])
           for fileid in inaugural.fileids()
           for w in inaugural.words(fileid)
           for target in ['america', 'citizen']
#            checks if they start with either of the "targets" america or citizen using startswith()
           if w.lower().startswith(target))
cfd.plot()

# Annotated Text Corpora
# Many text corpora contain linguistic annotations, representing POS tags, named entities, syntactic structures, semantic roles, and so forth. 
# see  http://nltk.org/data   http://nltk.org/howto

# Corpora in Other Languages
from nltk.corpus import udhr
nltk.corpus.cess_esp.words()
nltk.corpus.floresta.words()
nltk.corpus.indian.words('hindi.pos')
nltk.corpus.udhr.fileids()
nltk.corpus.udhr.words('Javanese-Latin1')[11:]
# examine the differences in word lengths for a selection of languages included in the udhr corpus
languages = ['Chickasaw', 'English', 'German_Deutsch',
    'Greenlandic_Inuktikut', 'Hungarian_Magyar', 'Ibibio_Efik']
cfd = nltk.ConditionalFreqDist(
          (lang, len(word))
          for lang in languages
          for word in udhr.words(lang + '-Latin1'))  # @UndefinedVariable
cfd.plot(cumulative=True)

# Your Turn: Pick a language of interest in udhr.fileids(), and define a variable raw_text = udhr.raw(Language-Latin1). Now plot a frequency distribution of the letters of the text using nltk.FreqDist(raw_text).plot().

#Text Corpus Structure
help(nltk.corpus.reader) #http://nltk.org/howto

raw = gutenberg.raw("burgess-busterbrown.txt")
raw[1:20]
words = gutenberg.words("burgess-busterbrown.txt")
words[1:20]
sents = gutenberg.sents("burgess-busterbrown.txt")
sents[1:20]

#Loading your own Corpus
from nltk.corpus import PlaintextCorpusReader
corpus_root = '/usr/share/dict'
# '.*' can be a list of fileids, like ['a.txt', 'test/b.txt'], or a pattern that matches all fileids, like '[abc]/.*\.txt'
wordlists = PlaintextCorpusReader(corpus_root, '.*')
wordlists.fileids()
wordlists.words('connectives')

from nltk.corpus import BracketParseCorpusReader
corpus_root = r"C:\corpora\penntreebank\parsed\mrg\wsj"
file_pattern = r".*/wsj_.*\.mrg"
ptb = BracketParseCorpusReader(corpus_root, file_pattern)
ptb.fileids()
len(ptb.sents())
ptb.sents(fileids='20/wsj_2013.mrg')[19]

# Conditional Frequency Distributions: 
# is a collection of frequency distributions, each one for a different "condition".
# The condition will often be the category of the text. 

# A frequency distribution counts observable events,
# such as the appearance of words in a text.
# A conditional frequency distribution needs to pair each event with a condition.
# So instead of processing a sequence of words,
# we have to process a sequence of pairs:
text = ['The', 'Fulton', 'County', 'Grand', 'Jury', 'said', """..."""]
pairs = [('news', 'The'), ('news', 'Fulton'), ('news', 'County'), '''...''']
# Each pair has the form (condition, event). 
# If we were processing the entire Brown Corpus by genre there would be 15 conditions 
# (one per genre), and 1,161,192 events (one per word).

# Counting Words by Genre
# Whereas FreqDist() takes a simple list as input, ConditionalFreqDist() takes a list of pairs
from nltk.corpus import brown
cfd = nltk.ConditionalFreqDist(
        (genre, word)
        for genre in brown.categories()
        for word in brown.words(categories=genre))

# Let's break this down, and look at just two genres, news and romance.
# For each genre, we loop over every word in the genre, 
# producing pairs consisting of the genre and the word:
genre_word = [(genre, word)
              for genre in ['news', 'romance']
              for word in brown.words(categories=genre)]
len(genre_word)
# pairs at the beginning of the list genre_word will be of the form ('news', word)
# while those at the end will be of the form ('romance', word)
genre_word[:4]
# [('news', 'The'), ('news', 'Fulton'), ('news', 'County'), ('news', 'Grand')] # [_start-genre]
genre_word[-4:]
# [('romance', 'afraid'), ('romance', 'not'), ('romance', "''"), ('romance', '.')] # [_end-genre]
# We can now use this list of pairs to create a ConditionalFreqDist, 
# and save it in a variable cfd. 
cfd = nltk.ConditionalFreqDist(genre_word)
# As usual, we can type the name of the variable to inspect it,
cfd #<ConditionalFreqDist with 2 conditions>
# and verify it has two conditions:
cfd.conditions()
# ['news', 'romance'] # [_conditions-cfd]
# Let's access the two conditions, and satisfy ourselves that each is just a frequency distribution:
print(cfd['news'])
print(cfd['romance'])
cfd['romance'].most_common(20)
cfd['romance']['could']

# Plotting and Tabulating Distributions
from nltk.corpus import inaugural
# the counts being plotted are the number of times the word occured in a particular speech
cfd = nltk.ConditionalFreqDist(
# It exploits the fact that the filename for each speech,
# e.g., 1865-Lincoln.txt contains the year as the first four characters
        (target, fileid[:4])
        for fileid in inaugural.fileids()
        for w in inaugural.words(fileid)
#         The condition is either of the words america or citizen 
        for target in ['america', 'citizen']
# This code generates the pair  ('america', '1865') for every instance of a word 
# whose lowercased form starts with america — such as Americans — in the file 1865-Lincoln.txt.
        if w.lower().startswith(target))

from nltk.corpus import udhr
# the condition is the name of the language 
# and the counts being plotted are derived from word lengths 
languages = ['Chickasaw', 'English', 'German_Deutsch',
    'Greenlandic_Inuktikut', 'Hungarian_Magyar', 'Ibibio_Efik']
cfd = nltk.ConditionalFreqDist(
        (lang, len(word))
# It exploits the fact that the filename for each language is the language name
#  followed by '-Latin1' (the character encoding).
        for lang in languages
        for word in udhr.words(lang + '-Latin1'))  # @UndefinedVariable

# In the plot() and tabulate() methods, we can optionally specify 
# which conditions to display with a conditions= parameter.
# When we omit it, we get all the conditions.
   
# we can tabulate the cumulative frequency data just for two languages,
#  and for words less than 10 characters long
cfd.tabulate(conditions=['English', 'German_Deutsch'],
# Similarly, we can limit the samples to display with a samples= parameter.
             samples=range(10), cumulative=True)
"""
                  0    1    2    3    4    5    6    7    8    9
       English    0  185  525  883  997 1166 1283 1440 1558 1638 (*)
German_Deutsch    0  171  263  614  717  894 1013 1110 1213 1275
"""# (*) 1,638 words of the English text have 9 or fewer letters

# This makes it possible to load a large quantity of data into
#  a conditional frequency distribution, and then to explore it by plotting 
# or tabulating selected conditions and samples. 
# It also gives us full control over the order of conditions and samples in any displays.

"""
Your Turn: 
Working with the news and romance genres from the Brown Corpus,
find out which days of the week are most newsworthy, and which are most romantic.
Define a variable called days containing a list of days of the week, i.e. ['Monday', ...].
Now tabulate the counts for these words using cfd.tabulate(samples=days).
Now try the same thing using plot in place of tabulate.
You may control the output order of days with the help of an extra parameter: samples=['Monday', ...].
"""
from nltk.corpus import brown
days = ['Monday', 'Tuesday', 'Wednesday','Thursday','Friday','Saturday','Sunday']
cfd = nltk.ConditionalFreqDist(
        (genre, word)
        for genre in ['news', 'romance']
        for word in brown.words(categories=genre))
cfd.tabulate(samples=days)
"""
           Monday   Tuesday Wednesday  Thursday    Friday  Saturday    Sunday
   news        54        43        22        20        41        33        51
romance         2         3         3         1         3         4         5
"""
cfd.plot(samples=days)

#  In general, when we use a list comprehension as a parameter to a function, like  set([w.lower() for w in t]),
#  we are permitted to omit the square brackets and just write: set(w.lower() for w in t). (See the discussion of "generator expressions" in 4.2 for more about this.)

# Generating Random Text with Bigrams
# use a conditional frequency distribution to create a table of bigrams (word pairs).

# The bigrams() function takes a list of words and builds a list of consecutive word pairs.
# Remember that, in order to see the result and not a cryptic "generator object"
sent = ['In', 'the', 'beginning', 'God', 'created', 'the', 'heaven',
  'and', 'the', 'earth', '.']
list(nltk.bigrams(sent))
"""
[('In', 'the'), ('the', 'beginning'), ('beginning', 'God'), ('God', 'created'),
('created', 'the'), ('the', 'heaven'), ('heaven', 'and'), ('and', 'the'),
('the', 'earth'), ('earth', '.')]
"""

def generate_model(cfdist, word, num=15):
    for i in range(num):
        print(word, end=' ')
#         reset word to be the most likely token in that context (using max())
#         next time through the loop, we use that word as our new context.
        word = cfdist[word].max()

text = nltk.corpus.genesis.words('english-kjv.txt')
bigrams = nltk.bigrams(text)
cfd = nltk.ConditionalFreqDist(bigrams)
# after the word living, the most likely word is creature;
cfd['living']
# FreqDist({'creature': 7, 'thing': 4, 'substance': 2, ',': 1, '.': 1, 'soul': 1})
generate_model(cfd, 'living')
# living creature that he said , and the land of the land of the land

"""
As you can see by inspecting the output, 
this simple approach to text generation tends to get stuck in loops; 
another method would be to randomly choose the next word from among the available words.

Generating Random Text:
this program obtains all bigrams from the text of the book of Genesis, 
then constructs a conditional frequency distribution to record which words 
are most likely to follow a given word; e.g., after the word living, the most likely word 
is creature; the generate_random_model() function uses this data, and a seed word, 
to generate random text.
"""
from random import choice
def generate_random_model(cfdist, word, num=15):
    for i in range(num):
        print(word, end=' ')
#         reset word to be the most likely token in that context (using max())
#         next time through the loop, we use that word as our new context.
#         word = cfdist[word].max()
        word = choice(list( w for w in cfdist[word]) ) 
text = nltk.corpus.genesis.words('english-kjv.txt')
bigrams = nltk.bigrams(text) 
cfd = nltk.ConditionalFreqDist(bigrams)
generate_random_model(cfd, 'living')

"""
Example    Description
cfdist = ConditionalFreqDist(pairs)    create a conditional frequency distribution from a list of pairs
cfdist.conditions()    the conditions
cfdist[condition]    the frequency distribution for this condition
cfdist[condition][sample]    frequency for the given sample for this condition
cfdist.tabulate()    tabulate the conditional frequency distribution
cfdist.tabulate(samples, conditions)    tabulation limited to the specified samples and conditions
cfdist.plot()    graphical plot of the conditional frequency distribution
cfdist.plot(samples, conditions)    graphical plot limited to the specified samples and conditions
cfdist1 < cfdist2    test if samples in cfdist1 occur less frequently than in cfdist2
"""

#More Python: Reusing Code
'''a file called: monty.py'''
from monty import *
# Functions
def lexical_diversity(my_text_data):
    word_count = len(my_text_data)
    vocab_size = len(set(my_text_data))
    diversity_score = vocab_size / word_count
    return diversity_score
from nltk.corpus import genesis
kjv = genesis.words('english-kjv.txt')
lexical_diversity(kjv)
# 0.06230453042623537
    
def plural(word):
    if word.endswith('y'):
        return word[:-1] + 'ies'
    elif word[-1] in 'sx' or word[-2:] in ['sh', 'ch']:
        return word + 'es'
    elif word.endswith('an'):
        return word[:-2] + 'en'
    else:
        return word + 's'
plural('fairy')
# 'fairies'
plural('woman')
# 'women'

# Modules
# save your function(s) in a file called (say) text_proc.py. 
# Now, you can access your work simply by importing it from the file:
from text_proc import plural
plural('wish') #wishes
plural('fan')   #fen

# A collection of variable and function definitions in a file is called a Python module. 
# A collection of related modules is called a package. 
# NLTK's code for processing the Brown Corpus is an example of a module, 
# and its collection of code for processing all the different corpora is an example of a package. 
# NLTK itself is a set of packages, sometimes called a library.

# Lexical Resources
'''
Lexicon Terminology:
lexical entry
headword (lemma)
homonyms
'''
# Wordlist Corpora
# NLTK includes some corpora that are nothing more than wordlists. The Words Corpus is the /usr/share/dict/words file from Unix, used by some spell checkers.
# find unusual or mis-spelt words
def unusual_words(text):
    text_vocab = set(w.lower() for w in text if w.isalpha())
#     an existing wordlist
    english_vocab = set(w.lower() for w in nltk.corpus.words.words())
    unusual = text_vocab - english_vocab
    return sorted(unusual)
unusual_words(nltk.corpus.gutenberg.words('austen-sense.txt'))
unusual_words(nltk.corpus.nps_chat.words())

# corpus of stopwords 
from nltk.corpus import stopwords
stopwords.words('english')
# compute what fraction of words in a text are not in the stopwords list: 
from __future__ import division 
def content_fraction(text):
    stopwords = nltk.corpus.stopwords.words('english')
    content = [w for w in text if w.lower() not in stopwords]
    return len(content) / len(text)

content_fraction(nltk.corpus.reuters.words())
# 0.7364374824583169

# solving word puzzles字谜题
# Our program iterates through every word and, for each one, checks whether it meets the conditions.
# It is easy to check obligatory letter and length constraints (and we'll only look for words with six or more letters here). 
# It is trickier to check that candidate solutions only use combinations of the supplied letters, especially since some of the supplied letters appear twice (here, the letter v). 
# The FreqDist comparison method permits us to check that the frequency of each letter in the candidate word is less than or equal to the frequency of the corresponding letter in the puzzle.
puzzle_letters = nltk.FreqDist('egivrvonl')
obligatory = 'r'
wordlist = nltk.corpus.words.words()
[w for w in wordlist if len(w) >= 6
                    and obligatory in w
                    and nltk.FreqDist(w) <= puzzle_letters]
'''
['glover', 'gorlin', 'govern', 'grovel', 'ignore', 'involver', 'lienor',
'linger', 'longer', 'lovering', 'noiler', 'overling', 'region', 'renvoi',
'revolving', 'ringle', 'roving', 'violer', 'virole']
'''
# Names corpus, containing 8,000 first names categorized by gender.
names = nltk.corpus.names
names.fileids()
# ['female.txt', 'male.txt']
male_names = names.words('male.txt')
female_names = names.words('female.txt')
[w for w in male_names if w in female_names]
'''
['Abbey', 'Abbie', 'Abby', 'Addie', 'Adrian', 'Adrien', 'Ajay', 'Alex', 'Alexis',
'Alfie', 'Ali', 'Alix', 'Allie', 'Allyn', 'Andie', 'Andrea', 'Andy', 'Angel',
'Angie', 'Ariel', 'Ashley', 'Aubrey', 'Augustine', 'Austin', 'Averil', ...]
'''
# It is well known that names ending in the letter a are almost always female. 
# We can see this and some other patterns in the graph
cfd = nltk.ConditionalFreqDist(
        (fileid, name[-1])
        for fileid in names.fileids()
        for name in names.words(fileid))
cfd.plot()

# A Pronouncing Dictionary
#  NLTK includes the CMU Pronouncing Dictionary for US English, which was designed for use by speech synthesizers.
# The symbols in the CMU Pronouncing Dictionary are from the Arpabet, described in more detail at http://en.wikipedia.org/wiki/Arpabet
entries = nltk.corpus.cmudict.entries()
len(entries)
for entry in entries[42371:42379]:
    print(entry)

# For each word, this lexicon provides a list of phonetic codes — distinct labels for each contrastive sound — known as phones.
# Each entry consists of two parts, and we can process these individually using a more complex version of the for statement.
for word, pron in entries:
    if len(pron) == 3:
#         it assigns the contents of pron to three new variables ph1, ph2 and ph3.
        ph1, ph2, ph3 = pron
        if ph1 == 'P' and ph3 == 'T':
            print(word, ph2, end=' ')
# find rhyming words
# used inside a list comprehension
# finds all words whose pronunciation ends with a syllable sounding like nicks.
syllable = ['N', 'IH0', 'K', 'S']
[word for word, pron in entries if pron[-4:] == syllable]
'''
Notice that the one pronunciation is spelt in several ways: 
nics, niks, nix, even ntic's with a silent t, for the word atlantic's. 
Let's look for some other mismatches between pronunciation and writing. 
Can you summarize the purpose of the following examples and explain how they work?
'''  
# 查找最后一个发音为M同时最后一个字母为n的单词
[w for w, pron in entries if pron[-1] == 'M' and w[-1] == 'n']
# ['autumn', 'column', 'condemn', 'damn', 'goddamn', 'hymn', 'solemn']
# 查找以N发音但首字母不是n的单词前俩字母，寻找共性patterns
sorted(set(w[:2] for w, pron in entries if pron[0] == 'N' and w[0] != 'n'))
# ['gn', 'kn', 'mn', 'pn']

# The phones contain digits to represent primary stress (1), secondary stress (2) and no stress (0).
# extract the stress digits and then scan our lexicon to find words having a particular stress pattern.
def stress(pron):
#     a doubly-nested for loop
    return [char for phone in pron for char in phone if char.isdigit()] 
# stress() is invoked inside the condition of a list comprehension
[w for w, pron in entries if stress(pron) == ['0', '1', '0', '2', '0']]
'''
['abbreviated', 'abbreviated', 'abbreviating', 'accelerated', 'accelerating',
'accelerator', 'accelerators', 'accentuated', 'accentuating', 'accommodated',
'accommodating', 'accommodative', 'accumulated', 'accumulating', 'accumulative', ...]
'''
[w for w, pron in entries if stress(pron) == ['0', '2', '0', '1', '0']]
'''
['abbreviation', 'abbreviations', 'abomination', 'abortifacient', 'abortifacients',
'academicians', 'accommodation', 'accommodations', 'accreditation', 'accreditations',
'accumulation', 'accumulations', 'acetylcholine', 'acetylcholine', 'adjudication', ...]
'''
# find minimally-contrasting sets of words
#  Here we find all the p-words consisting of three sounds, 
# and group them according to their first and last sounds.
p3 = [(pron[0]+'-'+pron[2], word)
      for (word, pron) in entries
      if pron[0] == 'P' and len(pron) == 3]
cfd = nltk.ConditionalFreqDist(p3)
for template in sorted(cfd.conditions()):
    if len(cfd[template]) > 10:
        words = sorted(cfd[template])
        wordstring = ' '.join(words)
        print(template, wordstring[:70] + "...")
'''
P-CH patch pautsch peach perch petsch petsche piche piech pietsch pitch pit...
P-K pac pack paek paik pak pake paque peak peake pech peck peek perc perk ...
P-L pahl pail paille pal pale pall paul paule paull peal peale pearl pearl...
P-N paign pain paine pan pane pawn payne peine pen penh penn pin pine pinn...
P-P paap paape pap pape papp paup peep pep pip pipe pipp poop pop pope pop...
P-R paar pair par pare parr pear peer pier poor poore por pore porr pour...
P-S pace pass pasts peace pearse pease perce pers perse pesce piece piss p...
P-T pait pat pate patt peart peat peet peete pert pet pete pett piet piett...
P-UW1 peru peugh pew plew plue prew pru prue prugh pshew pugh...
'''
# Rather than iterating over the whole dictionary, we can also access it by looking up particular words.
prondict = nltk.corpus.cmudict.dict()
prondict['fire']
# [['F', 'AY1', 'ER0'], ['F', 'AY1', 'R']]
prondict['blog'] = [['B', 'L', 'AA1', 'G']]
prondict['blog']
# If we try to look up a non-existent key, we get a KeyError.
# We can use any lexical resource to process a text, 
# e.g., to filter out words having some lexical property (like nouns), 
# or mapping every word of the text. For example, the following 
# text-to-speech function looks up each word of the text in the pronunciation dictionary.
text = ['natural', 'language', 'processing']
[ph for w in text for ph in prondict[w][0]]
# ['N', 'AE1', 'CH', 'ER0', 'AH0', 'L', 'L', 'AE1', 'NG', 'G', 'W', 'AH0', 'JH',
# 'P', 'R', 'AA1', 'S', 'EH0', 'S', 'IH0', 'NG']

#  Comparative Wordlists
# NLTK includes so-called Swadesh wordlists, lists of about 200 common words in several languages. 
# The languages are identified using an ISO 639 two-letter code.
from nltk.corpus import swadesh
swadesh.fileids()
# ['be', 'bg', 'bs', 'ca', 'cs', 'cu', 'de', 'en', 'es', 'fr', 'hr', 'it', 'la', 'mk',
# 'nl', 'pl', 'pt', 'ro', 'ru', 'sk', 'sl', 'sr', 'sw', 'uk']
swadesh.words('en')
# ['I', 'you (singular), thou', 'he', 'we', 'you (plural)', 'they', 'this', 'that',
# 'here', 'there', 'who', 'what', 'where', 'when', 'how', 'not', 'all', 'many', 'some',
# 'few', 'other', 'one', 'two', 'three', 'four', 'five', 'big', 'long', 'wide', ...]
# We can access cognate words同源词 from multiple languages using the entries() method, specifying a list of languages.
fr2en = swadesh.entries(['fr', 'en'])
fr2en
# [('je', 'I'), ('tu, vous', 'you (singular), thou'), ('il', 'he'), ...]
# convert this into a simple dictionary
translate = dict(fr2en)
translate['chien']
# 'dog'
translate['jeter']
# 'throw'
# We can make our simple translator more useful by adding other source languages. 
# Let's get the German-English and Spanish-English pairs, 
# convert each to a dictionary using dict(), 
# then update our original translate dictionary with these additional mappings:
de2en = swadesh.entries(['de', 'en'])    # German-English
es2en = swadesh.entries(['es', 'en'])    # Spanish-English
translate.update(dict(de2en))
translate.update(dict(es2en))
translate['Hund']
# 'dog'
translate['perro']
# 'dog'
# We can compare words in various Germanic and Romance languages:
languages = ['en', 'de', 'nl', 'es', 'fr', 'pt', 'la']
for i in [139, 140, 141, 142]:
    print(swadesh.entries(languages)[i])
'''
('say', 'sagen', 'zeggen', 'decir', 'dire', 'dizer', 'dicere')
('sing', 'singen', 'zingen', 'cantar', 'chanter', 'cantar', 'canere')
('play', 'spielen', 'spelen', 'jugar', 'jouer', 'jogar, brincar', 'ludere')
('float', 'schweben', 'zweven', 'flotar', 'flotter', 'flutuar, boiar', 'fluctuare')
'''

# Shoebox and Toolbox Lexicons
# Perhaps the single most popular tool used by linguists for managing data is Toolbox, 
# previously known as Shoebox since it replaces the field linguist's traditional shoebox 
# full of file cards. Toolbox is freely downloadable from 
# http://www.sil.org/computing/toolbox/.

# A Toolbox file consists of a collection of entries, where each entry is made up of one or more fields.
# Most fields are optional or repeatable, which means that this kind of lexical resource cannot be treated as a table or spreadsheet.
# Here is a dictionary for the Rotokas language. We see just the first entry, for the word kaa meaning "to gag":
from nltk.corpus import toolbox
toolbox.entries('rotokas.dic')  # @UndefinedVariable
'''
[('kaa', [('ps', 'V'), ('pt', 'A'), ('ge', 'gag'), ('tkp', 'nek i pas'),
('dcsv', 'true'), ('vx', '1'), ('sc', '???'), ('dt', '29/Oct/2005'),
('ex', 'Apoka ira kaaroi aioa-ia reoreopaoro.'),
('xp', 'Kaikai i pas long nek bilong Apoka bikos em i kaikai na toktok.'),
('xe', 'Apoka is gagging from food while talking.')]), ...]
'''
# Entries consist of a series of attribute-value pairs, 
# like ('ps', 'V') to indicate that the part-of-speech is 'V' (verb), 
# and ('ge', 'gag') to indicate that the gloss-into-English is 'gag'. 
# The last three pairs contain an example sentence in Rotokas and its translations into 
# Tok Pisin and English.

# The loose structure of Toolbox files makes it hard for us to do much more with them at this stage. XML provides a powerful way to process this kind of corpus and we will return to this topic in 11..
# The Rotokas language is spoken on the island of Bougainville, Papua New Guinea. This lexicon was contributed to NLTK by Stuart Robinson. 
# Rotokas is notable for having an inventory of just 12 phonemes (contrastive sounds), http://en.wikipedia.org/wiki/Rotokas_language

# WordNet
# WordNet is a semantically-oriented dictionary of English, similar to a traditional thesaurus but with a richer structure. 
# NLTK includes the English WordNet, with 155,287 words and 117,659 synonym sets.

# Senses and Synonyms感官和同义词
from nltk.corpus import wordnet as wn
wn.synsets('motorcar')  # @UndefinedVariable
# [Synset('car.n.01')]
# the first noun sense of car. 
# Thus, motorcar has just one possible meaning and it is identified as car.n.01, 
# The entity car.n.01 is called a synset, or "synonym set", a collection of synonymous words (or "lemmas"):
wn.synset('car.n.01').lemma_names()  # @UndefinedVariable
# ['car', 'auto', 'automobile', 'machine', 'motorcar']
# Each word of a synset can have several meanings, e.g., 
# car can also signify a train carriage, a gondola, or an elevator car. 
# However, we are only interested in the single meaning that is common to all words of the above synset. 
# Synsets also come with a prose definition and some example sentences:
wn.synset('car.n.01').definition()  # @UndefinedVariable
# 'a motor vehicle with four wheels; usually propelled by an internal combustion engine'
wn.synset('car.n.01').examples()  # @UndefinedVariable
# ['he needs a car to get to work']

# Although definitions help humans to understand the intended meaning of a synset, 
# the words of the synset are often more useful for our programs. 
# To eliminate ambiguity, we will identify these words as car.n.01.automobile, 
# car.n.01.motorcar, and so on. 
# This pairing of a synset with a word is called a lemma. 
# We can get all the lemmas for a given synset, look up a particular lemma, 
# get the synset corresponding to a lemma, and get the "name" of a lemma:
wn.synset('car.n.01').lemmas()  # @UndefinedVariable
# [Lemma('car.n.01.car'), Lemma('car.n.01.auto'), Lemma('car.n.01.automobile'),
# Lemma('car.n.01.machine'), Lemma('car.n.01.motorcar')]
wn.lemma('car.n.01.automobile')  # @UndefinedVariable
# Lemma('car.n.01.automobile')
wn.lemma('car.n.01.automobile').synset()  # @UndefinedVariable
# Synset('car.n.01')
wn.lemma('car.n.01.automobile').name()  # @UndefinedVariable
# 'automobile'
# Unlike the word motorcar, which is unambiguous and has one synset, the word car is ambiguous, having five synsets:
wn.synsets('car')  # @UndefinedVariable
# [Synset('car.n.01'), Synset('car.n.02'), Synset('car.n.03'), Synset('car.n.04'),
# Synset('cable_car.n.01')]
for synset in wn.synsets('car'):  # @UndefinedVariable
    print(synset.lemma_names())
'''
['car', 'auto', 'automobile', 'machine', 'motorcar']
['car', 'railcar', 'railway_car', 'railroad_car']
['car', 'gondola']
['car', 'elevator_car']
['cable_car', 'car']
'''
# For convenience, we can access all the lemmas involving the word car as follows.
wn.lemmas('car')  # @UndefinedVariable
# [Lemma('car.n.01.car'), Lemma('car.n.02.car'), Lemma('car.n.03.car'),
# Lemma('car.n.04.car'), Lemma('cable_car.n.01.car')]

# Your Turn: Write down all the senses of the word "dish" that you can think of. 
# Now, explore this word with the help of WordNet, using the same operations we used above.
wn.synsets('dish')  # @UndefinedVariable
# [Synset('dish.n.01'), Synset('dish.n.02'), Synset('dish.n.03'), Synset('smasher.
# n.02'), Synset('dish.n.05'), Synset('cup_of_tea.n.01'), Synset('serve.v.06'), Sy
# nset('dish.v.02')]
'''
['dish']
['dish']
['dish', 'dishful']
['smasher', 'stunner', 'knockout', 'beauty', 'ravisher', 'sweetheart', 'peach', 'lul', 'looker', 'mantrap', 'dish']
['dish', 'dish_aerial', 'dish_antenna', 'saucer']
['cup_of_tea', 'bag', 'dish']
['serve', 'serve_up', 'dish_out', 'dish_up', 'dish']
['dish']
'''
for synset in wn.synsets('dish'):  # @UndefinedVariable
    print(synset.lemma_names())
    print(synset.definition())
    print(synset.examples())
for lemma in wn.lemmas('dish'):  # @UndefinedVariable
    print(lemma.synset())
    print(lemma.name())

# The WordNet Hierarchy
# unique beginners or root synsets,such as abstract concepts: Entity, State, Event
# WordNet makes it easy to navigate between concepts.
# For example, given a concept like motorcar, 
# we can look at the concepts that are more specific; the (immediate) hyponyms下义词.
motorcar = wn.synset('car.n.01')  # @UndefinedVariable
types_of_motorcar = motorcar.hyponyms()
types_of_motorcar[0]
# Synset('ambulance.n.01')
sorted(lemma.name() for synset in types_of_motorcar for lemma in synset.lemmas())
'''
['Model_T', 'S.U.V.', 'SUV', 'Stanley_Steamer', 'ambulance', 'beach_waggon',
'beach_wagon', 'bus', 'cab', 'compact', 'compact_car', 'convertible',
'coupe', 'cruiser', 'electric', 'electric_automobile', 'electric_car',
'estate_car', 'gas_guzzler', 'hack', 'hardtop', 'hatchback', 'heap',
'horseless_carriage', 'hot-rod', 'hot_rod', 'jalopy', 'jeep', 'landrover',
'limo', 'limousine', 'loaner', 'minicar', 'minivan', 'pace_car', 'patrol_car',
'phaeton', 'police_car', 'police_cruiser', 'prowl_car', 'race_car', 'racer',
'racing_car', 'roadster', 'runabout', 'saloon', 'secondhand_car', 'sedan',
'sport_car', 'sport_utility', 'sport_utility_vehicle', 'sports_car', 'squad_car',
'station_waggon', 'station_wagon', 'stock_car', 'subcompact', 'subcompact_car',
'taxi', 'taxicab', 'tourer', 'touring_car', 'two-seater', 'used-car', 'waggon',
'wagon']
'''
# We can also navigate up the hierarchy by visiting hypernyms上位词.
# Some words have multiple paths, because they can be classified in more than one way. 
# There are two paths between car.n.01 and entity.n.01 
# because wheeled_vehicle.n.01 can be classified as both a vehicle and a container.
motorcar.hypernyms()
# [Synset('motor_vehicle.n.01')]
paths = motorcar.hypernym_paths()
len(paths)
# 2
[synset.name() for synset in paths[0]]
# ['entity.n.01', 'physical_entity.n.01', 'object.n.01', 'whole.n.02', 'artifact.n.01',
# 'instrumentality.n.03', 'container.n.01', 'wheeled_vehicle.n.01',
# 'self-propelled_vehicle.n.01', 'motor_vehicle.n.01', 'car.n.01']
[synset.name() for synset in paths[1]]
# ['entity.n.01', 'physical_entity.n.01', 'object.n.01', 'whole.n.02', 'artifact.n.01',
# 'instrumentality.n.03', 'conveyance.n.03', 'vehicle.n.01', 'wheeled_vehicle.n.01',
# 'self-propelled_vehicle.n.01', 'motor_vehicle.n.01', 'car.n.01']

# We can get the most general hypernyms (or root hypernyms) of a synset as follows:
motorcar.root_hypernyms()
# [Synset('entity.n.01')]

'''
Your Turn: Try out NLTK's convenient graphical WordNet browser: nltk.app.wordnet(). 
Explore the WordNet hierarchy by following the hypernym and hyponym links.
'''
nltk.app.wordnet()

# More Lexical Relations
# Hypernyms and hyponyms are called lexical relations because they relate one synset to another. 
# Another important way to navigate the WordNet network is from 
# items to their components (meronyms) or to the things they are contained in (holonyms)
#  For example, the parts of a tree are its trunk, crown, and so on; the part_meronyms().
# The substance a tree is made of includes heartwood and sapwood; the substance_meronyms(). 
# A collection of trees forms a forest; the member_holonyms()
wn.synset('tree.n.01').part_meronyms()  # @UndefinedVariable
# [Synset('burl.n.02'), Synset('crown.n.07'), Synset('limb.n.02'),
# Synset('stump.n.01'), Synset('trunk.n.01')]
wn.synset('tree.n.01').substance_meronyms()  # @UndefinedVariable
# [Synset('heartwood.n.01'), Synset('sapwood.n.01')]
wn.synset('tree.n.01').member_holonyms()  # @UndefinedVariable
# [Synset('forest.n.01')]

# To see just how intricate things can get, consider the word mint, which has several closely-related senses. 
# We can see that mint.n.04 is part of mint.n.02 and the substance from which mint.n.05 is made.
for synset in wn.synsets('mint', wn.NOUN):  # @UndefinedVariable
    print(synset.name() + ':', synset.definition())
'''
batch.n.02: (often followed by `of') a large number or amount or extent
mint.n.02: any north temperate plant of the genus Mentha with aromatic leaves and
           small mauve flowers
mint.n.03: any member of the mint family of plants
mint.n.04: the leaves of a mint plant used fresh or candied
mint.n.05: a candy that is flavored with a mint oil
mint.n.06: a plant where money is coined by authority of the government
'''
wn.synset('mint.n.04').part_holonyms()  # @UndefinedVariable
# [Synset('mint.n.02')]
wn.synset('mint.n.04').substance_holonyms()  # @UndefinedVariable
# [Synset('mint.n.05')]

# There are also relationships between verbs. 
# For example, the act of walking involves the act of stepping, 
# so walking entails stepping. Some verbs have multiple entailments蕴涵:
wn.synset('walk.v.01').entailments()  # @UndefinedVariable
# [Synset('step.v.01')]
wn.synset('eat.v.01').entailments()  # @UndefinedVariable
# [Synset('chew.v.01'), Synset('swallow.v.01')]
wn.synset('tease.v.03').entailments()  # @UndefinedVariable
# [Synset('arouse.v.07'), Synset('disappoint.v.01')]

# Some lexical relationships hold between lemmas, e.g., antonymy反义关系:
wn.lemma('supply.n.02.supply').antonyms()  # @UndefinedVariable
# [Lemma('demand.n.02.demand')]
wn.lemma('rush.v.01.rush').antonyms()  # @UndefinedVariable
# [Lemma('linger.v.04.linger')]
wn.lemma('horizontal.a.01.horizontal').antonyms()  # @UndefinedVariable
# [Lemma('inclined.a.02.inclined'), Lemma('vertical.a.01.vertical')]
wn.lemma('staccato.r.01.staccato').antonyms()  # @UndefinedVariable
# [Lemma('legato.r.01.legato')]

# You can see the lexical relations, and the other methods defined on a synset, using dir(), for example: 
dir(wn.synset('harmony.n.02'))  # @UndefinedVariable

# Semantic Similarity
# If two synsets share a very specific hypernym — 
# one that is low down in the hypernym hierarchy — they must be closely related.
right = wn.synset('right_whale.n.01')  # @UndefinedVariable
orca = wn.synset('orca.n.01')  # @UndefinedVariable
minke = wn.synset('minke_whale.n.01')  # @UndefinedVariable
tortoise = wn.synset('tortoise.n.01')  # @UndefinedVariable
novel = wn.synset('novel.n.01')  # @UndefinedVariable
right.lowest_common_hypernyms(minke)
# [Synset('baleen_whale.n.01')]
right.lowest_common_hypernyms(orca)
# [Synset('whale.n.02')]
right.lowest_common_hypernyms(tortoise)
# [Synset('vertebrate.n.01')]
right.lowest_common_hypernyms(novel)
# [Synset('entity.n.01')]

# Of course we know that whale is very specific (and baleen whale even more so), 
# while vertebrate is more general and entity is completely general. 
# We can quantify this concept of generality by looking up the depth of each synset:
wn.synset('baleen_whale.n.01').min_depth()  # @UndefinedVariable
# 14
wn.synset('whale.n.02').min_depth()  # @UndefinedVariable
# 13
wn.synset('vertebrate.n.01').min_depth()  # @UndefinedVariable
# 8
wn.synset('entity.n.01').min_depth()  # @UndefinedVariable
# 0
# Similarity measures have been defined over the collection of WordNet synsets which incorporate the above insight.
# For example, path_similarity assigns a score in the range 0–1 based on 
# the shortest path that connects the concepts in the hypernym hierarchy 
# (-1 is returned in those cases where a path cannot be found).
# Comparing a synset with itself will return 1.
# Consider the following similarity scores, relating right whale to 
# minke whale, orca, tortoise, and novel. Although the numbers won't mean much, 
# they decrease as we move away from the semantic space of sea creatures to inanimate objects无生命的物体.
right.path_similarity(minke)
# 0.25
right.path_similarity(orca)
# 0.16666666666666666
right.path_similarity(tortoise)
# 0.07692307692307693
right.path_similarity(novel)
# 0.043478260869565216

# Several other similarity measures are available; 
# you can type help(wn) for more information. 
# NLTK also includes VerbNet, a hierarhical verb lexicon linked to WordNet. 
# It can be accessed with nltk.corpus.verbnet.

# Significant sources of published corpora are the Linguistic Data Consortium (LDC) and the European Language Resources Agency (ELRA). Hundreds of annotated text and speech corpora are available in dozens of languages. Non-commercial licences permit the data to be used in teaching and research. For some corpora, commercial licenses are also available (but for a higher fee).

# A good tool for creating annotated text corpora is called Brat, and available from http://brat.nlplab.org/.

# These and many other language resources have been documented using OLAC Metadata, and can be searched via the OLAC homepage at  http://www.language-archives.org/. Corpora List is a mailing list for discussions about corpora, and you can find resources by searching the list archives or posting to the list. The most complete inventory of the world's languages is Ethnologue, http://www.ethnologue.com/. Of 7,000 languages, only a few dozen have substantial digital resources suitable for use in NLP.




