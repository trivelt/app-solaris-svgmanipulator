#!/usr/bin/python
import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
import unittest
from src.Linac import Linac
import src.svg as svg
from lxml import etree


class TestSvg(unittest.TestCase):
    def setUp(self):
        blankSVGpath = 'blank.svg'
        svgTree = etree.parse(blankSVGpath)
        self.svgRoot = svgTree.getroot()
        self.svgFile = svg.SVG()
        self.svgFile.setSvg(self.svgRoot)

    def testSetSvg(self):
        self.assertEqual(self.svgRoot, self.svgFile.getSvg())

    def testGetSymbolNode(self):
        symbols = self.svgFile.getSymbolsNode()
        self.assertEqual(symbols.attrib["id"], "symbols")
        self.assertEqual(symbols.attrib["{http://www.inkscape.org/namespaces/inkscape}label"], "symbols")

    def testBackgroundNode(self):
        background = self.svgFile.getBackgroundNode()
        self.assertEqual(background.attrib["id"], "background")
        self.assertEqual(background.attrib["{http://www.inkscape.org/namespaces/inkscape}label"], "background")

    def testZoom1Background(self):
        zoomNode = self.svgFile.getZoom1Background()
        self.assertEqual(zoomNode.attrib["id"], "layer2")
        self.assertEqual(zoomNode.attrib["class"], "zoom level1")
        self.assertEqual(zoomNode.attrib["{http://www.inkscape.org/namespaces/inkscape}label"], "zoom1")

    def testZoom2Background(self):
        zoomNode = self.svgFile.getZoom2Background()
        self.assertEqual(zoomNode.attrib["id"], "layer1")
        self.assertEqual(zoomNode.attrib["class"], "zoom level2")
        self.assertEqual(zoomNode.attrib["{http://www.inkscape.org/namespaces/inkscape}label"], "zoom2")

    def testSubsystemNode(self):
        magNode = self.svgFile.getSubsystemNode("MAG")
        diaNode = self.svgFile.getSubsystemNode("DIA")
        rfNode = self.svgFile.getSubsystemNode("RF")
        vacNode = self.svgFile.getSubsystemNode("VAC")

        self.assertEqual(magNode.attrib["class"], "layer selectable")
        self.assertEqual(magNode.attrib["id"], "magnet")
        self.assertEqual(diaNode.attrib["id"], "diagnostic")
        self.assertEqual(rfNode.attrib["id"], "layer4")
        self.assertEqual(vacNode.attrib["id"], "vacuum")

    def testSubsystemZoomNode(self):
        magNode = self.svgFile.getSubsystemZoomNode("MAG")
        self.assertEqual(magNode.attrib["class"], "zoom level2")

    def testFoundElement(self):
        linac = Linac()
        linac.addSection("TEST-abc")
        linac.updateSvg()
        zoomNode = self.svgFile.getZoom2Background()
        sectionRectNode = self.svgFile.getElementById("section1bottomRect", zoomNode)

        self.assertEqual(sectionRectNode.attrib["id"], "section1bottomRect")
        self.assertEqual(sectionRectNode.attrib["width"], "630")

    def testFoundElementByLabel(self):
        magNode = self.svgFile.getElementByLabel("MAG", self.svgRoot[3])
        self.assertEqual(magNode.attrib["id"], "magnet")

if __name__ == '__main__':
    unittest.main()