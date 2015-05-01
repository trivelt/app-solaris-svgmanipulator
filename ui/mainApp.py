from src.SvgDrawer import SvgDrawer
from PyQt4.QtGui import QMainWindow
from PyQt4 import QtCore
from SecondStepWidget import SecondStepWidget
from FirstStepWidget import FirstStepWidget
from ThirdStepWidget import ThirdStepWidget

class mainApp(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)

        self.firstStep = FirstStepWidget()
        self.secondStep = SecondStepWidget()
        self.thirdStep = ThirdStepWidget()
        self.setCentralWidget(self.firstStep)

        self.connect(self.firstStep, QtCore.SIGNAL("nextStep()"), self.showSecondStepAfterFirst)
        self.connect(self.secondStep, QtCore.SIGNAL("previousStep()"), self.showFirstStep)
        self.connect(self.secondStep, QtCore.SIGNAL("nextStep()"), self.showThirdStep)
        self.connect(self.thirdStep, QtCore.SIGNAL("previousStep()"), self.showSecondStepAfterThird)
        self.connect(self.thirdStep, QtCore.SIGNAL("loadDevices()"), self.loadDevices)

    def showFirstStep(self):
        self.secondStep.setParent(None)
        self.setCentralWidget(self.firstStep)

    def showSecondStepAfterFirst(self):
        self.firstStep.setParent(None)
        self.updateDefaultParameters()
        self.setCentralWidget(self.secondStep)

    def updateDefaultParameters(self):
        self.firstStep.saveSettings()

    def showSecondStepAfterThird(self):
        self.thirdStep.setParent(None)
        self.setCentralWidget(self.secondStep)

    def showThirdStep(self):
        self.secondStep.setParent(None)
        self.setCentralWidget(self.thirdStep)

    def loadDevices(self):
        svgDrawer = SvgDrawer()
        svgDrawer.loadSvg("../src/blank.svg")
        self.processLinacSections(svgDrawer)
        self.processRingSections(svgDrawer)
        svgDrawer.drawAll()
        svgDrawer.saveSvg("../testImage.svg")
        print "Loading"

    def processLinacSections(self, svgDrawer):
        sectionsData = self.secondStep.getLinacData()
        for section in sectionsData:
            [name, color, sizeInPercent, displayedNameFlag, displayedName, subsectionsData] = self.processSectionsData(section)
            widthInPixels = sizeInPercent*7770.0
            svgDrawer.addSectionToLinac(name, color, widthInPixels)


    def processRingSections(self, svgDrawer):
        sectionsData = self.secondStep.getRingData()
        for section in sectionsData:
            [name, color, sizeInPercent, displayedNameFlag, displayedName, subsectionsData] = self.processSectionsData(section)

            angleInDegrees = sizeInPercent*360.0
            svgDrawer.addSectionToRing(name, color, angleInDegrees)

    def processSectionsData(self, sectionsData):
            subsectionsData = None
            if len(sectionsData) > 5:
                subsectionsData = sectionsData[5]
            name = str(sectionsData[0])
            sizeInPercent = float(str(sectionsData[1]).replace(",","."))/100.0
            color = str(sectionsData[2])
            displayedNameFlag = bool(sectionsData[3])
            displayedName = str(sectionsData[4])

            return [name, color, sizeInPercent, displayedNameFlag, displayedName, subsectionsData]