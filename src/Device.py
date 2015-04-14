from lxml import etree
import svg

class Device:
    def __init__(self, name, icon, coordinates):
        self.realCoordinates = coordinates
        self.name = name
        self.icon = icon
        self.subsystem = ""
        self.section = None
        self.svgCoordinates = None
        self.numberInSection = None
        self.findAndSetSubsystemName()

    def findAndSetSubsystemName(self):
        nameParts = self.name.split("/")
        if len(nameParts) > 1:
            self.subsystem = nameParts[1]

    def updateSvg(self):
        pass

    def isRingElement(self):
        return self.getSectionName().startswith("R")

    def isLinacElement(self):
        return self.getSectionName().startswith("I")

    def getSectionName(self):
        nameParts = self.name.split("/")
        if len(nameParts) > 0:
            return nameParts[0]
        else:
            return None

