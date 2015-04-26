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
        if self.section == None:
            print(exceptionMessage + "Probably it was not added to the appropriate section.")
            raise Exception
        if self.icon == None:
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

        deviceElement = etree.SubElement(subsystemNode, "use")
        deviceElement.attrib["id"] = self.generateSimpleName()
        deviceElement.attrib["{http://www.w3.org/1999/xlink}href"] = "#" + self.icon.name
        deviceElement.attrib["x"] = str(self.svgCoordinateX)
        deviceElement.attrib["y"] = str(self.svgCoordinateY)

        descElement = etree.SubElement(deviceElement, "desc")
        descElement.attrib["id"] = self.generateSimpleName() + "Desc"
        descElement.text = "device=" + self.name

    def generateSimpleName(self):
        simpleName = self.name.lower()
        simpleName = simpleName.replace("-", "")
        simpleName = simpleName.replace("/", "")
        return simpleName

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

