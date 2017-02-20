#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 01:15:30 2016

@author: ilyarudyak
"""

import time

my_words = [elt.strip() for elt in open("sonnet_words.txt", "r").readlines()]
word_list = [elt.strip() for elt in open("sowpods.txt", "r").readlines()]
word_set = set(word_list)            

counter = 0

start = time.time()

for word in my_words:
    
    # instead of word_list
    # we don't need to call keys()
    if word not in word_set:           
        print(word)
        counter += 1

stop = time.time()        

print("Total new words: %d" % counter)
print("Total time: %.1f" % (stop - start))
