import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
from src.TangoDeviceManager import TangoDeviceManager
from src.Linac import Linac
from src.Ring import Ring
from src.LinacSection import LinacSection
from src.ArcDrawingTools import ArcDrawingTools
from src.SvgDrawer import SvgDrawer
from PyQt4.QtGui import QPushButton, QLabel, QGridLayout, QWidget, QLineEdit
from PyQt4 import QtCore
from SectionsDataProcessor import SectionsDataProcesssor
from DeviceOrderWidget import DeviceOrderWidget

class SecondAndHalfStepWidget(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.layout = QGridLayout()
        self.setLayout(self.layout)
        self.deviceOrderWidgets = list()
        self.tDeviceManager = TangoDeviceManager()
        self.currentWidgetIndex = -1

        self.setMinimumHeight(667)
        self.setMinimumWidth(942)

        self.setupButtons()

    def setupButtons(self):
        previousStepButton = QPushButton(self)
        previousStepButton.setText("Previous step")
        previousStepButton.setStyleSheet("background-color:red;color:white;")
        previousStepButton.setFixedWidth(600)
        self.layout.addWidget(previousStepButton, 0, 0, QtCore.Qt.AlignHCenter)
        self.connect(previousStepButton, QtCore.SIGNAL("clicked()"), QtCore.SIGNAL("previousStep()"))

        nextStepButton = QPushButton(self)
        nextStepButton.setText("Next step")
        nextStepButton.setStyleSheet("background-color:green;color:white;")
        nextStepButton.setFixedWidth(500)
        self.layout.addWidget(nextStepButton, 0, 1, QtCore.Qt.AlignHCenter)
        self.connect(nextStepButton, QtCore.SIGNAL("clicked()"), self.saveSettingsBeforeNextStep)

        self.sectionLabel = QLabel(self)
        self.sectionLabel.setText("")
        self.sectionLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.layout.addWidget(self.sectionLabel, 1, 0, 1, -1, QtCore.Qt.AlignTop | QtCore.Qt.AlignHCenter)

        previousSectionButton = QPushButton(self)
        previousSectionButton.setText("Previous section")
        self.layout.addWidget(previousSectionButton, 2, 0)
        self.connect(previousSectionButton, QtCore.SIGNAL("clicked()"), self.previousSection)

        nextSectionButton = QPushButton(self)
        nextSectionButton.setText("Next section")
        self.layout.addWidget(nextSectionButton, 2, 1)
        self.connect(nextSectionButton, QtCore.SIGNAL("clicked()"), self.nextSection)

    def previousSection(self):
        if self.currentWidgetIndex > 0:
            self.changeWidget(-1)

    def nextSection(self):
        if self.currentWidgetIndex+1 < len(self.deviceOrderWidgets):
            self.changeWidget(1)

    def changeWidget(self, diff):
        self.layout.removeWidget(self.deviceOrderWidgets[self.currentWidgetIndex])
        self.deviceOrderWidgets[self.currentWidgetIndex].setVisible(False)
        self.currentWidgetIndex += diff
        self.layout.addWidget(self.deviceOrderWidgets[self.currentWidgetIndex], 3, 0, 1, -1, QtCore.Qt.AlignHCenter)
        self.deviceOrderWidgets[self.currentWidgetIndex].setVisible(True)
        self.showSectionName()

    def showSectionName(self):
        sectionWidget = self.deviceOrderWidgets[self.currentWidgetIndex]
        sectionName = sectionWidget.section.longName
        labelString = "Section "
        labelString += sectionName
        self.sectionLabel.setText(labelString)

    def setSectionsData(self, linacData, ringData):
        self.svgDrawer = SvgDrawer()
        sectionsProcessor = SectionsDataProcesssor(self.svgDrawer)
        sectionsProcessor.processLinacSections(linacData)
        sectionsProcessor.processRingSections(ringData)
        self.sections = self.svgDrawer.getAllSections()

    def createDeviceWidgets(self):
        self.clearWidgets()
        devices = self.tDeviceManager.getDevicesWithoutParameters()
        self.svgDrawer.addDeviceToAccelerator(devices)
        for section in self.sections:
            widget =  DeviceOrderWidget()
            widget.setSection(section)
            widget.setVisible(False)
            self.deviceOrderWidgets.append(widget)
        if len(self.deviceOrderWidgets) > 0:
            self.currentWidgetIndex = 0
            self.deviceOrderWidgets[0].setVisible(True)
            self.layout.addWidget(self.deviceOrderWidgets[0], 3, 0, 1, -1, QtCore.Qt.AlignHCenter)
            self.showSectionName()

    def clearWidgets(self):
        for widget in self.deviceOrderWidgets:
            widget.setVisible(False)
            self.layout.removeWidget(widget)
            del widget
        del self.deviceOrderWidgets[:]

    def saveSettingsBeforeNextStep(self):
        linacSectionNumber = 1
        ringSectionNumber = 1
        for sectionOrderWidget in self.deviceOrderWidgets:
            if isinstance(sectionOrderWidget.section, LinacSection):
                self.processLinacSection(sectionOrderWidget, linacSectionNumber)
                linacSectionNumber += 1
            else:
                self.processRingSection(sectionOrderWidget, ringSectionNumber)
                ringSectionNumber += 1
        self.emit(QtCore.SIGNAL("nextStep()"))

    def processLinacSection(self, sectionOrderWidget, number):
        sortedDevices = sectionOrderWidget.getSortedDevices()
        yCoord = 0
        baseXCoord = number * 100
        deviceNumber = 1
        for device in sortedDevices:
            xCoord = baseXCoord + deviceNumber
            device.realCoordinates = [float(xCoord), float(yCoord)]
            self.tDeviceManager.putDeviceParametersIntoDb(device)
            deviceNumber += 1

    def processRingSection(self, sectionOrderWidget, number):
        sortedDevices = sectionOrderWidget.getSortedDevices()
        deviceNumber = 0
        baseAngle = (360.0 / len(self.deviceOrderWidgets)) * number
        for device in sortedDevices:
            angle = baseAngle + deviceNumber
            [xCoord, yCoord] = ArcDrawingTools.polarToCartesian(0, 0, 1, angle)
            device.realCoordinates = [float(xCoord), float(yCoord)]
            self.tDeviceManager.putDeviceParametersIntoDb(device)
            deviceNumber -= 1
