from PyQt4.QtGui import QMainWindow, QPushButton, QLabel, QGridLayout, QWidget
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
#        self.setCentralWidget(self.secondStep)

        self.connect(self.firstStep, QtCore.SIGNAL("nextStep()"), self.showSecondStep)
        self.connect(self.secondStep, QtCore.SIGNAL("previousStep()"), self.showFirstStep)
        self.connect(self.secondStep, QtCore.SIGNAL("nextStep()"), self.showThirdStep)
        self.connect(self.thirdStep, QtCore.SIGNAL("previousStep()"), self.showSecondStep)

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