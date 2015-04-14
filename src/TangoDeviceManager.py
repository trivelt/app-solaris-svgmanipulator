import PyTango

class TangoDeviceManager:
    def __init__(self):
        self.database = PyTango.Database()

    def getDevices(self):
        self.servers = self.database.get_server_list()
        self.devices = []
        for server in self.servers:
            self.devices.append(self.database.get_device_class_list(server))
        return self.devices
