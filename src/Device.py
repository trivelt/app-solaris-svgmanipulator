from SettingsCloud import SettingsCloud
from ArcDrawingTools import ArcDrawingTools
from lxml import etree
import svg

class Device:
    def __init__(self, name, icon, coordinates):
        self.realCoordinates = coordinates
        self.name = name
        self.icon = icon
        self.subsystemName = ""
        self.section = None
        self.numberInSection = None

        self.svgCoordinateX = None
        self.svgCoordinateY = None


        self.findAndSetSubsystemName()

    def findAndSetSubsystemName(self):
        nameParts = self.name.split("/")
        if len(nameParts) > 1:
            self.subsystemName = nameParts[1]

    def updateSvg(self):
        try:
            self.checkNecessaryConditions()
        except:
            return
        self.assignSvgCoordinates()
        self.createSvgNode()


    def checkNecessaryConditions(self):
        exceptionMessage = "Device " + self.name + " cannot be drawn. "
        if self.section is None:
            print(exceptionMessage + "Probably it was not added to the appropriate section.")
            raise Exception
        if self.icon is None:
            print(exceptionMessage + "No icon assigned to the device. ")
            raise Exception
        if self.subsystemName == "":
            print(exceptionMessage + "Subsystem name is invalid.")
            raise Exception

    def assignSvgCoordinates(self):
        if self.isLinacElement():
            self.assignSvgCoordinatesForLinacDevice()
        else:
            self.assignSvgCoordinatesForRingDevice()

    def assignSvgCoordinatesForLinacDevice(self):
        self.svgCoordinateY = 3585
        if self.numberInSection == 0:
            self.svgCoordinateX = self.section.startCoordinate + self.section.getDistanceBetweenDevices()
        else:
            self.svgCoordinateX = self.section.startCoordinate + (self.numberInSection+1) * self.section.getDistanceBetweenDevices()

    def assignSvgCoordinatesForRingDevice(self):
        centerX = 11977.075
        centerY = 4814.0
        radius = 2645.4143
        if self.numberInSection == 0:
            angle = self.section.startAngle + self.section.getAngleBetweenDevices()
        else:
            angle = self.section.startAngle + (self.numberInSection+1) * self.section.getAngleBetweenDevices()
        self.svgCoordinateX, self.svgCoordinateY = ArcDrawingTools.polarToCartesian(centerX, centerY, radius, angle)

    def createSvgNode(self):
        svgFile = svg.SVG()
        svgRoot = svgFile.getSvg()
        subsystemNode = svgFile.getSubsystemZoomNode(self.subsystemName)

        if subsystemNode != None:
            self.drawDeviceIcon(subsystemNode)
            if SettingsCloud.getParameter("deviceCaptions") == True:
                self.drawDeviceCaption(subsystemNode)
        else:
            print "Device " + self.name + " can not be added - wrong subsystem name"

    def drawDeviceIcon(self, parentNode):
        deviceElement = etree.SubElement(parentNode, "use")
        deviceElement.attrib["id"] = self.generateSimpleName()
        deviceElement.attrib["{http://www.w3.org/1999/xlink}href"] = "#" + self.icon.name
        deviceElement.attrib["x"] = str(self.svgCoordinateX)
        deviceElement.attrib["y"] = str(self.svgCoordinateY)

        descElement = etree.SubElement(deviceElement, "desc")
        descElement.attrib["id"] = self.generateSimpleName() + "Desc"
        descElement.text = "device=" + self.name

    def drawDeviceCaption(self, parentNode):
        if self.isLinacElement():
            self.drawLinacDeviceCaption(parentNode)
        else:
            self.drawRingDeviceCaption(parentNode)

    def drawLinacDeviceCaption(self, parentNode):
        textElement = etree.SubElement(parentNode, "text")
        textElement.attrib["id"] = self.generateSimpleName() + "Caption"
        textElement.attrib["style"] = "font-size:10px;"
        textElement.attrib["x"] = str(self.svgCoordinateX + 2)
        textElement.attrib["y"] = str(self.svgCoordinateY + 40)
        textElement.attrib["transform"] = "rotate(45, " + str(self.svgCoordinateX+2) + ", " \
                                          + str(self.svgCoordinateY + 40) + ")"
        textElement.text = self.getShortName()

    def drawRingDeviceCaption(self, parentNode):
        textElement = etree.SubElement(parentNode, "text")
        textElement.attrib["id"] = self.generateSimpleName() + "Caption"
        textElement.attrib["style"] = "font-size:10px;"
        textElement.attrib["x"] = str(self.svgCoordinateX + 10)
        textElement.attrib["y"] = str(self.svgCoordinateY + 0)
        #textElement.attrib["transform"] = "rotate(45, " + str(self.svgCoordinateX+2) + ", " + str(self.svgCoordinateY+1) + ")"
        textElement.text = self.getShortName()

    def generateSimpleName(self):
        simpleName = self.name.lower()
        simpleName = simpleName.replace("-", "")
        simpleName = simpleName.replace("/", "")
        return simpleName

    def getShortName(self):
        nameParts = self.name.split("-")
        if len(nameParts) > 0:
            return nameParts[-1]
        else:
            return self.name

    def isRingElement(self):
        return self.getSectionName().startswith("R1-")

    def isLinacElement(self):
        return self.getSectionName().startswith("I-")

    def getSectionName(self):
        nameParts = self.name.split("/")
        if len(nameParts) > 0:
            return nameParts[0]
        else:
            return None

