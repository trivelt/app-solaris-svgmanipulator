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
        self.colour = "green"
        self.name = "xyz"
        self.coord = 129
        self.width = 108.1
        LinacSubsection.id = 1

        self.blankSVGpath = './blank.svg'
        svgTree = etree.parse(self.blankSVGpath)
        svgRoot = svgTree.getroot()
        self.svgFile = svg.SVG()
        self.svgFile.setSvg(svgRoot)

    def testSubsectionCreate(self):
        subsection = LinacSubsection(self.name, self.colour, self.coord, self.width)
        self.assertEqual(subsection.longName, self.name)
        self.assertEqual(subsection.startCoordinate, self.coord)
        self.assertEqual(subsection.width, self.width)
        self.assertEqual(subsection.id, 1)

        secondSubsection = LinacSubsection("Name", None, None, None)
        self.assertEqual(secondSubsection.id, 2)

    def testDrawRectangle(self):
        subsection = LinacSubsection(self.name, self.colour, self.coord, self.width)
        subsection.updateSvg()
        zoomNode = self.svgFile.getZoom2Background()
        rectangle = self.svgFile.getElementById("linacSubsection1Rect", zoomNode)

        self.assertEqual(rectangle.attrib["width"], str(self.width))
        self.assertEqual(rectangle.attrib["style"], "fill:green;fill-opacity:0.49803922;stroke:none;display:inline")

    def testDrawText(self):
        subsection = LinacSubsection(self.name, self.colour, self.coord, self.width)
        subsection.updateSvg()
        zoomNode = self.svgFile.getZoom2Background()
        textElementNode = self.svgFile.getElementById("linacSubsection1SmallCaption", zoomNode)
        textElement = self.svgFile.getElementById("linacSubsection1SmallCaptionTextPath", textElementNode)

        self.assertEqual(textElement.text, self.name)


    def tearDown(self):
        LinacSubsection.id = 1

if __name__ == '__main__':
    unittest.main()