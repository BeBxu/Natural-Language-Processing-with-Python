#!/usr/bin/python
# -*- coding: utf-8 -*-

#1.Try using the Python interpreter as a calculator, and typing expressions like 12 / (4 + 1).
print 12 / (4 + 1)
#2.Given an alphabet of 26 letters, there are 26 to the power 10, or 26 ** 10, ten-letter strings we can form. That works out to  141167095653376. How many hundred-letter strings are possible?
# 26**100=3142930641582938830174357788501626427282669988762475256374173175398995908420104023465432599069702289330964075081611719197835869803511992549376L

#3.The Python multiplication operation can be applied to lists. What happens when you type ['Monty', 'Python'] * 20, or 3 * sent1?
#['Monty', 'Python', 'Monty', 'Python', 'Monty', 'Python', 'Monty', 'Python', 'Monty', 'Python', 'Monty', 'Python', 'Monty', 'Python', 'Monty', 'Python', 'Monty', 'Python', 'Monty', 'Python', 'Monty', 'Python', 'Monty', 'Python', 'Monty', 'Python', 'Monty', 'Python', 'Monty', 'Python', 'Monty', 'Python', 'Monty', 'Python', 'Monty', 'Python', 'Monty', 'Python', 'Monty', 'Python']
#['Call', 'me', 'Ishmael', '.', 'Call', 'me', 'Ishmael', '.', 'Call', 'me', 'Ishmael', '.']

#4.Review 1 on computing with language. How many words are there in text2? How many distinct words are there?
from nltk.book import *
len(text2) #tokens
len(set(text2)) #set length of tokens, word types

#5.Compare the lexical diversity scores for humor and romance fiction in 1.1. Which genre is more lexically diverse?
#Genre    Tokens    Types    Lexical diversity
#humor    21695    5017    0.231
#fiction: romance    70022    8452    0.121

#6. Produce a dispersion plot of the four main protagonists in Sense and Sensibility: Elinor, Marianne, Edward, and Willoughby. What can you observe about the different roles played by the males and females in this novel? Can you identify the couples?
text2.dispersion_plot(["Elinor", "Marianne", "Edward", "Willoughby"])

#7.Find the collocations in text5
text5.collocations()

#8.Consider the following Python expression: len(set(text4)). State the purpose of this expression. Describe the two steps involved in performing this computation.
#Ans: count the length of distinct words and punctuation symbols in text4. 1.get the unique items types 2. calculate its number.

#9.Define a string and assign it to a variable, e.g., my_string = 'My String' (but put something more interesting in the string). Print the contents of this variable in two ways, first by simply typing the variable name and pressing enter, then by using the print statement.
my_string = 'My String'
my_string
print my_string
#Try adding the string to itself using my_string + my_string, or multiplying it by a number, e.g., my_string * 3. Notice that the strings are joined together without any spaces. How could you fix this?
my_string+my_string
my_string*3
my_string+' '+my_string
((my_string+' ')*3).strip()
((my_string+' ')*3)[:-1]

#10.Define a variable my_sent to be a list of words, using the syntax my_sent = ["My", "sent"] (but with your own words, or a favorite saying).
my_sent = ["My", "sent"]
#Use ' '.join(my_sent) to convert this into a string.
' '.join(my_sent)
#Use split() to split the string back into the list form you had to start with.
' '.join(my_sent).split()
' '.join(my_sent).split(' ')

#11.Define several variables containing lists of words, e.g., phrase1, phrase2, and so on. Join them together in various combinations (using the plus operator) to form whole sentences. What is the relationship between len(phrase1 + phrase2) and len(phrase1) + len(phrase2)?
phrase1 = ["My", "sent","asfsdag","adfshafhwert"]
phrase2 = ["asfsdag","adfshafhwert"]
phrase1+phrase2 #['My', 'sent', 'asfsdag', 'adfshafhwert', 'asfsdag', 'adfshafhwert']
len(phrase1+phrase2) #6
len(phrase1)+len(phrase2) #6

#12.  Consider the following two expressions, which have the same value. Which one will typically be more relevant in NLP? Why?
"Monty Python"[6:12]
["Monty", "Python"][1]

#13. We have seen how to represent a sentence as a list of words, where each word is a sequence of characters. What does sent1[2][2] do? Why? Experiment with other index values.
sent1[2][2]
#'h' pick the third character of the third word from sent1.

#14.The first sentence of text3 is provided to you in the variable sent3. The index of the in sent3 is 1, because sent3[1] gives us 'the'. What are the indexes of the two other occurrences of this word in sent3?
sent3[1]
sent3.count('the') #3
sent3.index('the') #1
def find_all_index(arr,item):
    return [i for i,a in enumerate(arr) if a==item]
find_all_index(sent3,'the') # [1, 5, 8]

#index方法找不到会抛异常，find方法仅用于查找字符串，并且不会抛异常，找不到直接返回-1
def use_index(sent3, the='the'):
    try:
        res = sent3.index(the)
    #     res = sent3.index('theafhafh')
    except Exception as e:
#         print e
#         print type(e)
#         print "异常"
        res = -1
#     else:
#         print "没有异常要执行我"
    finally:
#         print "最后总是要执行我"
        return res

index_start = -1 
res = use_index(sent3)
while res!=-1:
    if (index_start==-1):
        index_start = res+1        
    else: 
        print index_start-1
        index_start += res+1
    res = use_index(sent3[index_start:])
    
if index_start==-1:
    print "zhao bu dao"
else:
    print index_start-1
    
#15.Review the discussion of conditionals in 4. Find all words in the Chat Corpus (text5) starting with the letter b. Show them in alphabetical order.
sorted(w for w in set(text5) if w.startswith('b'))

#16.Type the expression list(range(10)) at the interpreter prompt. Now try list(range(10, 20)), list(range(10, 20, 2)), and list(range(20, 10, -2)). We will see a variety of uses for this built-in function in later chapters.
list(range(10))
list(range(10, 20))
#注意步长及顺序，类比 extended slice
list(range(10, 20, 2))
list(range(20, 10, -2))

#17.Use text9.index() to find the index of the word sunset. You'll need to insert this word as an argument between the parentheses. By a process of trial and error, find the slice for the complete sentence that contains this word.
text9.index('sunset') #629
text9[629] #sunset
#slicing均排除了index为629的那个“sunset”
629 + 1 + text9[629+1:].index('.') # 629 + 1 + 13 = 643 text9[643]

#（0）list comprehension链表推导构造所有sunset之前“.”对应的index号，访问最后一个
[key for key,v in enumerate(text9[:629]) if v=='.'][-1] #612
#（1）从“sunset”前一个单词开始，往前找
#但是text9[629-1::-1]不支持extended slice，无法直接reverse, 先转换成list
629 - (1 + (text9[:])[629-1::-1].index('.')) # 629-(1+16) = 612 text9[612]
#（2）或者先截取text9[:629]自动返回一个list,再翻转
629 - (1 + text9[:629][::-1].index('.'))  #612
#（3）reversed()方法, 注：reversed()和sorted()类似(返回类型不同,一个迭代器，一个是List)，注意区分reverse()和sort()用法(两个函数的返回值都是None（其实是无返回值）)
629 - (1 + [w for w in reversed(text9[:629])].index('.')) #612
#（4）使用sorted(),自定义cmp函数返回为-1，表示无论什么都按原顺序翻转，此时设置参数reverse会失效。
629 - (1 + sorted(text9[:629],cmp=lambda x,y:-1, key=None, reverse=True).index('.')) #612
#（5）在python3.x中取消了cmp参数，也不支持直接往sort()里面传函数了。可以构造排序函数传递给key来实现。
#key自带一些方便的Operator 模块函数，比如key=itemgetter(1,2)，key=attrgetter('grade', 'age')
#key只允许传递一个参数，def 函数名(e)，e为将要被sorted的迭代对象中的元素，按续依次传入，根据返回值排序，并映射为原始元素
#这里是想用sorted将list按照index反序，key值无法获得index号，所以先用enumerate变成（index，item）pairs，再取反序的index=-e[0]
629 - (1 + [w[1] for w in sorted(enumerate(text9[:629]),key=lambda e: -e[0])].index('.')) #612
#（6）类似的思路，更直观的是用zip的方法给迭代对象加上索引，zip()函数可以把两个 list 变成一个 list，先构造对应index的一个range(629)
629 - (1 + [w[1] for w in sorted(zip(list(range(629)),text9[:629]),key=lambda e: -e[0])].index('.')) #612
#（6）拓展开来，可以用倒序打标记，顺序输出访问
#这些都为DSU（Decorate-Sort-Undecorate）排序方法，原因为排序的过程需要下列三步：
# 第一：对原始的list进行装饰，使得新list的值可以用来控制排序；
# 第二：对装饰后的list排序；
# 第三：将装饰删除，将排序后的装饰list重新构建为原来类型的list；

#（7）另一种python3的方法，将以前写的cmp函数转化成等效的key函数，在from functools import cmp_to_key里
# 根据传入list元素个数初始化相应个数的class K.obj实例 
# 若自己实现的话，只重载__lt__就行了，根据print测试代码，这里也只调用了此函数
# 这些双下划线函数是种钩子机制，the special method hooks are invoked
# So the list [1, 2, 3] is sorted as [K (1), K (2), K (3)], and if, say, K (1) is lower, then K (1) .__ lt __ (K (2)) is called, which is translated to mycmp (1, 2) <0.
# 原理是互相比较不同元素对应的K.obj实例，根据mycmp函数返回值和<0比较的boolean值判断是否less than
# 所以只需要控制mycmp函数的返回值，实现等效于以前cmp返回值的函数即可。
# 即根据mycmp的返回值排序，保证-1,0,1设置正确
# 关于这些K.obj实例互相比较的顺序应该和底层红黑树实现有关。
def cmp_to_key(mycmp):
    'Convert a cmp= function into a key= function'
    class K(object):
        def __init__(self, obj, *args):
#             print('obj created with ',obj)
            self.obj = obj
        def __lt__(self, other):
#             print('comparing less than ',self.obj)
#             print('comparing other ',other.obj)
            res = mycmp(self.obj, other.obj) < 0
#             print (res)
            return res
        def __gt__(self, other):
            print('comparing greter than ',self.obj)
            return mycmp(self.obj, other.obj) > 0
        def __eq__(self, other):
            print('comparing equal to ',self.obj)
            return mycmp(self.obj, other.obj) == 0
        def __le__(self, other):
            print('comparing less than equal ',self.obj)
            return mycmp(self.obj, other.obj) <= 0
        def __ge__(self, other):
            print('comparing greater than equal',self.obj)
            return mycmp(self.obj, other.obj) >= 0
        def __ne__(self, other):
            print('comparing not equal ',self.obj)
            return mycmp(self.obj, other.obj) != 0
    return K

def mycmp2(a, b):
    print("In Mycmp for", a, ' ', b)
    if a < b:
        return -1
    elif a > b:
        return 1
    return 0
# print(sorted([5,3,546,23,46,45,123,346,567,5464],key=cmp_to_key(mycmp2),reverse=False))

#重写sorted(text9[:629],cmp=lambda x,y:-1)中的lambda x,y:-1
629 - (1 + sorted(text9[:629],key=cmp_to_key(lambda x,y:-1)).index('.')) #612

#rindex方法仅仅支持字符串，不支持list
# text9[:629].rindex('.')

#Text[:]转换list; Text(list)转换为Text类型
from nltk.text import Text
import nltk.corpus
moby = Text(nltk.corpus.gutenberg.words('text.txt'))
type(moby)

#输出
' '.join(text9[612+1:643+1])

#18. ◑ Using list addition, and the set and sorted operations, compute the vocabulary of the sentences sent1 ... sent8.
# 循环读取sent1-sent8的变量值
para_dict = locals()
for i in range(1,9):
#     print para_dict['sent%d' % i]
    vocabulary = sorted(set(para_dict['sent%d' % i]))
    vocabulary_size = len(vocabulary)
    print vocabulary
    print vocabulary_size

#19. What is the difference between the following two lines? Which one will give a larger value? Will this be the case for other texts?
# >>> sorted(set(w.lower() for w in text1))    17231 小：先text1的词都取小写再去重复
# >>> sorted(w.lower() for w in set(text1))    19317 大：先去text1的重复，再取小写
# e.g. “A book and a pencil”和“a book and a pencil”里面的A和a的处理将不一样。

#20. What is the difference between the following two tests: w.isupper() and not w.islower()?
# w.islower()    test if w contains cased characters and all are lowercase
# w.isupper()    test if w contains cased characters and all are uppercase

#21. Write the slice expression that extracts the last two words of text2.
text2[-2:]

#22. Find all the four-letter words in the Chat Corpus (text5). 
#    With the help of a frequency distribution (FreqDist), show these words in decreasing order of frequency.
# s.isalpha()    test if s is non-empty and all characters in s are alphabetic
# s.isalnum()    test if s is non-empty and all characters in s are alphanumeric
# s.isdigit()    test if s is non-empty and all characters in s are digits
# s.istitle()    test if s contains cased characters and is titlecased (i.e. all words in s have initial capitals)
sorted([w for w in set(text5) if len(w)==4 and w.isalpha()])
# fdist = FreqDist(samples)    create a frequency distribution containing the given samples
# fdist[sample] += 1    increment the count for this sample
# fdist['monstrous']    count of the number of times a given sample occurred
# fdist.freq('monstrous')    frequency of a given sample
# fdist.N()    total number of samples
# fdist.most_common(n)    the n most common samples and their frequencies
# for sample in fdist:    iterate over the samples
# fdist.max()    sample with the greatest count
# fdist.tabulate()    tabulate the frequency distribution
# fdist.plot()    graphical plot of the frequency distribution
# fdist.plot(cumulative=True)    cumulative plot of the frequency distribution
# fdist1 |= fdist2    update fdist1 with counts from fdist2
# fdist1 < fdist2    test if samples in fdist1 occur less frequently than in fdist2
fdist = FreqDist([w for w in text5 if len(w)==4 and w.isalpha()])
fdist.plot()
fdist.plot(cumulative=True)

#23. Review the discussion of looping with conditions in 4. Use a combination of for and if statements to 
# loop over the words of the movie script for Monty Python and the Holy Grail (text6) and print all the uppercase words, one per line.
for w in text6: 
    if w.isupper():
        print w
        
w_upper = [w for w in text6 if w.isupper()]
for u in w_upper:
    print u

# 24. Write expressions for finding all words in text6 that meet the conditions listed below.
#  The result should be in the form of a list of words: ['word1', 'word2', ...].
# Ending in ize
# Containing the letter z
# Containing the sequence of letters pt
# Having all lowercase letters except for an initial capital (i.e., titlecase)
# s.startswith(t)    test if s starts with t
# s.endswith(t)    test if s ends with t
# t in s    test if t is a substring of s
all_words = [w for w in set(text6) if w.isalpha()]
a = [s for s in all_words if s.endswith("ize")]
b = [s for s in all_words if ('z' in s)]
c = [s for s in all_words if ("pt" in s)]
d = [s for s in all_words if (s.islower() or s.istitle())]

# 25.  Define sent to be the list of words ['she', 'sells', 'sea', 'shells', 'by', 'the', 'sea', 'shore']. 
# Now write code to perform the following tasks:
# Print all words beginning with sh
# Print all words longer than four characters
sent = ['she', 'sells', 'sea', 'shells', 'by', 'the', 'sea', 'shore']
[w for w in sent if w.startswith('sh')]
[w for w in sent if len(w)>4]

# 26. What does the following Python code do?
#   sum(len(w) for w in text1) 
# Can you use it to work out the average word length of a text?
# 计算text1的总字符数
from __future__ import division
avg = sum(len(w) for w in text1) / len(text1) # 3.830411128023649

#27. Define a function called vocab_size(text) that has a single parameter for the text, and which returns the vocabulary size of the text.
def vocab_size(text):
    return len(set(text))

#28. Define a function percent(word, text) that calculates how often a given word occurs in a text, 
# and expresses the result as a percentage.
def percent(word, text):    
    return repr(100 * text.count(word) / len(text))+'%'

#29. We have been using sets to store vocabularies.
#  Try the following Python expression: set(sent3) < set(text1). 
# Experiment with this using different arguments to set(). 
# What does it do? Can you think of a practical application for this?
#sets不记录元素位置或者插入点。因此，sets不支持 indexing, slicing, 或其它类序列（sequence-like）的操作。  
# a = t | s          # t 和 s的并集  
# b = t & s          # t 和 s的交集  
# c = t – s          # 求差集（项在t中，但不在s中）  
# d = t ^ s          # 对称差集（项在t或s中，但不会同时出现在二者中）  
# 布尔值，做条件判断用。











