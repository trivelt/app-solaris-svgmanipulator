#!/usr/bin/python
import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
import unittest

from src.LinacSection import LinacSection
from src.Device import Device
import src.svg as svg
from lxml import etree

class TestSectionBase(unittest.TestCase):
    def setUp(self):
        self.colour = "red"
        self.name = "abcd-12"
        self.coord = 150.123
        self.width = 199.33
        self.blankSVGpath = './blank.svg'

    def testSectionCreate(self):
        section = LinacSection(self.name, self.colour, self.coord, self.width)
        self.assertEqual(section.longName, self.name)
        self.assertEqual(section.width, self.width)
        self.assertEqual(section.startCoordinate, self.coord)
        self.assertEqual(section.colour, self.colour)
        self.assertEqual(section.shortName, "section1")

        secondSection = LinacSection("bb", self.colour, self.coord)
        self.assertEqual(secondSection.longName, "bb")
        self.assertEqual(secondSection.shortName, "section2")

    def testUpdateZoom1(self):
        svgTree = etree.parse(self.blankSVGpath)
        svgRoot = svgTree.getroot()
        svgFile = svg.SVG()
        svgFile.setSvg(svgRoot)

        zoom1 = svgFile.getZoom1Background()
        zoom1Old = etree.tostring(zoom1)

        section = LinacSection(self.name, self.colour, self.coord, self.width)
        self.assertEqual(etree.tostring(zoom1), zoom1Old)
        section.updateSvg()
        self.assertNotEqual(etree.tostring(zoom1), zoom1Old)

    def testUpdateZoom2(self):
        svgTree = etree.parse(self.blankSVGpath)
        svgRoot = svgTree.getroot()
        svgFile = svg.SVG()
        svgFile.setSvg(svgRoot)

        zoom2 = svgFile.getZoom2Background()
        zoom2Old = etree.tostring(zoom2)

        section = LinacSection(self.name, self.colour, self.coord, self.width)
        self.assertEqual(etree.tostring(zoom2), zoom2Old)
        section.updateSvg()
        self.assertNotEqual(etree.tostring(zoom2), zoom2Old)


    def tearDown(self):
        LinacSection.id = 1


class TestSectionElements(unittest.TestCase):
    def setUp(self):
        blankSVGpath = './blank.svg'
        svgTree = etree.parse(blankSVGpath)
        self.svgRoot = svgTree.getroot()
        self.svgFile = svg.SVG()
        self.svgFile.setSvg(self.svgRoot)
        self.aSection = LinacSection("A","grey", 0)
        self.bSection = LinacSection("B", "pink", 630)
        self.aSection.updateSvg()
        self.bSection.updateSvg()

    def testBigCaption(self):
        zoomNode = self.svgFile.getZoom1Background()
        bigCaption = self.svgFile.getElementById("section1bigText", zoomNode)
        self.assertEqual(bigCaption.text, "A")
        self.assertEqual(bigCaption.attrib["x"], "0")
        self.assertEqual(bigCaption.attrib["y"], "3653.7168")
        self.assertEqual(bigCaption.attrib["style"], "font-size:139.74479675px;font-style:normal;font-variant:normal;"
                                                     "font-weight:normal;font-stretch:normal;text-align:start;"
                                                     "line-height:125%;letter-spacing:0px;word-spacing:0px;writing-mode:"
                                                     "lr-tb;text-anchor:start;opacity:0.75;fill:#000000;fill-opacity:1;"
                                                     "stroke:none;font-family:DejaVu Sans;-inkscape-font-specification:"
                                                     "'DejaVu Sans, Normal'")

        secondBigCaption = self.svgFile.getElementById("section2bigText", zoomNode)
        self.assertEqual(secondBigCaption.attrib["x"], "630")
        self.assertEqual(secondBigCaption.attrib["y"], "3653.7168")
        self.assertEqual(secondBigCaption.text, "B")

    def testBigRect(self):
        zoomNode = self.svgFile.getZoom1Background()
        bigRect = self.svgFile.getElementById("section1bigRect", zoomNode)
        self.assertEqual(bigRect.attrib["x"], "0")
        self.assertEqual(bigRect.attrib["y"], "3495")
        self.assertEqual(bigRect.attrib["width"], "630")
        self.assertEqual(bigRect.attrib["height"], "209.99997")
        self.assertEqual(bigRect.attrib["style"], "fill:grey;fill-opacity:0.49803922;stroke:none")
        secondBigCaption = self.svgFile.getElementById("section2bigRect", zoomNode)
        self.assertEqual(secondBigCaption.attrib["x"], "630")
        self.assertEqual(secondBigCaption.attrib["y"], "3495")

    def testSmallCaption(self):
        zoomNode = self.svgFile.getZoom2Background()
        smallCaption = self.svgFile.getElementById("section1smallText", zoomNode)
        self.assertEqual(smallCaption.attrib["x"], "100")
        self.assertEqual(smallCaption.attrib["y"], "3702.2803")
        self.assertEqual(smallCaption.text, "A")

    def testBottomRect(self):
        zoomNode = self.svgFile.getZoom2Background()
        bottomRect = self.svgFile.getElementById("section1bottomRect", zoomNode)
        self.assertEqual(bottomRect.attrib["x"], "0")
        self.assertEqual(bottomRect.attrib["y"], "3685")
        self.assertEqual(bottomRect.attrib["width"], "630")
        self.assertEqual(bottomRect.attrib["height"], "19.999943")
        self.assertEqual(bottomRect.attrib["style"], "fill:#ffaaaa;fill-opacity:0.49803922;stroke:none;display:inline")

    def testVerticalLine(self):
        zoomNode = self.svgFile.getZoom2Background()
        verticalLine = self.svgFile.getElementById("section2verticalLine", zoomNode)
        self.assertEqual(verticalLine.attrib["x"], "1260")
        self.assertEqual(verticalLine.attrib["y"], "3594.144")
        self.assertEqual(verticalLine.attrib["width"], "0.85600001")
        self.assertEqual(verticalLine.attrib["height"], "109.856")
        self.assertEqual(verticalLine.attrib["style"], "fill:#3c3c3c;fill-opacity:0.74901961")

    def tearDown(self):
        LinacSection.id = 1

if __name__ == '__main__':
    unittest.main()