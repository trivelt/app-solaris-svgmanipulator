from ArcDrawingTools import ArcDrawingTools
from RingSection import RingSection
from svg import SVG
from lxml import etree

class Ring:
    def __init__(self):
        self.sections = list()
        self.radius = 2645.4143

    def addSection(self, name, colour=None, angleInDegrees=45):
        startAngle = self.computeNewSectionStartAngle()
        newSection = RingSection(name, colour, startAngle, angleInDegrees)
        self.sections.append(newSection)
        return newSection

    def computeNewSectionStartAngle(self):
        if len(self.sections) == 0:
            return -90
        else:
            lastSection = self.sections[-1]
            return lastSection.endAngle

    def getSection(self, name):
        searchedSection = None
        for section in self.sections:
            if section.longName == name:
                searchedSection = section
            for subsection in section.subsections:
                if subsection.longName == name:
                    searchedSection = subsection
        return searchedSection

    def updateSvg(self):
        for section in self.sections:
            section.updateSvg()
        self.drawWhiteCircles()

    def drawWhiteCircles(self):
        self.svgFile = SVG()
        zoom1Node = self.svgFile.getZoom1Background()
        zoom2Node = self.svgFile.getZoom2Background()
        self.drawWhiteCircle(zoom1Node, -150, 50, "whiteCircleZoom1")
        self.drawWhiteCircle(zoom2Node, -200, 80, "whiteCircleZoom2")

    def drawWhiteCircle(self, parentNode, radiusOffset, strokeWidth, idName):
        path = ArcDrawingTools.describeArcClockwise(11989.075, 4827.0225, 2705.4143+radiusOffset, 0, 359.99)
        sectionElement = etree.SubElement(parentNode, "path")
        sectionElement.attrib["id"] = idName
        sectionElement.attrib["d"] = path
        sectionElement.attrib["fill"] = "white"
        sectionElement.attrib["stroke"] = "white"
        sectionElement.attrib["stroke-width"] = str(strokeWidth)