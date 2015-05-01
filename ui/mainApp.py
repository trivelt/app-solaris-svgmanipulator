from os import path
import sys
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
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

        self.secondStep.setVisible(False)
        self.thirdStep.setVisible(False)
        self.setCentralWidget(self.firstStep)

        self.connect(self.firstStep, QtCore.SIGNAL("nextStep()"), self.showSecondStep)
        self.connect(self.secondStep, QtCore.SIGNAL("previousStep()"), self.showFirstStep)
        self.connect(self.secondStep, QtCore.SIGNAL("nextStep()"), self.showThirdStep)
        self.connect(self.thirdStep, QtCore.SIGNAL("previousStep()"), self.showSecondStep)

        self.connect(self.thirdStep, QtCore.SIGNAL("loadDevices()"), self.loadDevices)

    def showFirstStep(self):
        self.firstStep.setVisible(True)
        self.secondStep.setVisible(False)

        self.secondStep.setParent(None)
        self.setCentralWidget(self.firstStep)

    def showSecondStep(self):
        self.firstStep.setVisible(False)
        self.secondStep.setVisible(True)
        self.firstStep.setParent(None)
        self.thirdStep.setParent(None)
        self.setCentralWidget(self.secondStep)

    def showThirdStep(self):
        self.thirdStep.setVisible(True)
        self.secondStep.setParent(None)
        self.setCentralWidget(self.thirdStep)

    def loadDevices(self):
        svgDrawer = SvgDrawer()
        svgDrawer.drawAll()
        svgDrawer.saveSvg("../testImage.svg")
        print "Loading"