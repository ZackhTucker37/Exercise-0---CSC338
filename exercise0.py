"""
Name: Zackh Tucker
Date: 1.24.18
Class: CSC 338
Exercise 0, python review program. Writing as per instructions on paper. 
"""

import sys
import string

def readFile(fname):
    foo = open(fname, 'r')
    fileText = foo.read()
    foo.close()
    fileText = fileText.lower()
    for char in string.punctuation:
        fileText = fileText.replace(char, "")
    return fileText

def countWords(text):
    my_dick = {}
    for word in text:
        if word not in my_dick:
            my_dick[word] = 1
        else:
            my_dick[word] += 1
    return my_dick

def countChars(text):
    my_dick = {}
    for char in text:
        if char not in my_dick:
            my_dick[char] = 1
        else:
            my_dick[char] += 1
    return my_dick

def showCounts(dict):
    for key in dict: 
    	if key == '\n':
    		continue
    	elif key == ' ':
    		continue
    	else:
    		print (key, dict[key])

def main():
    foo1 = readFile(sys.argv[1])
    word_list = foo1.split()
    word_count = countWords(word_list)
    chars_dict = countChars(foo1)
    showCounts(chars_dict)
    print('\n')
    showCounts(word_count)

main()