from PyQt4.QtGui import QPushButton, QLabel, QGridLayout, QWidget, QLineEdit, QFileDialog
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

        fileLocationLabel = QLabel(self)
        fileLocationLabel.setText("Save as: ")
        self.layout.addWidget(fileLocationLabel, 1, 0, QtCore.Qt.AlignTop)

        self.fileLocationEdit = QLineEdit(self)
        self.fileLocationEdit.setText("new.svg")
        self.layout.addWidget(self.fileLocationEdit, 1, 1, QtCore.Qt.AlignTop)

        chooseFileButton = QPushButton(self)
        chooseFileButton.setText("...")
        self.layout.addWidget(chooseFileButton, 1, 2, QtCore.Qt.AlignTop)
        self.connect(chooseFileButton, QtCore.SIGNAL("clicked()"), self.chooseFile)

        loadButton = QPushButton(self)
        loadButton.setText("Load devices and create SVG")
        self.layout.addWidget(loadButton, 2, 0, 1, -1, QtCore.Qt.AlignTop)
        self.connect(loadButton, QtCore.SIGNAL("clicked()"), QtCore.SIGNAL("loadDevices()"))

    def getFilePath(self):
        return str(self.fileLocationEdit.text())

    def chooseFile(self):
        fileChooser = QFileDialog()
        chooseFile = fileChooser.getSaveFileName()
        self.fileLocationEdit.setText(chooseFile)