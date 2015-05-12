import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
from src.TangoDeviceManager import TangoDeviceManager
from src.Device import Device
from src.Icon import Icon
from PyQt4.QtGui import QPushButton, QLabel, QGridLayout, QWidget, QLineEdit, QFileDialog, QFrame
from PyQt4 import QtCore
from PyQt4.QtCore import QRect
from IconChooser import IconChooser

class DeviceWidget(QWidget):
    def __init__(self, parent=None, device=None):
        QWidget.__init__(self, parent)

        self.resize(500,70)

        self.upButton = QPushButton(self)
        self.upButton.setText("up")
        self.upButton.setStyleSheet("font-size:10px")
        self.upButton.setGeometry(QRect(5, 10, 42, 20))

        self.downButton = QPushButton(self)
        self.downButton.setText("down")
        self.downButton.setStyleSheet("font-size:10px")
        self.downButton.setGeometry(QRect(5, 30, 42, 20))

        self.deviceNameLabel = QLabel(self)
        self.deviceNameLabel.setText("DEViCE NAME")
        self.deviceNameLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.deviceNameLabel.setGeometry(QRect(55, 5, 350, 50))

        self.deviceIcon = IconChooser(self)
        self.deviceIcon.setGeometry(QRect(450, 15, 20, 20))
        self.deviceIcon.setIcon("/home/maciej/Pobrane/kits-maxiv-app-maxiv-linacsynoptic/linacsynoptic/images/icons/symbol-solenoid.svg")

        horizontalLine = QFrame(self)
        horizontalLine.setGeometry(60, 60, 380, 3)
        horizontalLine.setFrameShape(QFrame.HLine)
        horizontalLine.setFrameShadow(QFrame.Sunken)

        self.connect(self.upButton, QtCore.SIGNAL("clicked()"), QtCore.SIGNAL("up()"))
        self.connect(self.downButton, QtCore.SIGNAL("clicked()"), QtCore.SIGNAL("down()"))
        self.connect(self.deviceIcon, QtCore.SIGNAL("iconUpdated()"), self.changeDeviceIcon)

        self.position = -1
        self.device = None
        if device is not None:
            self.setDevice(device)

    def setDevice(self, device):
        self.device = device
        self.deviceNameLabel.setText(device.name)
        if device.icon is not None:
            self.deviceIcon.setIcon(device.icon.path)

    def changeDeviceIcon(self):
        iconPath = self.deviceIcon.getSelectedIcon()
        if self.device.icon is not None:
            self.device.icon.path = iconPath
        else:
            newIcon = Icon(iconPath)
            self.device.icon = newIcon