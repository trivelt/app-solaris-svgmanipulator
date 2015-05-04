import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
from src.SvgDrawer import SvgDrawer
from PyQt4.QtGui import QMainWindow, QApplication
from PyQt4 import QtCore
from SecondStepWidget import SecondStepWidget
from FirstStepWidget import FirstStepWidget
from ThirdStepWidget import ThirdStepWidget
from SectionsDataProcessor import SectionsDataProcesssor

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