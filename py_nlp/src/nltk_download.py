#!/usr/bin/python
# -*- coding: utf-8 -*-
import nltk
#安装语料库
# nltk.download()
#从nltk的book模块中加载所有的条目
from nltk.book import *
#选择文本
text1
text2
#搜索文本:查找词“monstrous”
text1.concordance("monstrous")
#关键词索引：查询文章中与monstrous运用相似的词（相似语法结构，上下文）
text1.similar("monstrous")
text2.similar("monstrous")
#研究共用两个或以上词汇的上下文
#自动检测出现在文本中的特定的词，并显示同一上下文中出现的其他词。
text2.common_contexts(["monstrous","very"])
#判断词在文本中的位置
text4.dispersion_plot(["citizens","democracy","freedom","duties","America"])
#产生一些随机文本,请安装nltk2.0.1版本，nltk3.x的版本是没了。有一个nltk.parse.generate生成相似句子
# text3.generate()
#获取长度:单词和标点符号，即标识符 "tokens."
len(text3)
#获取词汇表 items types包括 "word types."和标点符号
set(text3)
#排序
sorted(set(text3))
#计算单词数，词类型
len(set(text3))
#计算词汇丰富度 lexical richness of the text
#py2里先引入，确保是浮点除法
from __future__ import division
len(set(text3)) / len(text3)
#count particular words
text3.count("smote")
#compute what percentage of the text is taken up by a specific word
100 * text4.count('a') / len(text4)
#写成函数
def lexical_diversity(text):
    return len(set(text)) / len(text)

def percentage(count, total):
    return 100 * count / total

lexical_diversity(text3)
lexical_diversity(text5)
percentage(4, 5)
percentage(text4.count('a'), len(text4))

