import PyTango
import os
from Device import Device
from Icon import Icon

class TangoDeviceManager:
    def __init__(self):
        self.setTangoDatabaseAddress("192.168.130.200:10000")
        self.database = PyTango.Database()
        self.devices = []

    def setTangoDatabaseAddress(self, address):
        # default = 192.168.130.100:10000
        os.environ['TANGO_HOST'] = address

    def getDevices(self):
        allTangoDevices = self.getAllDevicesFromDatabase()
        self.filterDevices(allTangoDevices)
        self.getAttributesFromDbAndAssignToDevices()
        return self.devices

    def getAllDevicesFromDatabase(self):
        servers = self.database.get_server_list()
        allTangoDevices = []
        for server in servers:
            allTangoDevices.append(self.database.get_device_class_list(server))
        return allTangoDevices

    def filterDevices(self, devices):
        for deviceGroup in devices:
            self.filterDevicesInDeviceGroup(deviceGroup)

    def filterDevicesInDeviceGroup(self, deviceNames):
        for name in deviceNames:
            device = Device(name, None, None)
            if device.isLinacElement() or device.isRingElement():
                self.devices.append(device)

    def getAttributesFromDbAndAssignToDevices(self):
        self.assignCoordinatesToDevices()
        self.assignIconsToDevices()

    def assignIconsToDevices(self):
        #proxyDevice = PyTango.DeviceProxy("I-S00/MAG/I-S00-MAG-COBX2")
        deviceToRemove = []
        for device in self.devices:
            iconProperty = self.database.get_device_property(device.name, "icon")
            if not iconProperty["icon"]:
                print("Device " + device.name + " has not set icon path property")
                deviceToRemove.append(device)
            else:
                iconPath = iconProperty["icon"][0]
                icon = Icon(iconPath)
                device.icon = icon
        for device in deviceToRemove:
            self.devices.remove(device)

    def assignCoordinatesToDevices(self):
        deviceToRemove = []
        for device in self.devices:
            proxyDevice = PyTango.DeviceProxy(device.name)
            xCoordProperty = proxyDevice.get_property("x")
            yCoordProperty = proxyDevice.get_property("y")
            if not xCoordProperty["x"] or not yCoordProperty["y"]:
                print("Device " + device.name + " has not set coordinate properties")
                deviceToRemove.append(device)
            else:
                yCoord = float(yCoordProperty["y"][0])
                xCoord = float(xCoordProperty["x"][0])
                device.realCoordinates = [xCoord, yCoord]
        for device in deviceToRemove:
            self.devices.remove(device)
