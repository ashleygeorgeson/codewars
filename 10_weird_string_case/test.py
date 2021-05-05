#!/usr/bin/env python

# imports
import os
import sys
from solution import to_weird_case

# Module "Global" Variables
location = os.path.abspath(__file__)
here = os.path.abspath(os.path.dirname(__file__)) # Get the absolute path for the directory where this file is located "here"
project_root = os.path.abspath(os.path.join(here, "..")) # Get the absolute path for the project / repository root
sys.path.insert(0, project_root)# Extend the system path to include the project root and import the test module

# relative imports
import codewars_test as test

test.describe('to_weird_case')

test.it('should return the correct value for a single word')
test.assert_equals(to_weird_case('This'), 'ThIs')
test.assert_equals(to_weird_case('is'), 'Is')

test.it('should return the correct value for multiple words')
test.assert_equals(to_weird_case('This is a test'), 'ThIs Is A TeSt')
