from svg import SVG

class Section:
    def __init__(self, name, colour):
        self.longName = name
        self.displayedName = name
        self.colour = colour
        self.devices = list()

        self.svgFile = SVG()
        self.svgRoot = self.svgFile.getSvg()

    def __repr__(self):
        return self.longName

    def addDevice(self, device):
        device.numberInSection = len(self.devices)
        self.devices.append(device)

    def getDevice(self, number):
        if number >= len(self.devices) or number < 0:
            return None
        else:
            return self.devices[number]

    def sortDevices(self):
        self.devices = sorted(self.devices, key=lambda devices: devices.realCoordinates[0])
        
    def numberOfDevices(self):
        return len(self.devices)

    def setDisplayedName(self, name):
        self.displayedName = name