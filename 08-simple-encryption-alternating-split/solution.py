#!/usr/bin/env python

# Docstring
""" For building the encrypted string:
Take every 2nd char from the string, then the other chars, that are not every 2nd char, and concat them as new String.
Do this n times!.
"""

# imports
import os
import sys
import argparse
#from typing import final

# Module Constants
START_MESSAGE = "Simple Encryption #1 - Alternating Split"

# Module "Global" Variables
location = os.path.abspath(__file__)

def decrypt(text, n): # Fully working, but long and nasty
    """decrypt function
    Split the passed string into two substrings of equal length where string len is even, else substring1 length is 1 char longer
    find len of string, floor div = second half, floor div + mod = 1st half
    Take every 2nd char from the string, then the other chars, that are not every 2nd char, and concat them as new String.
    Do this n times!

    split original string into two halves, str1 and str2 which REVERSE the order of the original string substrings, i.e. 'abcdef' becomes 'def''abc'
    loop through the length of the longest string, and append str2,str1 char into a new string in pairs
    """
    if text == None or '': return(None) # Return None if no text or blank string passed to decrypt
    #elif n <= 0: return(encrypted_text) # Return encrypted text if no num iterations passed is < 1
    else: # Execute decryption routine
        for i in range(n): # Loop through num of decrypt iterations
            str1,str2 = text[len(text)//2:len(text):1],text[0:len(text)//2:1] # Split encrypted text into two substrings, REVERSED
            text='' # Reset text string to '' in order to append new decrypted string and use fr further decrypiton iterations
            for i in range(len(str1)): # Loop through each character in each substring, using str1 which should be largest where string length is odd
                    if i+1 <= len(str2) != None: text += (str1[i] + str2[i]) # Where string length is not odd, add the loop element of each subsring to the decrypted string 
                    else: text+=str1[i] # Where the string length is odd, only add the loop element of the first substring to the decrypted string
        return(text) # Return the decrypted string

def encrypt(text, n):
    """encrypt function
    For building the encrypted string:
    Take every 2nd char from the string, then the other chars, that are not every 2nd char, and concat them as new String.
    Do this n times!
    """
    if text == None or '': return(None)
    else:
        for i in range(n):
            text = text[1:len(text):2] + text[0:len(text):2]
        return(text)

# Module Functions and Classes
def main(args):
    """My main script function.

    Displays the full path to this script, and a list of the arguments passed to the script.
    """
    print("="*64)
    print(START_MESSAGE)
    print("Script Location:", location)
    print("Arguments Passed:", args)
    print("="*64)
    if args.decrypt:
        print("Mode: Decrypt", args.encrypt, "Input phrase:", args.text, "Cipher complexity:", args.n)
        print(" -> Output phrase:", decrypt(args.text, args.n))
    else:
        #print("Decrypt:", args.encrypt, "Input phrase:", args.text, "Cipher complexity:", args.n)
        print(" -> Mode: Encrypt", "Input phrase:", args.text, "Cipher complexity:", args.n)
        print(" -> Output phrase:", encrypt(args.text, args.n))

# Check to see if this file is the "__main__" script being executed
if __name__ == '__main__':
    _, *script_args = sys.argv
    parser = argparse.ArgumentParser()
    parser = argparse.ArgumentParser(description='Simple encryption, alternating split program')
    parser.add_argument('text', type=str, help="String to de/encrypt")
    parser.add_argument('n', type=int, help="Cipher complexity: Number of times to alternate split in crypto algorithm")
    group = parser.add_mutually_exclusive_group(required=True) # Mututally exclusive group
    group.add_argument("-d", "--decrypt", action="store_true",
                        help="Encrypt text")
    group.add_argument("-e", "--encrypt", action="store_true",
                        help="Decrypt text")
    args = parser.parse_args()
    main(args)