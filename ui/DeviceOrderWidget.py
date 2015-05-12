import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
from src.TangoDeviceManager import TangoDeviceManager
from PyQt4.QtGui import QPushButton, QLabel, QGridLayout, QWidget, QLineEdit, QFileDialog, QScrollArea, QVBoxLayout
from PyQt4 import QtCore
from PyQt4.QtCore import QRect
from DeviceWidget import DeviceWidget
from src.Device import Device
from src.IconAssigner import IconAssigner

class DeviceOrderWidget(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.section = None
        self.deviceWidgets = list()
        self.setMinimumWidth(520)
        self.setMinimumHeight(600)
        self.iconAssigner = IconAssigner()

        self.setupLayout()
        self.setupScrollArea()

        # self.addNewDeviceWidget(device = Device("ABC", None, None))
        # self.addNewDeviceWidget(device = Device("XD", None, None))
        # self.addNewDeviceWidget(device = Device("1313XD", None, None))
        # self.addNewDeviceWidget(device = Device(":-(", None, None))

    def setupLayout(self):
        self.containerWidget = QWidget(self)
        self.widgetHeight = 0
        self.containerWidget.setGeometry(QRect(0,0,451,self.widgetHeight))

        self.layout = QVBoxLayout()
        self.containerWidget.setLayout(self.layout)

    def setupScrollArea(self):
        self.scrollArea = QScrollArea(self)
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setMaximumWidth(530)
        self.scrollArea.setMinimumHeight(600)
        self.scrollArea.setWidgetResizable(False)
        self.scrollArea.setWidget(self.containerWidget)

    def setSection(self, section):
        self.section = section
        devices = section.devices
        devices = sorted(devices, key=lambda device: device.getShortName())
        for device in devices:
            self.addNewDeviceWidget(device)

    def addNewDeviceWidget(self, device=None):
        newWidget = DeviceWidget(self, device = device)
        newWidget.position = len(self.deviceWidgets)

        iconPath = self.iconAssigner.getIconPath(device)
        newWidget.deviceIcon.setIcon(iconPath)

        self.deviceWidgets.append(newWidget)
        self.layout.addWidget(newWidget)

        self.widgetHeight += 100
        self.containerWidget.resize(530, self.widgetHeight)

        self.connect(newWidget, QtCore.SIGNAL("up()"), self.upWidget)
        self.connect(newWidget, QtCore.SIGNAL("down()"), self.downWidget)

    def upWidget(self):
        widget = self.sender()
        if widget.position > 0:
            self.swap(widget.position, widget.position-1)

    def downWidget(self):
        widget = self.sender()
        if widget.position < len(self.deviceWidgets)-1:
            self.swap(widget.position, widget.position+1)

    def swap(self, first, second):
        firstWidget = self.deviceWidgets[first]
        secondWidget = self.deviceWidgets[second]

        firstWidget.position = second
        secondWidget.position = first

        self.layout.removeWidget(firstWidget)
        self.layout.removeWidget(secondWidget)
        self.deviceWidgets.remove(firstWidget)
        self.deviceWidgets.remove(secondWidget)
        if first > second:
            self.layout.insertWidget(second, firstWidget)
            self.layout.insertWidget(first, secondWidget)
            self.deviceWidgets.insert(second, firstWidget)
            self.deviceWidgets.insert(first, secondWidget)
        else:
            self.layout.insertWidget(first, secondWidget)
            self.layout.insertWidget(second, firstWidget)
            self.deviceWidgets.insert(first, secondWidget)
            self.deviceWidgets.insert(second, firstWidget)

    def getSortedDevices(self):
        devices = list()
        for deviceWidget in self.deviceWidgets:
            devices.append(deviceWidget.device)
        return devices