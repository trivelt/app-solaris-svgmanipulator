from LinacSection import LinacSection

class Linac:
    def __init__(self):
        self.sections = list()
        self.width = 6778.519
        LinacSection.id = 1

    def addSection(self, name, colour=None, width=630):
        print("Adding new section " + str(name) + " to the linac")
        if colour == None:
            colour = self.getNextSectionColour()
        coordinate = self.computeNewSectionCoordinate()
        newSection = LinacSection(name, colour, coordinate, width)
        self.sections.append(newSection)
        return newSection

    def addLastLongSection(self):
        colour = self.getNextSectionColour()
        coordinate = self.computeNewSectionCoordinate()
        newSection = LinacSection("", colour, coordinate, 1885+self.width-coordinate)
        self.sections.append(newSection)

    def addDevice(self, device):
        print("Adding new device " + device.name + " to the linac")
        sectionName = device.getSectionName()
        deviceSection = self.getSection(sectionName)
        if deviceSection == None:
            print("Device can not be added - wrong section name")
            return
        deviceSection.addDevice(device)
        device.section = deviceSection

    def computeNewSectionCoordinate(self):
        if len(self.sections) == 0:
            return 1885
        else:
            lastSection = self.sections[-1]
            startOfLastSection = lastSection.startCoordinate
            widthOfLastSection = lastSection.width
            startOfNextSection = startOfLastSection+widthOfLastSection
            return startOfNextSection

    def getNextSectionColour(self):
        if len(self.sections) == 0:
            return "#55ffdd"
        else:
            previousSectionColour = self.sections[-1].colour
            if previousSectionColour != "#b3b3b3":
                return "#b3b3b3"
            else:
                return "grey"

    def assignDevicesBeforeDrawing(self):
        for section in self.sections:
            if section.hasSubsections() and section.numberOfDevices() > 0:
                self.assignDevicesToSubsections(section)

    def assignDevicesToSubsections(self, section):
        for device in section.devices:
            nearestDevice = self.findNearestDevice(device)
            if nearestDevice is None:
                nearestSubsection = section.subsections[0]
            else:
                nearestSubsection = nearestDevice.section
            nearestSubsection.addDevice(device)
            device.section = nearestSubsection
            section.devices.remove(device)

    def findNearestDevice(self, unassignedDevice):
        deviceSection = unassignedDevice.section
        devicesFromSubsections = deviceSection.getDevicesFromSubsections()
        if len(devicesFromSubsections) == 0:
            return None

        nearestDevice = devicesFromSubsections[0]
        minimalDistance = abs(devicesFromSubsections[0].realCoordinates[0] - unassignedDevice.realCoordinates[0])

        for device in devicesFromSubsections:
            distanceFromDevice = abs(device.realCoordinates[0] - unassignedDevice.realCoordinates[0])
            if  distanceFromDevice < minimalDistance:
                minimalDistance = distanceFromDevice
                nearestDevice = device
        return nearestDevice


    def numberOfSections(self):
        return len(self.sections)

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
