#! /usr/bin/env python3

"""
Your goal in this kata is to implement a difference function, which subtracts one list from another and returns the result.

It should remove all values from list a, which are present in list b.
"""

# Imports 
import os
import sys

'''
def array_dif(a,b):
    c = [] # New array to store the differences between arrays [a] and [b]
    for i in a:
        for j in b:
            if i is j: # Tested value from [a] is present in [b] - do not append to the new array
                print("VALUE PRESENT! " , i , "=" , j)
            else:
                print("NO MATCH! " , i , "!=" , j) # Tested value from [a] is not present in [b] - append to the new array
                c.append(i) 
    return(c)
'''

def array_dif2(a,b):
    for i in a:
        for j in b:
            try: a.remove(j)
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