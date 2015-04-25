#!/usr/bin/python
import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
import unittest

from src.Ring import Ring
from src.RingSection import RingSection
from src.ArcDrawingTools import ArcDrawingTools
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
        RingSection.id = 1

    def testNewSection(self):
        section = RingSection("R1-01", "green", 15, 35)
        self.assertEqual(section.longName, "R1-01")
        self.assertEqual(section.shortName, "ringSection1")
        self.assertEqual(section.startAngle, 15)
        self.assertEqual(section.endAngle, 50)

    def testIsInUpperHalf(self):
        upperSection = RingSection("InUpper", None, -30, 180)
        lowerSection = RingSection("InLower", None, 100, 120)
        self.assertEqual(upperSection.isInUpperHalf(), True)
        self.assertEqual(lowerSection.isInUpperHalf(), False)

    def testDrawZoom1Section(self):
        section = RingSection("name", "blue", 0, 90)
        section.drawSectionOnZoom1(ArcDrawingTools.describePathForTextAnticlockwise)
        node = self.svgFile.getZoom1Background()
        sectionNode = self.svgFile.getElementById("ringSection1colourfulCircle", node)
        self.assertEqual(sectionNode.attrib["d"], "M 14794.4893 4827.0225 A 2805.4143 2805.4143 0 0 0 11989.075 "
                                                  "2021.6082L 11989.075 4827.0225 L 14794.4893 4827.0225 Z")
        self.assertEqual(sectionNode.attrib["fill"], "blue")

    def testDrawBigCaption(self):
        section = RingSection("R2-01", "yellow", 100,45)
        section.drawSectionOnZoom1(ArcDrawingTools.describePathForTextAnticlockwise)
        zoomNode = self.svgFile.getZoom1Background()
        textNode = self.svgFile.getElementById("ringSection1bigCaption", zoomNode)
        self.assertEqual(textNode.attrib["style"], "font-size:200px;font-style:normal;")

    def tearDown(self):
        RingSection.id = 1

if __name__ == '__main__':
    unittest.main()