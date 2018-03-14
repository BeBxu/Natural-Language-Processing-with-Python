#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import division
import nltk
from boto.beanstalk.response import SolutionStackDescription
# 1.☼ Create a variable phrase containing a list of words. 
# Review the operations described in the previous chapter, including 
# addition, multiplication, indexing, slicing, and sorting.
words = ["hello","world","natural","language","processing","python"]
words[1:4]+words[-1:]
# ['world', 'natural', 'language', 'python']
words[1:4]*3
# 乘数只能是int类型
# ['world', 'natural', 'language', 'world', 'natural', 'language', 'world', 'natural', 'language']
words[-1]
# 'python' str类型
words[-1:]
# ['python'] list类型
sorted(words)
# ['hello', 'language', 'natural', 'processing', 'python', 'world']
# 补充两个倒排
sorted(words,reverse=True)
# ['world', 'python', 'processing', 'natural', 'language', 'hello']
sorted(words)[::-1]
# ['world', 'python', 'processing', 'natural', 'language', 'hello']

#2. ☼ Use the corpus module to explore austen-persuasion.txt. How many word tokens does this book have? How many word types?
# nltk.corpus.gutenberg.fileids() austen-persuasion.txt
persuasion = nltk.corpus.gutenberg.words('austen-emma.txt')
#Tokens
len(persuasion)
# 192427
#Word types
len(set(persuasion))
# 7811

# 3.☼ Use the Brown corpus reader nltk.corpus.brown.words() 
# or the Web text corpus reader nltk.corpus.webtext.words() to access some sample text in two different genres.
from nltk.corpus import brown
# brown.categories()
news_text = brown.words(categories='news')
reviews_text = brown.words(categories='reviews')
# OR
brown.words(categories=['news', 'reviews'])
from nltk.corpus import webtext
# webtext.fileids()
webtext.words('singles.txt')
webtext.words('overheard.txt')

# 4.☼ Read in the texts of the State of the Union addresses, using the state_union corpus reader. 
# Count occurrences of men, women, and people in each document. 
# What has happened to the usage of these words over time?
from nltk.corpus import state_union
search_terms = ['men', 'women', 'people']
for fileid in state_union.fileids():
#     fdist = nltk.FreqDist(word for target in search_terms for word in state_union.words(fileid) if word.lower().startswith(target))
    fdist = nltk.FreqDist(state_union.words(fileid))
    for term in search_terms:
        print(fileid, term, fdist[term])

#over time
# years = [fileid[:4] for fileid in state_union.fileids()]
'''
[
(genre, fileid[:4])
for genre in ['men', 'women', 'people']
for fileid in state_union.fileids()
for word in state_union.words(fileid) if word==genre
]
    
cfd = nltk.ConditionalFreqDist(
          (target, fileid[:4])
          for fileid in state_union.fileids()
          for w in state_union.words(fileid)
          for target in ['men', 'women', 'people']
          if w.lower().startswith(target))
'''
cfd = nltk.ConditionalFreqDist(
        (genre, fileid[:4])
        for genre in search_terms
        for fileid in state_union.fileids()
        for word in state_union.words(fileid) if word==genre) #判断条件可酌情修改
cfd.tabulate()
cfd.plot()        

# 5.☼ Investigate the holonym-meronym relations for some nouns. 整体-部分关系
# Remember that there are three kinds of holonym-meronym relation, so you need to use: 
# member_meronyms(), 部件 成员
# part_meronyms(), 部件
# substance_meronyms(), 部件本质是此词的
# member_holonyms(), 
# part_holonyms(), 
# and substance_holonyms().
'''
Meronym and holonym refer to the part-whole relations of words. 
Whereas a meronym is the name of a constituent part of a concept, 
a holonym is the name of the whole of which the meronym is a part
(i.e., P1 is a meronym of Q1 if P1 is a part of Q1, 
and Q2 is a holonym of P2 if P2 is a part of Q2). 
Furthermore, in Wordnet, some of the categories of meronym relations include:
1. Part of mernonym: P1 is a part meronym of Q1 if P1 is a component part of Q1.
Example Query Word: battery
Part Meronym(s): electrode, pole(terminal).
2. Member memronym: P1 is a member meronym of Q1 if P1 is a member of Q1.
Example Query Word: forest
Member Meronym(s): tree, underbrush
3. Substance memronym: P1 is a substance meronym of Q1 if P1 is the stuff that Q1 is made of.
Example Query Word: chalk
Substance Meronym(s): calcium carbonate
'''
from nltk.corpus import wordnet as wn
wn.synset('forest.n.01').member_meronyms()  # @UndefinedVariable
# [Synset('tree.n.01'), Synset('underbrush.n.01')]
wn.synset('battery.n.02').part_meronyms()  # @UndefinedVariable
# [Synset('electrode.n.01'), Synset('terminal.n.02')]
wn.synset('chalk.n.01').substance_meronyms() # @UndefinedVariable
# [Synset('calcium_carbonate.n.01')]

wn.synset('tree.n.01').member_holonyms() # @UndefinedVariable
# [Synset('forest.n.01')]
wn.synset('underbrush.n.01').member_holonyms() # @UndefinedVariable
# [Synset('forest.n.01')]
wn.synset('electrode.n.01').part_holonyms() # @UndefinedVariable
# [Synset('battery.n.02'), Synset('electrolytic_cell.n.01'), Synset('electronic_equipment.n.01'), Synset('tube.n.02')]
wn.synset('terminal.n.02').part_holonyms() # @UndefinedVariable
# [Synset('battery.n.02'), Synset('electrical_device.n.01')]
wn.synset('calcium_carbonate.n.01').substance_holonyms() # @UndefinedVariable
# [Synset('calcite.n.01'), Synset('chalk.n.01')]

# 6.☼ In the discussion of comparative wordlists, 
# we created an object called translate which you could look up using words 
# in both German and Spanish in order to get corresponding words in English. 
# What problem might arise with this approach? 
# Can you suggest a way to avoid this problem?
from nltk.corpus import swadesh
translate = dict()
de2en = swadesh.entries(['de', 'en'])    # German-English
es2en = swadesh.entries(['es', 'en'])    # Spanish-English
translate.update(dict(de2en))
translate.update(dict(es2en))
translate['Hund']
# 'dog'
translate['perro']
# 'dog'
# Problem: 查询值没有做处理，不够robust. 例如查询translate['hund']就不能得到正确结果
# Solution: 构造好（key,value）pair，再update一次，可根据需要适当对键值进行处理，比如忽略大小写，单复数变换，stem之类的。
# 重复键值对会保持下来
translate.update(dict( (key.lower(),value) for key,value in de2en))
translate.update(dict( (key.lower(),value) for key,value in es2en))

# 7.☼ According to Strunk and White's Elements of Style, the word however, 
# used at the start of a sentence, means "in whatever way" or "to whatever extent", 
# and not "nevertheless". They give this example of correct usage: 
# However you advise him, he will probably do as he thinks best. 
# (http://www.bartleby.com/141/strunk3.html) 
# Use the concordance tool to study actual usage of this word in the various texts 
# we have been considering. 
# See also the LanguageLog posting "Fossilized prejudices about 'however'" at  
# http://itre.cis.upenn.edu/~myl/languagelog/archives/001913.html
    
emma = nltk.Text(nltk.corpus.gutenberg.words('austen-emma.txt'))
# emma.concordance("However") 大小写不敏感,等价于emma2
# emma2 = nltk.text.ConcordanceIndex(list(nltk.corpus.gutenberg.words('austen-emma.txt')), key=lambda s:s.lower())
# 可以删去key=，也可以去掉.lower(),list()同样可以省去，因为都是可enumerate对象：for t in enumerate(nltk.corpus.gutenberg.words('austen-emma.txt'))
emma2 = nltk.text.ConcordanceIndex(nltk.corpus.gutenberg.words('austen-emma.txt'))
emma2.print_concordance("However")
type(emma)
# <class 'nltk.text.Text'>
type(emma2)
# <class 'nltk.text.ConcordanceIndex'>

# 8.◑ Define a conditional frequency distribution over the Names corpus that 
# allows you to see which initial letters are more frequent for males vs. females (cf. 4.4).
names = nltk.corpus.names
# names.fileids()
# male_names = names.words('male.txt')
# female_names = names.words('female.txt')
cfd = nltk.ConditionalFreqDist(
        (fileid, name[0])
        for fileid in names.fileids()
          for name in names.words(fileid))
cfd.plot()

# 9.◑ Pick a pair of texts and study the differences between them, 
# in terms of vocabulary, vocabulary richness, genre, etc. 
# Can you find pairs of words which have quite different meanings across the two texts, 
# such as monstrous in Moby Dick and in Sense and Sensibility?
from nltk.book import *
# vocabulary
len(set(text1))
# 19317
len(set(text2))
# 6833
# vocabulary richness
len(set(text1)) / len(text1)
# 0.07406285585022564
len(set(text2)) / len(text2)
# 0.04826383002768831
# genre
text1.collocations()
text2.collocations()

stopwords = nltk.corpus.stopwords.words('english')
modals = ['can', 'could', 'may', 'might', 'must', 'will']
stopwords.extend(modals)

content1 = [w for w in text1 if w.lower() not in stopwords and w.isalnum()]
content2 = [w for w in text2 if w.lower() not in stopwords and w.isalnum()]
fdist1 = FreqDist(content1)
fdist2 = FreqDist(content2)
fdist1.most_common(50)
fdist2.most_common(50)
fdist1.plot(50)
fdist1.plot(50, cumulative=True)
fdist2.plot(50)
fdist2.plot(50, cumulative=True)

text1.concordance("monstrous")
text2.concordance("monstrous")
text1.similar("monstrous")
text2.similar("monstrous")
text1.common_contexts(["monstrous", "very"])
text2.common_contexts(["monstrous", "very"])
text1.dispersion_plot(["monstrous", "very"])
text2.dispersion_plot(["monstrous", "very"])

# 10.◑ Read the BBC News article: UK's Vicky Pollards 'left behind' 
# http://news.bbc.co.uk/1/hi/education/6173441.stm. 
# The article gives the following statistic about teen language: 
# "the top 20 words used, including yeah, no, but and like, account for around a third of all words." 
# How many word types account for a third of all word tokens, 
# for a variety of text sources? What do you conclude about this statistic? 
# Read more about this on LanguageLog, at http://itre.cis.upenn.edu/~myl/languagelog/archives/003993.html.



















































