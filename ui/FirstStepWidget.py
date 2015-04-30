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

        #self.layout.setSpacing(0)

        settingsWidget = SettingsWidget(self)
        #settingsWidget.setMaximumWidth(300)
        self.layout.addWidget(settingsWidget, 1, 0)

        nextStepButton = QPushButton(self)
        nextStepButton.setText("Next step")
        nextStepButton.setStyleSheet("background-color:green;color:white;")
        self.layout.addWidget(nextStepButton, 0, 0, -1, 1, QtCore.Qt.AlignTop)




        self.connect(nextStepButton, QtCore.SIGNAL("clicked()"), QtCore.SIGNAL("nextStep()"))
