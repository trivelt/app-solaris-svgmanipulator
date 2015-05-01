from PyQt4.QtGui import QPushButton, QLabel, QGridLayout, QWidget
from PyQt4 import QtCore
from SettingsWidget import SettingsWidget

class FirstStepWidget(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.layout = QGridLayout()
        self.setLayout(self.layout)

        self.setMinimumHeight(667)
        self.setMinimumWidth(942)

        self.settingsWidget = SettingsWidget(self)
        self.layout.addWidget(self.settingsWidget, 1, 0)

        nextStepButton = QPushButton(self)
        nextStepButton.setText("Next step")
        nextStepButton.setStyleSheet("background-color:green;color:white;")
        self.layout.addWidget(nextStepButton, 0, 0, -1, 1, QtCore.Qt.AlignTop)

        self.connect(nextStepButton, QtCore.SIGNAL("clicked()"), QtCore.SIGNAL("nextStep()"))

    def saveSettings(self):
        self.settingsWidget.saveSettings()