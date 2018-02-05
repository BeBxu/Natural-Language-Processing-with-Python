#!/usr/bin/python
# -*- coding: utf-8 -*-
from nltk.book import *

def lexical_diversity(text):
    return len(set(text)) / len(text)

def percentage(count, total):
    return 100 * count / total
#think of a text as nothing more than a sequence of words and punctuation
sent1 = ['Call', 'me', 'Ishmael', '.']
sent1
lexical_diversity(sent1)
# from nltk.book import * 引入后可调用
sent2
sent3
#链接俩链表 concatenation
['Monty', 'Python'] + ['and', 'the', 'Holy', 'Grail']
sent4 + sent1
#appending 
sent1.append("Some")
#the item that occurs at an index such as 173
text4[173]
#do the converse; given a word, find the index of when it first occurs:
text4.index('awaken')
#slicing 切片: access sublists 
text5[16715:16735]
text6[1600:1625]
#Traceback : runtime error
#can omit the first number if the slice begins at the start of the list
sent = ['word1', 'word2', 'word3', 'word4', 'word5', 'word6', 'word7', 'word8', 'word9', 'word10']
sent[:3]
#omit the second number if the slice goes to the end 
text2[141525:]
#modify an element of a list by assigning to one of its index values
sent[0] = 'First'
sent[9] = 'Last'
len(sent)
# replace an entire slice with new material 最后一个sent[9]没有被修改
sent[1:9] = ['Second', 'Third']
sent
# assignment 赋值
my_sent = ['Bravely', 'bold', 'Sir', 'Robin', ',', 'rode', 'forth', 'from', 'Camelot', '.']
noun_phrase = my_sent[1:4]
wOrDs = sorted(noun_phrase)
#reserved words保留字 such as def, if, not, and import.
# should start the name with a letter, optionally followed by digits (0 to 9) or letters.
# Names are case-sensitive
# Variable names cannot contain whitespace, but you can separate words using an underscore
# Be careful not to insert a hyphen instead of an underscore
#  since Python interprets the "-" as a minus sign.

#assign a string to a variable [1], index a string [2], and slice a string 
name = 'Monty'
name[0]
name[:4]
name * 2
name + '!'
' '.join(['Monty', 'Python'])
'Monty Python'.split()

saying = ['After', 'all', 'is', 'said', 'and', 'done', 'more', 'is', 'said', 'than', 'done']
tokens = set(saying)
tokens = sorted(tokens)
tokens[-2:]

#frequency distribution
#find the 50 most frequent words
fdist1 = FreqDist(text1)
print(fdist1)
fdist1.most_common(50)
fdist1['whale']
# words tell us nothing about the text; they're just English "plumbing."
#generate a cumulative frequency plot for these words
fdist1.plot(50, cumulative=True)
#hapaxes：words that occur once only
fdist1.hapaxes()
#long words
#We would like to find the words from the vocabulary of the text that are more than 15 characters long
#Let's call this property P, so that P(w) is true if and only if w is more than 15 characters long. Now we can express the words of interest using mathematical set notation as shown in (1a). This means "the set of all w such that w is an element of V (the vocabulary) and w has property P".
#    {w | w ∈ V & P(w)}
V = set(text1)
#Note that it produces a list, not a set, which means that duplicates are possible.
long_words = [w for w in V if len(w) > 15]
sorted(long_words)
#Here are all words from the chat corpus that are longer than seven characters, that occur more than seven times:
fdist5 = FreqDist(text5)
sorted(w for w in set(text5) if len(w) > 7 and fdist5[w] > 7)

#collocation：a sequence of words that occur together unusually often
#bigrams: extracting from a text a list of word pairs
from nltk.util import bigrams
list(bigrams(['more', 'is', 'said', 'than', 'done']))
#find bigrams that occur more often than we would expect based on the frequency of the individual words
text4.collocations()
text8.collocations()
#the distribution of word lengths in a text
[len(w) for w in text1]
fdist = FreqDist(len(w) for w in text1)
print(fdist)
fdist
# how frequent the different lengths of word are (e.g., how many words of length four appear in the text, are there more words of length five than length four, etc)
fdist.most_common()
fdist.max()
fdist[3]
fdist.freq(3)
#Functions Defined for NLTK's Frequency Distributions
#http://www.nltk.org/book/ch01.html#tab-freqdist

#common pattern: [w for w in text if condition ]
#http://www.nltk.org/book/ch01.html#tab-word-tests
[w for w in sent7 if len(w) < 4]
[w for w in sent7 if len(w) <= 4]
[w for w in sent7 if len(w) == 4]
[w for w in sent7 if len(w) != 4]
# words ending with -ableness; 
sorted(w for w in set(text1) if w.endswith('ableness'))
#words containing gnt; 
sorted(term for term in set(text4) if 'gnt' in term)
#words having an initial capital; 
sorted(item for item in set(text6) if item.istitle())
#words consisting entirely of digits
sorted(item for item in set(sent7) if item.isdigit())

#using conjunction and disjunction: c1 and c2, c1 or c2.
sorted(w for w in set(text7) if '-' in w and 'index' in w)
sorted(wd for wd in set(text3) if wd.istitle() and len(wd) > 10)
#不都是小写字母
sorted(w for w in set(sent7) if not w.islower())
sorted(t for t in set(text2) if 'cie' in t or 'cei' in t)

#list comprehension链表推导
[len(w) for w in text1]
[w.upper() for w in text1]

#vocabulary size
len(text1)
len(set(text1))
#not double-counting words like This and this, which differ only in capitalization
len(set(word.lower() for word in text1))
#eliminate numbers and punctuation from the vocabulary count 
len(set(word.lower() for word in text1 if word.isalpha()))

from __future__ import print_function
word = 'cat'
if len(word) < 5:
    print('word length is less than 5')
for word in ['Call', 'me', 'Ishmael', '.']:
    print(word)
    
# First, we create a list of cie and cei words, 
#then we loop over each item and print it. 
#Notice the extra information given in the print statement: end=' '. 
#This tells Python to print a space (not the default newline) after each word.
tricky = [w for w in text1 if 'cie' in w or 'cei' in w]
for t in tricky:
    print(t, end=' ')


