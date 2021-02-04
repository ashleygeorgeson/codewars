#! /usr/bin/env python3

"""
Your goal in this kata is to implement a difference function, which subtracts one list from another and returns the result.

It should remove all values from list a, which are present in list b.
"""

# Imports 
import os
import sys

def array_dif2(a,b):
    ''' Function checks whether each element of [b] is in [a]. If it exists, the value is removed from [a].'''
    for i in a:
        for j in b:
            try: a.remove(j) # Need to catch value error exception in case a value is not present to remove (list.remove(value) errors if value is not present) 
            except: continue
    return(a)

def main():
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
    a = []
    b = [1,2] 
    c = array_dif2(a,b)
    print("FINAL ARRAY DIFFERENCE:" , c)


# Check to see if this file is the "__main__" script being executed
if __name__ == '__main__':
    _, *script_args = sys.argv
    main(*script_args)


    