#!/usr/bin/python3
#coding:utf-8
import string

path = 'Walden.txt'


# with open(path,encoding='utf-8',mode='r') as f:
#     # print(i for i in f.readline())
#     words = f.read().split()
#     cou_words = set(words)
#     w = {}
#     # print (words)
#     for word in cou_words:
#         w[word]=words.count(word)
#         # print (f.read())
#         pass
#     print (w)

with open(path,'r') as f:
    # words = f.read().split()
    # print(words)
    # for word in words:
    #     print('{}-{} times'.format(word,words.count(word)))
    #
    words = [raw_word.strip(string.punctuation).lower() for raw_word in f.read().split()]
    words_index = set(words)
    counts_dict = {index:words.count(index) for index in words_index}

# a = lambda x: counts_dict[x]
# print(a())
for word in sorted(counts_dict, key = lambda x: counts_dict[x], reverse=True):
    print('{}--{} times'.format(word,counts_dict[word]))


