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

def decrypt(encrypted_text, n):
    """decrypt function
    For building the decrypted string:
    Opposite of the encrypt function
    Split the string in two
    find len of string, floor div = second half, floor div + mod = 1st half
    Take every 2nd char from the string, then the other chars, that are not every 2nd char, and concat them as new String.
    Do this n times!


    split original string into two halves, str1 and str2
    loop through the length of the longest string, and append str2,str1 char into a new string


    """
    #first_half_chars = len(encrypted_text)//2 + len(encrypted_text)%2 -1
    #second_half_chars = len(encrypted_text)//2 -1
    #str1,str2 = encrypted_text[7:15:1],encrypted_text[0:7:1]
    if encrypted_text == None or '': return(None)
    elif n <= 0: return(encrypted_text)
    else:
        for i in range(n):
            str1,str2 = encrypted_text[len(encrypted_text)//2:len(encrypted_text):1],encrypted_text[0:len(encrypted_text)//2:1]
            text=''
            for i in range(len(str1)):
                #print(i)
                if i+1 <= len(str2) != None: text = text + str1[i] + str2[i]
                else: text = text + str1[i]
            #print(encrypted_text[7:15:1] + encrypted_text[0:7:1])
        return(text)

def decrypt(text): # woks, only for n=1
    str3=''
    str1,str2 = text[len(text)//2:len(text):1],text[0:len(text)//2:1]
    for i in range(len(str1)):
            str3+=(str1[i]+str2[i])
    return(str3)

def decrypt(text, n):# works for n>1 but does not feel optimal
    for i in range(n):
        str3=''
        str1,str2 = text[len(text)//2:len(text):1],text[0:len(text)//2:1]
        for i in range(len(str1)):
                str3+=(str1[i]+str2[i])
                text=str3
    return(text)

def decrypt(text, n):# works for n>1, more optimal but still not great
    for i in range(n):
        str1,str2 = text[len(text)//2:len(text):1],text[0:len(text)//2:1]
        text=''
        for i in range(len(str1)):
                text+=(str1[i]+str2[i])
    return(text)

    '''
    #print("Decrypt:", args.decrypt, args.text, args.n)
    if encrypted_text == None or '': return(None)
    elif n <= 0: return(encrypted_text)
    else:
        for i in range(n):
            text = encrypted_text[1:len(encrypted_text):2] + encrypted_text[0:len(encrypted_text):2]
        return(text)
    '''

def encrypt(text, n):
    """encrypt function
    For building the encrypted string:
    Take every 2nd char from the string, then the other chars, that are not every 2nd char, and concat them as new String.
    Do this n times!
    """
    #print("Encrypt:", args.encrypt, args.text, args.n)
    if text == None or '': return(None)
    elif n <= 0: return(text)
    else:
        for i in range(n):
            text = text[1:len(text):2] + text[0:len(text):2]
        return(text)

# Module Functions and Classes
def main(args):
    """My main script function.

    Displays the full path to this script, and a list of the arguments passed to the script.
    """
    print(START_MESSAGE)
    print("Script Location:", location)
    print("Arguments Passed:", args)
    #print(solution(*args))
    if args.decrypt:
        print(decrypt(args.text, args.n))
    else:
        print(encrypt(args.text, args.n))

# Check to see if this file is the "__main__" script being executed
if __name__ == '__main__':
    _, *script_args = sys.argv
    parser = argparse.ArgumentParser()
    parser = argparse.ArgumentParser(description='Simple encryption, alternating split program')
    parser.add_argument('text', type=str, help="String to de/encrypt")
    parser.add_argument('n', type=int, help="Number of times to alternate split in crypto algorithm")
    group = parser.add_mutually_exclusive_group(required=True) # Mututally exclusive group
    group.add_argument("-d", "--decrypt", action="store_true",
                        help="Encrypt text")
    group.add_argument("-e", "--encrypt", action="store_true",
                        help="Decrypt text")
    args = parser.parse_args()
    #print(args.text, args.n, args.decrypt, args.encrypt)
    #main(args.text, args.n)
    #print(type(args))
    #print(type(*args))
    main(args)