from LinacAbstractSection import LinacAbstractSection
from LinacSubsection import LinacSubsection
from lxml import etree
import svg


class LinacSection(LinacAbstractSection):
    id = 1

    def __init__(self, name, colour, startCoordinate, width=630):
        LinacAbstractSection.__init__(self, name, colour, startCoordinate, width)
        self.shortName = "section" + str(self.id)
        self.subsections = list()

        self.id = LinacSection.id
        LinacSection.id += 1

    def addSubsection(self, name, colour, width):
        startCoordinate = self.computeSubsectionStartCoordinate()
        if (startCoordinate + width) > (self.startCoordinate + self.width):
            print("Cannot create subsection - wrong parameters")
            return
        newSubsection = LinacSubsection(name, colour, startCoordinate, width)
        self.subsections.append(newSubsection)
        print("Adding subsection " + name + " to the section " + self.longName)
        return newSubsection

    def computeSubsectionStartCoordinate(self):
        if len(self.subsections) == 0:
            return self.startCoordinate
        else:
            lastSubsection = self.subsections[-1]
            startOfLastSubsection = lastSubsection.startCoordinate
            widthOfLastSubsection = lastSubsection.width
            startOfNextSubsection = startOfLastSubsection + widthOfLastSubsection
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

    def sortDevicesRecursively(self):
        self.sortDevices()
        for subsection in self.subsections:
            subsection.sortDevices()

    def updateSvg(self):
        self.updateZoom1()
        self.updateZoom2()
        self.svgFile.setSvg(self.svgRoot)
        self.updateSubsections()

    def getDevicesFromSubsections(self):
        devices = list()
        for subsection in self.subsections:
            devices.extend(subsection.devices)
        return devices

    def createBigCaption(self, parentNode):
        style = "font-size:150.0px;font-style:normal;'"
        self.drawText(parentNode, 3650, "BigCaption", style)

    def createSmallCaption(self, parentNode):
        style = "font-size:20px;font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;" \
                "font-family:Sans;-inkscape-font-specification:'Sans, Normal'"
        self.drawText(parentNode, 3702, "SmallCaption", style)

    def createBottomRect(self, parentNode):
        rectElement = etree.SubElement(parentNode, "rect")
        rectElement.attrib["id"] = self.shortName + "bottomRect"
        rectElement.attrib["x"] = str(self.startCoordinate)
        rectElement.attrib["y"] = "3685"
        rectElement.attrib["width"] = str(self.width)
        rectElement.attrib["height"] = "19.999943"
        rectElement.attrib["style"] = "fill:#ffaaaa;fill-opacity:0.49803922;stroke:none;display:inline"

    def createBigRect(self, parentNode):
        rectElement = etree.SubElement(parentNode, "rect")
        rectElement.attrib["id"] = self.shortName + "bigRect"
        rectElement.attrib["x"] = str(self.startCoordinate)
        rectElement.attrib["y"] = "3495"
        rectElement.attrib["width"] = str(self.width)
        rectElement.attrib["height"] = "209.99997"
        rectElement.attrib["style"] = "fill:" + self.colour + ";fill-opacity:0.49803922;stroke:none"

        descElement = etree.SubElement(rectElement, "desc")
        descElement.attrib["id"] = self.shortName + "desc"
        descElement.text = "section=" + self.longName

    def createVerticalLine(self, parentNode):
        rectElement = etree.SubElement(parentNode, "rect")
        rectElement.attrib["id"] = self.shortName + "verticalLine"
        rectElement.attrib["x"] = str(self.startCoordinate+self.width)
        rectElement.attrib["y"] = "3594.144"
        rectElement.attrib["width"] = "0.85600001"
        rectElement.attrib["height"] = "109.856"
        rectElement.attrib["style"] = "fill:#3c3c3c;fill-opacity:0.74901961"

    def drawText(self, parentNode, yCoord, idName, style):
        defs = self.svgFile.getElementById("defs8812", self.svgRoot)
        pathDef = etree.SubElement(defs, "path")
        pathDef.attrib["id"] = self.shortName + idName + "Path"
        pathDef.attrib["d"] = self.computeCaptionPath(yCoord)

        textElement = etree.SubElement(parentNode, "text")
        textElement.attrib["id"] = self.shortName + idName
        textElement.attrib["style"] = style
        textElement.attrib["text-anchor"] = "middle"

        textPathElement = etree.SubElement(textElement, "textPath")
        textPathElement.attrib["{http://www.w3.org/1999/xlink}href"] = "#" + self.shortName + idName + "Path"
        textPathElement.attrib["startOffset"] = "50%"
        textPathElement.attrib["id"] = self.shortName + idName + "TextPath"
        textPathElement.text = self.displayedName

    def computeCaptionPath(self, yCoord):
        path = ["M", self.startCoordinate, yCoord, "l", self.width, 0]
        return " ".join([str(x) for x in path])

    def updateZoom1(self):
        zoomNode = self.svgFile.getZoom1Background()
        self.createBigRect(zoomNode)
        self.createBigCaption(zoomNode)

    def updateZoom2(self):
        zoomNode = self.svgFile.getZoom2Background()
        self.createBottomRect(zoomNode)
        self.createSmallCaption(zoomNode)
        self.createVerticalLine(zoomNode)

    def updateSubsections(self):
        for section in self.subsections:
            section.updateSvg()