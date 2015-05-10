from Device import Device
from os import path
import re

class IconAssigner:
    iconDict = {
        "^Q.*" : "symbol-quadrupole.svg",
        "^CO.Y.*" : "symbol30040.svg",
        "^CO.X.*" : "symbol30062.svg",
        "^VGMB.*" : "symbol-valve.svg",
        "^CT.*" : "symbol-ct.svg",
        "^BP.*" : "symbol7975.svg",
        "^SCRN.*" : "symbol12414.svg",
        "^DET.*" : "symbol12414.svg",
        "^DIA.*" : "symbol-dipole.svg.svg",
        "^SXL.*" : "symbol10623.svg",
        "^SOL.*" : "symbol-solenoid.svg"
    }
    def __init__(self):
        self.resourceDir = self.getResourceDirPath()

    def getResourceDirPath(self):
        currentFilePath = path.realpath(__file__)
        currentDirPath = path.dirname(currentFilePath)
        splittedPath = currentDirPath.split("/")
        splittedPath[-1] = "resources"
        return "/".join(splittedPath)

    def getIconPath(self, device):
        iconName = self.findIconForDevice(device)
        iconPath = self.createPathToIcon(iconName)
        return iconPath

    def findIconForDevice(self, device):
        deviceName = device.getShortName()
        deviceName = deviceName.upper()
        iconName = None
        for patternString in IconAssigner.iconDict:
            pattern = re.compile(patternString)
            if pattern.match(deviceName):
                print "To the device " + deviceName + " matches pattern " + patternString
                iconName = IconAssigner.iconDict[patternString]
                break
        if iconName is None:
            iconName = "default.svg"
        return iconName

    def createPathToIcon(self, iconName):
        iconPath = self.resourceDir
        iconPath += "/"
        iconPath += str(iconName)
        return iconPath