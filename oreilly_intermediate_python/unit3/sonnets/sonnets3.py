#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Solutions for Unit 2 examples with comprehensions

@author: ilyarudyak
"""

import numpy as np

word_list = [elt.strip() for elt in open("sowpods.txt", "r").readlines()]
             
words_contain_uu = [word for word in word_list if 'UU' in word]
palindromes = [(word, len(word)) for word in word_list if word == word[::-1]]
p = np.array(palindromes, dtype=[('word', 'S10'), ('len', 'i4')])               

argmax_len = np.argmax(p['len'])
print(p[argmax_len])