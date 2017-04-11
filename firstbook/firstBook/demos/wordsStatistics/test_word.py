#coding:utf-8
import string

path = 'Walden.txt'

with open(path,'r') as f:
    words = [word.strip(string.punctuation).lower() for word in f.read().split()]
    words_index=set(words)
    word = {word:words.count(word) for word in words_index}

for word_get in sorted(word,key = lambda x: word[x],reverse= True):
    print ("{}--{} times".format(word_get,word[word_get]))