#!/usr/bin/python
# -*- coding: utf-8 -*-

# sent3 = ['the', 'the', 'beginning', 'God', 'created', 'the', 'heaven', 'and', 'the', 'earth', '.']
# res = ''
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
    
# index_start = -1 
# res = use_index(sent3)
# while res!=-1:
#     if (index_start==-1):
#         index_start = res+1        
#     else: 
#         print index_start-1
#         index_start += res+1
#     res = use_index(sent3[index_start:])
#     
# if index_start==-1:
#     print "zhao bu dao"
# else:
#     print index_start-1
#     
# def use_find(sent3, the='the'):
#     return sent3.find(the)
# index_start = -1 
# res = use_find(sent3)
# while res!=-1:
#     if (index_start==-1):
#         index_start = res+1        
#     else: 
#         print index_start-1
#         index_start += res+1
#     res = use_find(sent3[index_start:])
#      
# if index_start==-1:
#     print "zhao bu dao"
# else:
#     print index_start-1
# import time
# 
# time_end = '2017-12-26'
# tsmp = time.mktime(time.strptime(time_end, '%Y-%m-%d'))
# print type(tsmp)
# tsmp = int(tsmp)
# print type(tsmp)
# tsmp = repr(tsmp)
# print type(tsmp)
# print tsmp
# from nltk.book import *
# para_dict = locals()
# for i in range(1,9):
#     print para_dict['sent%d' % i]

from nltk.corpus import nps_chat
chatroom = nps_chat.posts('10-19-20s_706posts.xml')  # @UndefinedVariable
print chatroom[123]


