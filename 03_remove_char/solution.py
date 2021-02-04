#! /usr/bin/env python3

"""
It's pretty straightforward. Your goal is to create a function that removes the first and last characters of a string.
You're given one parameter, the original string. You don't have to worry with strings with less than two characters.
"""

# Imports 
import os
import sys

def remove_char(s):
    ''' Function removes first and last characters from string.'''
    return(s[1:len(s)-1])

def main():
    string = '123456789'
    # Test Case 1 Values - "a was [1,2], b was [1], expected [2]"
    #a = [1,2]
    #b = [1] 
    # Test Case 2 Values - "a was [1,2,2], b was [1], expected [2,2]"
    #a = [1,2,2]
    #b = [1]
    # Test Case 3 Values - "a was [1,2,2], b was [2], expected [1]"
    #a = [1,2,2]
    #b = [2] 
    # Test Case 4 Values - "a was [1,2,2], b was [], expected [1,2,2]"
    #a = [1,2,2]
    #b = [] 
    # Test Case 5 Values - "a was [], b was [1,2], expected []"
    #a = []
    #b = [1,2] 
    print("INITAL STRING:" , string)
    string = remove_char(string)
    print("FINAL STRING:" , string)


# Check to see if this file is the "__main__" script being executed
if __name__ == '__main__':
    _, *script_args = sys.argv
    main(*script_args)    