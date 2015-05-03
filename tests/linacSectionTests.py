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

class TestSectionBase(unittest.TestCase):
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

    def testHasSubsections(self):
        section = LinacSection("I-K00", None, None)
        self.assertEqual(section.hasSubsections(), False)

        sectionWithSubsections = LinacSection("I-S01", None, 100)
        sectionWithSubsections.addSubsection("I-S01A", None, 0)
        self.assertEqual(sectionWithSubsections.hasSubsections(), True)

    def testGetSubsection(self):
        section = LinacSection("I-K00", None, 100)
        subsection = section.addSubsection("I-K00A", None, 100)
        self.assertEqual(section.getSubsection("I-K00B"), None)
        self.assertEqual(section.getSubsection("I-K00A"), section.subsections[0])
        self.assertEqual(subsection, section.getSubsection("I-K00A"))

    def testGetAllDevices(self):
        section = LinacSection("I-K00", None, 0)

        firstDevice = Device("test1", None, None)
        secondDevice = Device("test2", None, None)
        thirdDevice = Device("test3", None, None)
        fourthDevice = Device("test4", None, None)

        section.addSubsection("I-K01A", None, 100)
        section.addSubsection("I-K01B", None, 100)
        firstSubsection = section.getSubsection("I-K01A")
        secondSubsection = section.getSubsection("I-K01B")

        firstSubsection.addDevice(firstDevice)
        section.addDevice(secondDevice)
        secondSubsection.addDevice(thirdDevice)
        firstSubsection.addDevice(fourthDevice)

        allDevices = section.getAllDevices()
        self.assertTrue(firstDevice in allDevices)
        self.assertTrue(secondDevice in allDevices)
        self.assertTrue(thirdDevice in allDevices)
        self.assertTrue(fourthDevice in allDevices)
        self.assertEqual(len(allDevices), 4)

    def testComputeSubsectionCoordinate(self):
        section = LinacSection("test", None, 100)
        self.assertEqual(section.computeSubsectionStartCoordinate(), 100)

        section.addSubsection("subtest", None, 45)
        self.assertEqual(section.computeSubsectionStartCoordinate(), 145)

    def testSortDevicesRecursively(self):
        section = LinacSection("A", None, 100)
        subsection = section.addSubsection("A01", None, 50)
        firstDevice = Device("first", None, [301,222])
        secondDevice = Device("second", None, [154,222])
        thirdDevice = Device("third", None, [101,222])
        fourthDevice = Device("fourth", None, [55, 30])
        subsection.addDevice(firstDevice)
        subsection.addDevice(secondDevice)
        section.addDevice(thirdDevice)
        section.addDevice(fourthDevice)

        devices = section.getAllDevices()
        self.assertEqual(devices[0], thirdDevice)
        self.assertEqual(devices[2], firstDevice)

        section.sortDevicesRecursively()
        devices = section.getAllDevices()
        self.assertEqual(devices[0], fourthDevice)
        self.assertEqual(devices[2], secondDevice)



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
        bigCaptionNode = self.svgFile.getElementById("section1BigCaption", zoomNode)
        bigCaption =  self.svgFile.getElementById("section1BigCaptionTextPath", bigCaptionNode)
        self.assertEqual(bigCaption.text, "A")
        self.assertEqual(bigCaptionNode.attrib["style"], "font-size:150.0px;font-style:normal;'")

        secondBigCaptionNode = self.svgFile.getElementById("section2BigCaption", zoomNode)
        secondBigCaption =  self.svgFile.getElementById("section2BigCaptionTextPath", secondBigCaptionNode)
        self.assertEqual(secondBigCaption.text, "B")

    def testBigRect(self):
        zoomNode = self.svgFile.getZoom1Background()
        bigRect = self.svgFile.getElementById("section1bigRect", zoomNode)
        self.assertEqual(bigRect.attrib["x"], "0")
        self.assertEqual(bigRect.attrib["y"], "3495")
        self.assertEqual(bigRect.attrib["width"], "630")
        self.assertEqual(bigRect.attrib["height"], "209.99997")
        self.assertEqual(bigRect.attrib["style"], "fill:grey;fill-opacity:0.79803922;stroke:none")
        secondBigCaption = self.svgFile.getElementById("section2bigRect", zoomNode)
        self.assertEqual(secondBigCaption.attrib["x"], "630")
        self.assertEqual(secondBigCaption.attrib["y"], "3495")

    def testSmallCaption(self):
        zoomNode = self.svgFile.getZoom2Background()
        smallCaptionNode = self.svgFile.getElementById("section1SmallCaption", zoomNode)
        smallCaption = self.svgFile.getElementById("section1SmallCaptionTextPath", smallCaptionNode)
        self.assertEqual(smallCaptionNode.attrib["text-anchor"], "middle")
        self.assertEqual(smallCaption.text, "A")

    def testBottomRect(self):
        zoomNode = self.svgFile.getZoom2Background()
        bottomRect = self.svgFile.getElementById("section1bottomRect", zoomNode)
        self.assertEqual(bottomRect.attrib["x"], "0")
        self.assertEqual(bottomRect.attrib["y"], "3685")
        self.assertEqual(bottomRect.attrib["width"], "630")
        self.assertEqual(bottomRect.attrib["height"], "19.999943")
        self.assertEqual(bottomRect.attrib["style"], "fill:grey;fill-opacity:0.79803922;stroke:none;display:inline")

    def testVerticalLine(self):
        zoomNode = self.svgFile.getZoom2Background()
        verticalLine = self.svgFile.getElementById("section2verticalLine", zoomNode)
        self.assertEqual(verticalLine.attrib["x"], "1260")
        self.assertEqual(verticalLine.attrib["y"], "3594.144")
        self.assertEqual(verticalLine.attrib["width"], "0.85600001")
        self.assertEqual(verticalLine.attrib["height"], "109.856")
        self.assertEqual(verticalLine.attrib["style"], "fill:#3c3c3c;fill-opacity:0.74901961")

    def testDisplayedName(self):
        cSection = LinacSection("C", "green", 640)
        cSection.setDisplayedName("ABCDEFGH")
        cSection.updateSvg()

        zoomNode = self.svgFile.getZoom2Background()
        smallCaptionNode = self.svgFile.getElementById("section3SmallCaption", zoomNode)
        smallCaption = self.svgFile.getElementById("section3SmallCaptionTextPath", smallCaptionNode)
        self.assertEqual(smallCaption.text, "ABCDEFGH")

        zoomNode = self.svgFile.getZoom1Background()
        bigCaptionNode = self.svgFile.getElementById("section3BigCaption", zoomNode)
        bigCaption = self.svgFile.getElementById("section3BigCaptionTextPath", bigCaptionNode)
        self.assertEqual(bigCaption.text, "ABCDEFGH")

    def tearDown(self):
        LinacSection.id = 1

if __name__ == '__main__':
    unittest.main()