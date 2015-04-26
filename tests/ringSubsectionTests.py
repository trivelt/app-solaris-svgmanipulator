#!/usr/bin/python
import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
import unittest
from src.RingSubsection import RingSubsection

class TestRingSubsection(unittest.TestCase):
    def setUp(self):
        RingSubsection.id = 1

    def testNewSubsection(self):
        subsecton = RingSubsection("R1-01A", None, 0, 5)
        secondSubsecton = RingSubsection("R1-01B", None, 5, 10)
        self.assertEqual(subsecton.id, 1)
        self.assertEqual(secondSubsecton.id, 2)
        self.assertEqual(subsecton.shortName, "ringSubsection1")
        self.assertEqual(subsecton.longName, "R1-01A")

    def tearDown(self):
        RingSubsection.id = 1

if __name__ == '__main__':
    unittest.main()