#!/usr/bin/python
import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
import unittest
from src.RingSubsection import RingSubsection

class TestRingSubsection(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()