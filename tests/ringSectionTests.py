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

    def testHasSubsections(self):
        section = RingSection("R-01", None, 0, 45)
        self.assertEqual(section.hasSubsections(), False)

        sectionWithSubsections = RingSection("R-02", None, 45, 90)
        sectionWithSubsections.addSubsection("R-02A", None, 30)
        self.assertEqual(sectionWithSubsections.hasSubsections(), True)

    def testGetSubsection(self):
        section = RingSection("R-00", None, 100, 60)
        subsection = section.addSubsection("R-00A", None, 100)
        self.assertEqual(section.getSubsection("R-00B"), None)
        self.assertEqual(section.getSubsection("R-00A"), section.subsections[0])
        self.assertEqual(subsection, section.getSubsection("R-00A"))

    def testComputeSubsectionStartAngle(self):
        section = RingSection("R1-01", None, 30, 40)
        self.assertEqual(section.computeSubsectionStartAngle(), 30)
        section.addSubsection("R1-01A", None, 15)
        self.assertEqual(section.computeSubsectionStartAngle(), 45)

    def tearDown(self):
        RingSection.id = 1

if __name__ == '__main__':
    unittest.main()