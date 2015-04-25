#!/usr/bin/python
import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
import unittest

from src.Ring import Ring
from src.RingSection import RingSection
from src.Device import Device
import src.svg as svg
from lxml import etree


class TestRingSection(unittest.TestCase):
    def setUp(self):
        blankSVGpath = './blank.svg'
        svgTree = etree.parse(blankSVGpath)
        svgRoot = svgTree.getroot()
        self.svgFile = svg.SVG()
        self.svgFile.setSvg(svgRoot)

    def testNewSection(self):
        pass

    def testUpdateSvg(self):

        section = RingSection("name", "blue", 0, 90)
        section.updateSvg()

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()