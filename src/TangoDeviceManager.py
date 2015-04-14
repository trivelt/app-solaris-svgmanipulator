import PyTango
import os
from Device import Device

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
        pass

    def assignCoordinatesToDevices(self):
        pass
