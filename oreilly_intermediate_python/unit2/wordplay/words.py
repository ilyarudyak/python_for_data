# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import scrabble

# print all words containing 'uu'
#==============================================================================
# for word in scrabble.wordlist:
#     if 'uu' in word:
#         print(word)
#==============================================================================
 
def count_appearance(double_letter):
    count = 0
    for word in scrabble.wordlist:
        if double_letter in word:
            count += 1
    return count
       
# what letters never appear doubled
#==============================================================================
# for letter in sorted(scrabble.scores.keys()):
#     double_letter = letter + letter
#     if (count_appearance(double_letter) == 0):
#         print(double_letter)
#==============================================================================
    
# words that contain all vowels 'aeiou'        
#==============================================================================
# def is_contain_vowels(word):
#     return set('aeiou').issubset(set(word))
#     
# for word in scrabble.wordlist:
#     if is_contain_vowels(word):
#         print(word)
#         break
#==============================================================================
    
# find longest palindrome
def is_palindrome(word):
    return word == word[::-1]

palindrome = ''
for word in scrabble.wordlist:
     if is_palindrome(word):
         if len(word) > len(palindrome):
             palindrome = word
print(palindrome + ':' + str(len(palindrome)))
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
