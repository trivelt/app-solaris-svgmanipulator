from RingAbstractSection import RingAbstractSection
from RingSubsection import RingSubsection
from ArcDrawingTools import ArcDrawingTools
from lxml import etree

class RingSection(RingAbstractSection):
    id = 1

    def __init__(self, name, colour, startAngle, angle):
        RingAbstractSection.__init__(self, name, colour, startAngle, angle)
        self.subsections = list()
        self.shortName = "ringSection" + str(self.id)

        self.id = RingSection.id
        RingSection.id += 1

    def addSubsection(self, name, colour, angle):
        startAngle = self.computeSubsectionStartAngle()
        newSubsection = RingSubsection(name, colour, startAngle, angle)
        self.subsections.append(newSubsection)
        return newSubsection

    def computeSubsectionStartAngle(self):
        if len(self.subsections) == 0:
            return self.startAngle
        else:
            lastSubsection = self.subsections[-1]
            endOfLastSubsection = lastSubsection.endAngle
            startOfNextSubsection = endOfLastSubsection
            return startOfNextSubsection

    def getSubsection(self, name):
        for subsection in self.subsections:
            if subsection.longName == name:
                return subsection
        return None

    def getAllDevices(self):
        if self.hasSubsections():
            devicesFromSubsections = self.getDevicesFromSubsections()
            return self.devices + devicesFromSubsections
        else:
            return self.devices

    def hasSubsections(self):
        return True if self.subsections else False

    def getDevicesFromSubsections(self):
        devices = list()
        for subsection in self.subsections:
            devices.extend(subsection.devices)
        return devices

    def updateSvg(self):
        if self.isInUpperHalf():
            clockwiseFunction = ArcDrawingTools.describeArcAnticlockwise
        else:
            clockwiseFunction = ArcDrawingTools.describeArcClockwise
        self.drawSectionOnZoom1(clockwiseFunction)
        self.drawSectionOnZoom2(clockwiseFunction)
        self.updateSubsections()

    def updateSubsections(self):
        for subsection in self.subsections:
            subsection.updateSvg()

    def drawSectionOnZoom1(self, clockwiseFunction):
        self.drawBigColorfulCircle()
        self.drawBigText(clockwiseFunction)

    def drawBigColorfulCircle(self):
        zoomNode = self.svgFile.getZoom1Background()
        sectionElement = self.drawColourfulSection(zoomNode, 0, 250, "colourfulCircle")

        descElement = etree.SubElement(sectionElement, "desc")
        descElement.attrib["id"] = self.shortName + "desc"
        descElement.text = "section=" + self.longName

    def drawSectionOnZoom2(self, clockwiseFunction):
        zoomNode = self.svgFile.getZoom2Background()
        self.drawColourfulSection(zoomNode, -150, 20, "colorfulBorder")
        self.drawSmallText(clockwiseFunction)

    def drawColourfulSection(self, parentNode, radiusOffset, strokeWidth, idName):
        path = ArcDrawingTools.describeArcClockwise(self.centerX, self.centerY, self.radius+radiusOffset, self.startAngle, self.endAngle)

        sectionElement = etree.SubElement(parentNode, "path")
        sectionElement.attrib["id"] = self.shortName + idName
        sectionElement.attrib["d"] = path
        sectionElement.attrib["fill"] = "white"
        sectionElement.attrib["fill-opacity"] = "0.0"
        sectionElement.attrib["stroke"] =  self.colour
        sectionElement.attrib["stroke-width"] = str(strokeWidth)
        return sectionElement


    def drawBigText(self, clockwiseFunction):
        style = "font-size:200px;font-style:normal;"
        zoomElement = self.svgFile.getZoom1Background()
        if clockwiseFunction == ArcDrawingTools.describeArcAnticlockwise:
            radiusOffset = -100
        else:
            radiusOffset = 35
        self.drawText(zoomElement, radiusOffset, clockwiseFunction, style, "bigCaption")

    def drawSmallText(self, clockwiseFunction):
        style = "font-size:20px;font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;text-align:" \
                "start;line-height:125%;letter-spacing:0px;word-spacing:0px;writing-mode:lr-tb;text-anchor:start;fill:" \
                "#000000;fill-opacity:1;stroke:none;display:inline;font-family:Sans;-inkscape-font-specification:'Sans, Normal'"
        zoomElement = self.svgFile.getZoom2Background()
        if clockwiseFunction == ArcDrawingTools.describeArcAnticlockwise:
            radiusOffset = -157
        else:
            radiusOffset = -143

        self.drawText(zoomElement, radiusOffset, clockwiseFunction, style, "smallCaption")

    def drawText(self, parentNode, radiusOffset, clockwiseFunction, style, idName):
        defs = self.svgFile.getElementById("defs8812", self.svgRoot)
        pathDef = etree.SubElement(defs, "path")
        pathDef.attrib["id"] = self.shortName + idName + "Path"
        pathDef.attrib["d"] = clockwiseFunction(self.centerX, self.centerY, self.radius+radiusOffset, self.startAngle, self.endAngle)

        textElement = etree.SubElement(parentNode, "text")
        textElement.attrib["id"] = self.shortName + idName
        textElement.attrib["x"] = "0"
        textElement.attrib["y"] = "0"
        textElement.attrib["style"] = style
        textElement.attrib["text-anchor"] = "middle"

        textPathElement = etree.SubElement(textElement, "textPath")
        textPathElement.attrib["{http://www.w3.org/1999/xlink}href"] = "#" + self.shortName + idName + "Path"
        textPathElement.attrib["startOffset"] = "50%"
        textPathElement.text = self.longName