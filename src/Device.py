from lxml import etree
import svg

class Device:
    def __init__(self, name, icon, coordinates):
        self.realCoordinates = coordinates
        self.name = name
        self.icon = icon
        self.subsystemName = ""
        self.section = None
        self.svgCoordinate = None
        self.numberInSection = None
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
        self.assignSvgCoordinate()
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

    def assignSvgCoordinate(self):
        if self.numberInSection == 0:
            self.svgCoordinate = self.section.startCoordinate + self.section.getDistanceBetweenDevices()
        else:
            previousDeviceInSection = self.section.getDevice(self.numberInSection-1)
            self.svgCoordinate = previousDeviceInSection.svgCoordinate + self.section.getDistanceBetweenDevices()

    def createSvgNode(self):
        svgFile = svg.SVG()
        svgRoot = svgFile.getSvg()
        subsystemNode = svgFile.getSubsystemZoomNode(self.subsystemName)

        deviceElement = etree.SubElement(subsystemNode, "use")
        deviceElement.attrib["id"] = self.generateSimpleName()
        deviceElement.attrib["{http://www.w3.org/1999/xlink}href"] = "#" + self.icon.name
        deviceElement.attrib["x"] = str(self.svgCoordinate)
        deviceElement.attrib["y"] = "3585"

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

