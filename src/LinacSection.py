from LinacAbstractSection import LinacAbstractSection
from lxml import etree
import svg


class LinacSection(LinacAbstractSection):
    id = 1

    def __init__(self, name, colour, startCoordinate, width=630):
        LinacAbstractSection.__init__(self, name, colour, startCoordinate, width)
        self.shortName = "section" + str(self.id)

        self.id = LinacSection.id
        LinacSection.id += 1

    def updateSvg(self):
        self.updateZoom1()
        self.updateZoom2()
        self.svgFile.setSvg(self.svgRoot)

    def createBigCaption(self, parentNode):
        textElement = etree.SubElement(parentNode, "text")
        textElement.attrib["id"] = self.shortName + "bigText"
        textElement.attrib["x"] = str(self.startCoordinate)
        textElement.attrib["y"] = "3653.7168"
        textElement.attrib["style"] = "font-size:139.74479675px;font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;text-align:start;line-height:125%;letter-spacing:0px;word-spacing:0px;writing-mode:lr-tb;text-anchor:start;opacity:0.75;fill:#000000;fill-opacity:1;stroke:none;font-family:DejaVu Sans;-inkscape-font-specification:'DejaVu Sans, Normal'"
        textElement.text = self.longName

    def createSmallCaption(self, parentNode):
        textElement = etree.SubElement(parentNode, "text")
        textElement.attrib["id"] = self.shortName + "smallText"
        textElement.attrib["x"] = str(self.startCoordinate+100)
        textElement.attrib["y"] = "3702.2803"
        textElement.attrib["style"] = "font-size:20px;font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;text-align:start;line-height:125%;letter-spacing:0px;word-spacing:0px;writing-mode:lr-tb;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none;display:inline;font-family:Sans;-inkscape-font-specification:'Sans, Normal'"
        textElement.text = self.longName

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

    def updateZoom1(self):
        zoomNode = self.svgFile.getZoom1Background()
        self.createBigRect(zoomNode)
        self.createBigCaption(zoomNode)

    def updateZoom2(self):
        zoomNode = self.svgFile.getZoom2Background()
        self.createBottomRect(zoomNode)
        self.createSmallCaption(zoomNode)
        self.createVerticalLine(zoomNode)
