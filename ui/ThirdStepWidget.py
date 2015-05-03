from PyQt4.QtGui import QPushButton, QLabel, QGridLayout, QWidget, QLineEdit
from PyQt4 import QtCore

class ThirdStepWidget(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.layout = QGridLayout()
        self.setLayout(self.layout)

        self.setMinimumHeight(667)
        self.setMinimumWidth(942)

        self.setupButtons()

    def setupButtons(self):
        previousStepButton = QPushButton(self)
        previousStepButton.setText("Previous step")
        previousStepButton.setStyleSheet("background-color:red;color:white;")
        previousStepButton.setFixedWidth(400)
        self.layout.addWidget(previousStepButton, 0, 0, -1, -1,QtCore.Qt.AlignTop | QtCore.Qt.AlignCenter)
        self.connect(previousStepButton, QtCore.SIGNAL("clicked()"), QtCore.SIGNAL("previousStep()"))

        tangoHostLabel = QLabel(self)
        tangoHostLabel.setText("Tango Host: ")
        self.layout.addWidget(tangoHostLabel, 1, 0, QtCore.Qt.AlignTop)

        self.tangoHostEdit = QLineEdit(self)
        self.tangoHostEdit.setText("127.0.0.1:10000")
        self.layout.addWidget(self.tangoHostEdit, 1, 1, QtCore.Qt.AlignTop)

        fileLocationLabel = QLabel(self)
        fileLocationLabel.setText("Save as: ")
        self.layout.addWidget(fileLocationLabel, 2, 0, QtCore.Qt.AlignTop)

        self.fileLocationEdit = QLineEdit(self)
        self.fileLocationEdit.setText("new.svg")
        self.layout.addWidget(self.fileLocationEdit, 2, 1, QtCore.Qt.AlignTop)

        loadButton = QPushButton(self)
        loadButton.setText("Load devices and create SVG")
        self.layout.addWidget(loadButton, 3,0, 1, -1, QtCore.Qt.AlignTop)
        self.connect(loadButton, QtCore.SIGNAL("clicked()"), QtCore.SIGNAL("loadDevices()"))

    def getFilePath(self):
        return str(self.fileLocationEdit.text())

    def getTangoHost(self):
        return str(self.tangoHostEdit.text())