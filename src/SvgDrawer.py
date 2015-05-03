import src.svg as svg
from lxml import etree
from Linac import Linac
from Ring import Ring
from TangoDeviceManager import TangoDeviceManager

class SvgDrawer:
    def __init__(self):
        self.linac = Linac()
        self.ring = Ring()
        self.tDeviceManager = TangoDeviceManager()
        self.svgFile = None

    def setTangoHost(self, tangoHost):
        self.tDeviceManager.setTangoDatabaseAddress(tangoHost)

    def loadSvg(self, svgPath):
        svgTree = etree.parse(svgPath)
        self.svgFile = svg.SVG()
        self.svgFile.setSvg(svgTree.getroot())

    def saveSvg(self, svgPath):
        svgRoot = self.svgFile.getSvg()
        toWrite = etree.tostring(svgRoot, pretty_print=True)
        fd = open(svgPath, 'w')
        fd.write(toWrite)

    def addSectionToLinac(self, name, colour, width):
        return self.linac.addSection(name, colour, width)

    def addSectionToRing(self, name, colour, angle):
        return self.ring.addSection(name, colour, angle)

    def addSubsection(self, section, subsectionName, colour, widthOrAngle):
        section.addSubsection(subsectionName, colour, widthOrAngle)

    def drawAll(self):
        devices = self.tDeviceManager.getDevices()
        self.initializeBlankSvg()

        self.drawAccelerator()
        self.drawIcons(devices)
        self.drawDevices(devices)

    def initializeBlankSvg(self):
        blankSVGpath = '../src/blank.svg'
        self.loadSvg(blankSVGpath)

    def drawAccelerator(self):
        self.linac.updateSvg()
        self.ring.updateSvg()

    def drawIcons(self, devices):
        icons = set()
        for device in devices:
            icons.add(device.icon)

        for icon in icons:
            icon.updateSvg()

    def drawDevices(self, devices):
        self.addDeviceToAccelerator(devices)
        devices = self.sortDevices()
        self.drawDevicesOnSvg(devices)

    def addDeviceToAccelerator(self, devices):
        for device in devices:
            if device.isLinacElement():
                self.linac.addDevice(device)
            elif device.isRingElement():
                self.ring.addDevice(device)

        self.ring.assignDevicesBeforeDrawing()
        self.linac.assignDevicesBeforeDrawing()

    def sortDevices(self):
        sortedDevices = list()
        sortedDevices.extend(self.linac.getAllDevicesSorted())
        sortedDevices.extend(self.ring.getAllDevicesSorted())
        return sortedDevices

    def drawDevicesOnSvg(self, devices):
        for device in devices:
            device.updateSvg()