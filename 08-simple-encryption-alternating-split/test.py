#!/usr/bin/env python

# imports
import os
import sys
from solution import encrypt, decrypt

# Module "Global" Variables
location = os.path.abspath(__file__)
here = os.path.abspath(os.path.dirname(__file__)) # Get the absolute path for the directory where this file is located "here"
project_root = os.path.abspath(os.path.join(here, "..")) # Get the absolute path for the project / repository root
sys.path.insert(0, project_root)# Extend the system path to include the project root and import the test module

# relative imports
import codewars_test as test

test.describe('Basic Tests')
test.assert_equals(encrypt("This is a test!", 0), "This is a test!")
test.assert_equals(encrypt("This is a test!", 1), "hsi  etTi sats!")
test.assert_equals(encrypt("This is a test!", 2), "s eT ashi tist!")
test.assert_equals(encrypt("This is a test!", 3), " Tah itse sits!")
test.assert_equals(encrypt("This is a test!", 4), "This is a test!")
test.assert_equals(encrypt("This is a test!", -1), "This is a test!")
test.assert_equals(encrypt("This kata is very interesting!", 1), "hskt svr neetn!Ti aai eyitrsig")

test.assert_equals(decrypt("This is a test!", 0), "This is a test!")
test.assert_equals(decrypt("hsi  etTi sats!", 1), "This is a test!")
test.assert_equals(decrypt("s eT ashi tist!", 2), "This is a test!")
test.assert_equals(decrypt(" Tah itse sits!", 3), "This is a test!")
test.assert_equals(decrypt("This is a test!", 4), "This is a test!")
test.assert_equals(decrypt("This is a test!", -1), "This is a test!")
test.assert_equals(decrypt("hskt svr neetn!Ti aai eyitrsig", 1), "This kata is very interesting!")

test.assert_equals(encrypt("", 0), "")
test.assert_equals(decrypt("", 0), "")
test.assert_equals(encrypt(None, 0), None)
test.assert_equals(decrypt(None, 0), None)
