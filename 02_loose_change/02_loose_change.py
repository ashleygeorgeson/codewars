#!/usr/bin/env python3

"""
Welcome young Jedi!
In this Kata you must create a function that takes an amount of US currency in #cents,
and returns a dictionary/hash which shows the least amount of coins used to make up that amount.
The only coin denominations considered in this exercise are: Pennies (1¢), Nickels (5¢), Dimes (10¢) and Quarters (25¢).
Therefore the dictionary returned should contain exactly 4 key/value pairs.
"""

# Imports 
#import os
import sys

def loose_change(cents):
    '''Takes an amount of currency in #cents, returns dictionary of least coins'''
    
    # Create empty dictionary
    change_dict = {
        'Nickels' : '',
        'Pennies' : '',
        'Dimes' : '',
        'Quarters': ''
        }
        
    # Account for negative integers or floats
    if cents < 0:
        cents = 0
    elif type(cents) == float:
        cents = int(cents)

    # Calculate number of quarters first (as largest), remove from pennies and add to change_dict
    quarters = cents // 25
    cents = cents - (quarters * 25)
    change_dict['Quarters'] = quarters
    # Calculate number of dimes next (as next largest), remove from pennies and add to change_dict
    dimes = cents // 10
    cents = cents - (dimes * 10)
    change_dict['Dimes'] = dimes
    # Calculate number of nickels next (as next largest), remove from pennies and add to change_dict
    nickels = cents // 5
    cents = cents - (nickels * 5)
    change_dict['Nickels'] = nickels
    # Then finally add the remaining #cents to change_dict as 'Pennies'
    change_dict['Pennies'] = cents
    return(change_dict)

def main():
    # Test Case 1 - expected {'Nickels': 0, 'Pennies': 4, 'Dimes': 0, 'Quarters': 1}"
    #cents = 29
    # Test Case 2 - expected {'Nickels': 1, 'Pennies': 1, 'Dimes': 1, 'Quarters': 3}"
    #cents = 91
    # Test Case 3 - expected {'Nickels': 0, 'Pennies': 0, 'Dimes': 0, 'Quarters': 0}"
    #cents = 0
    # Test Case 4 - expected {'Nickels': 0, 'Pennies': 0, 'Dimes': 0, 'Quarters': 0}"
    #cents = -2
    # Test Case 5 - expected {'Nickels': 0, 'Pennies': 3, 'Dimes': 0, 'Quarters': 0}" FAIL!!!
    cents = 3.9
    change_dict = loose_change(cents)
    print(change_dict)

# Check to see if this file is the "__main__" script being executed
if __name__ == '__main__':
    _, *script_args = sys.argv
    main(*script_args)