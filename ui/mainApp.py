import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
from src.SvgDrawer import SvgDrawer
from PyQt4.QtGui import QMainWindow, QApplication
from PyQt4 import QtCore
from SecondStepWidget import SecondStepWidget
from FirstStepWidget import FirstStepWidget
from SecondAndHalfStepWidget import SecondAndHalfStepWidget
from ThirdStepWidget import ThirdStepWidget
from SectionsDataProcessor import SectionsDataProcesssor
from SettingsWidget import SettingsCloud

class mainApp(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)

        self.firstStep = FirstStepWidget()
        self.secondStep = SecondStepWidget()
        self.secondAndHalfStep = SecondAndHalfStepWidget()
        self.thirdStep = ThirdStepWidget()
        self.setCentralWidget(self.firstStep)

        self.connect(self.firstStep, QtCore.SIGNAL("nextStep()"), self.showSecondStepAfterFirst)
        self.connect(self.secondStep, QtCore.SIGNAL("previousStep()"), self.showFirstStep)
        self.connect(self.secondStep, QtCore.SIGNAL("nextStep()"), self.showStepAfterSecond)
        self.connect(self.secondAndHalfStep, QtCore.SIGNAL("previousStep()"), self.showSecondStepAfterSecondAndHalf)
        self.connect(self.secondAndHalfStep, QtCore.SIGNAL("nextStep()"), self.showThirdStep)
        self.connect(self.thirdStep, QtCore.SIGNAL("previousStep()"), self.showStepBeforeThird)
        self.connect(self.thirdStep, QtCore.SIGNAL("loadDevices()"), self.loadDevices)

    def showSecondStepAfterFirst(self):
        self.firstStep.setParent(None)
        self.updateDefaultParameters()
        self.setCentralWidget(self.secondStep)

    def showFirstStep(self):
        self.secondStep.setParent(None)
        self.setCentralWidget(self.firstStep)

    def updateDefaultParameters(self):
        self.firstStep.saveSettings()

    def showStepAfterSecond(self):
        self.secondStep.setParent(None)
        if SettingsCloud.getParameter("parameterFromDb"):
            self.setCentralWidget(self.thirdStep)
        else:
            self.setCentralWidget(self.secondAndHalfStep)

    def showSecondStepAfterSecondAndHalf(self):
        self.secondAndHalfStep.setParent(None)
        self.setCentralWidget(self.secondStep)

    def showThirdStep(self):
        self.secondAndHalfStep.setParent(None)
        self.setCentralWidget(self.thirdStep)

    def showStepBeforeThird(self):
        self.thirdStep.setParent(None)
        if SettingsCloud.getParameter("parameterFromDb"):
            self.setCentralWidget(self.secondStep)
        else:
            self.setCentralWidget(self.secondAndHalfStep)

    def loadDevices(self):
        svgDrawer = SvgDrawer()
        svgDrawer.loadSvg(self.getBaseSvgPath())
        svgDrawer.setTangoHost(self.thirdStep.getTangoHost())

        self.processSectionsData(svgDrawer)

        svgDrawer.drawAll()

        destinationFile = self.thirdStep.getFilePath()
        svgDrawer.saveSvg(destinationFile)

    def getBaseSvgPath(self):
        currentFilePath = path.realpath(__file__)
        currentDirPath = path.dirname(currentFilePath)
        baseSvgPath = currentDirPath + "/../src/blank.svg"
        return baseSvgPath

    def processSectionsData(self, svgDrawer):
        dataProcessor = SectionsDataProcesssor(svgDrawer)
        linacSectionsData = self.secondStep.getLinacData()
        ringSectionsData = self.secondStep.getRingData()
        dataProcessor.processLinacSections(linacSectionsData)
        dataProcessor.processRingSections(ringSectionsData)
        dataProcessor.drawLastSectionIfNecessary()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mA = mainApp()
    mA.show()

    sys.exit(app.exec_())