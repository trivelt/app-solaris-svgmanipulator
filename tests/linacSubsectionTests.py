#!/usr/bin/python
import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
import unittest

from src.LinacSection import LinacSection
from src.LinacSubsection import LinacSubsection
from src.Device import Device
import src.svg as svg
from lxml import etree

class TestLinacSubsection(unittest.TestCase):
    def setUp(self):
        self.colour = "red"
        self.name = "abcd-12"
        self.coord = 150.123
        self.width = 199.33
        self.blankSVGpath = './blank.svg'
        LinacSection.id = 1

    def testSectionCreate(self):
        section = LinacSection(self.name, self.colour, self.coord, self.width)
        self.assertEqual(section.longName, self.name)

    def tearDown(self):
        LinacSection.id = 1

if __name__ == '__main__':
    unittest.main()