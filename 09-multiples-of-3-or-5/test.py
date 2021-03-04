#!/usr/bin/env python

# imports
import os
import sys
from solution import solution

# Module "Global" Variables
location = os.path.abspath(__file__)
here = os.path.abspath(os.path.dirname(__file__)) # Get the absolute path for the directory where this file is located "here"
project_root = os.path.abspath(os.path.join(here, "..")) # Get the absolute path for the project / repository root
sys.path.insert(0, project_root)# Extend the system path to include the project root and import the test module

# relative imports
import codewars_test as test

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it("should handle basic cases")
    def basic_tests():
        test.assert_equals(solution(10), 23)