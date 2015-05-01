from PyQt4.QtGui import QPushButton, QLabel, QGridLayout, QWidget
from PyQt4 import QtCore
from SectionWidget import SectionWidget

class SecondStepWidget(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.layout = QGridLayout()
        self.setLayout(self.layout)

        self.setupLabels()
        self.setupButtons()
        self.setupSectionWidgets()

        self.layout.setSpacing(0)

    def setupLabels(self):
        linacLabel = QLabel(self)
        linacLabel.setText("Linac sections")
        linacLabel.setAlignment(QtCore.Qt.AlignCenter)
        ringLabel = QLabel(self)
        ringLabel.setText(("Ring sections"))
        ringLabel.setAlignment(QtCore.Qt.AlignCenter)

        self.layout.addWidget(linacLabel, 1, 0)
        self.layout.addWidget(ringLabel, 1, 1)

    def setupButtons(self):
        previousStepButton = QPushButton(self)
        previousStepButton.setText("Previous step")
        previousStepButton.setStyleSheet("background-color:red;color:white;")

        nextStepButton = QPushButton(self)
        nextStepButton.setText("Next step")
        nextStepButton.setStyleSheet("background-color:green;color:white;")

        self.layout.addWidget(previousStepButton, 0, 0)
        self.layout.addWidget(nextStepButton, 0, 1)

        self.connect(previousStepButton, QtCore.SIGNAL("clicked()"), QtCore.SIGNAL("previousStep()"))
        self.connect(nextStepButton, QtCore.SIGNAL("clicked()"), QtCore.SIGNAL("nextStep()"))


    def setupSectionWidgets(self):
        self.linacSections = SectionWidget(self, True)
        self.ringSections = SectionWidget(self, False)

        self.layout.addWidget(self.linacSections, 2, 0, QtCore.Qt.AlignCenter)
        self.layout.addWidget(self.ringSections, 2, 1, QtCore.Qt.AlignCenter)

    def getLinacData(self):
        return self.linacSections.getSectionsData()

    def getRingData(self):
        return self.ringSections.getSectionsData()