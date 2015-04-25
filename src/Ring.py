from math import pi, cos, sin
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
        self.svgRoot = self.svgFile.getSvg()

        # white circle in zoom1
        parentNode = self.svgFile.getZoom1Background()
        path = self.describeArc(11989.075, 4827.0225, 2705.4143-150, 0, 359.99)
        sectionElement = etree.SubElement(parentNode, "path")
        sectionElement.attrib["id"] = "whiteCircle"
        sectionElement.attrib["d"] = path
        sectionElement.attrib["fill"] = "white"
        sectionElement.attrib["stroke"] = "white"
        sectionElement.attrib["stroke-width"] = "50"

        # white circle in zoom2
        zoomNode = self.svgFile.getZoom2Background()
        path = self.describeArc(11989.075, 4827.0225, 2705.4143-200, 0, 359.99)
        sectionElement = etree.SubElement(zoomNode, "path")
        sectionElement.attrib["id"] = "whiteBorder"
        sectionElement.attrib["d"] = path
        sectionElement.attrib["fill"] = "white"
        sectionElement.attrib["stroke"] = "white"
        sectionElement.attrib["stroke-width"] = "80"

    def polarToCartesian(self, centerX, centerY, radius, angleInDegrees):
        angleInRadians = (angleInDegrees-90.0) * pi / 180.0
        #print "Angle in radians=" + str(angleInRadians)
        x = centerX + (radius * cos(angleInRadians))
        y = centerY + (radius * sin(angleInRadians))
        return [x, y]


    def describeArc(self, x, y, radius, startAngle, endAngle):
        start = self.polarToCartesian(x, y, radius, endAngle)
        #print("startX=" + str(start[0]) + ", startY=" + str(start[1]))
        end = self.polarToCartesian(x, y, radius, startAngle)
        #print("endX=" + str(end[0]) + ", endY=" + str(end[1]))

        arcSweep = "0" if endAngle - startAngle <= 180 else "1"

        d = "M " + str(start[0]) + " " + str(start[1]) + \
             " A " + str(radius) + " " + str(radius) + " 0 " + arcSweep + " 0 "  +str(end[0]) + " " + str(end[1]) + \
            " L " + str(x) + " " + str(y) + \
            " L " + str(start[0]) + " " + str(start[1]) + " Z"

        return d