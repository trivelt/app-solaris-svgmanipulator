import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
from PyQt4.QtGui import QPushButton, QLabel , QWidget, QLineEdit, QHBoxLayout, QVBoxLayout, QDoubleSpinBox, QCheckBox
from PyQt4.QtCore import QRect, Qt
from ColorChooser import ColorChooser
from src.SettingsCloud import SettingsCloud

class SettingsWidget(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)

        self.setFixedWidth(500)
        self.setFixedHeight(400)
        self.setStyleSheet("font-size:20px;")

        self.vLayout = QVBoxLayout()
        self.setLayout(self.vLayout)

        settingsLabel = QLabel(self)
        settingsLabel.setText("Default settings")
        settingsLabel.setStyleSheet("font-size:25px;")
        settingsLabel.setFixedWidth(500)
        settingsLabel.setAlignment(Qt.AlignCenter)
        self.vLayout.addWidget(settingsLabel)

        sectionColorLabel = QLabel(self)
        sectionColorLabel.setText("Section colors:")
        self.sectionColorChooser = ColorChooser()
        self.sectionColorChooser.setMaximumWidth(50)
        self.sectionSecondColorChooser = ColorChooser()
        self.sectionSecondColorChooser.setMaximumWidth(50)
        self.putInHorizontalLayout(sectionColorLabel, self.sectionColorChooser, self.sectionSecondColorChooser)

        subsectionColorLabel = QLabel(self)
        subsectionColorLabel.setText("Subsection colors: ")
        self.subsectionColorChooser = ColorChooser(self)
        self.subsectionColorChooser.setMaximumWidth(50)
        self.subsectionSecondColorChooser = ColorChooser(self)
        self.subsectionSecondColorChooser.setMaximumWidth(50)
        self.putInHorizontalLayout(subsectionColorLabel, self.subsectionColorChooser, self.subsectionSecondColorChooser)

        linacSectionSizeLabel = QLabel(self)
        linacSectionSizeLabel.setText("Linac section size: ")
        self.linacSectionSizeSpinBox = QDoubleSpinBox(self)
        self.linacSectionSizeSpinBox.setFixedWidth(100)
        self.linacSectionSizeSpinBox.setMaximum(100.0)
        self.putInHorizontalLayout(linacSectionSizeLabel, self.linacSectionSizeSpinBox)

        linacSubsectionSizeLabel = QLabel(self)
        linacSubsectionSizeLabel.setText("Linac subsection size: ")
        self.linacSubsectionSizeSpinBox = QDoubleSpinBox(self)
        self.linacSubsectionSizeSpinBox.setFixedWidth(100)
        self.linacSubsectionSizeSpinBox.setMaximum(100.0)
        self.putInHorizontalLayout(linacSubsectionSizeLabel, self.linacSubsectionSizeSpinBox)

        ringSectionSizeLabel = QLabel(self)
        ringSectionSizeLabel.setText("Ring section size: ")
        self.ringSectionSizeSpinBox = QDoubleSpinBox(self)
        self.ringSectionSizeSpinBox.setFixedWidth(100)
        self.ringSectionSizeSpinBox.setMaximum(100.0)
        self.putInHorizontalLayout(ringSectionSizeLabel, self.ringSectionSizeSpinBox)

        ringSubectionSizeLabel = QLabel(self)
        ringSubectionSizeLabel.setText("Ring subsection size: ")
        self.ringSubsectionSizeSpinBox = QDoubleSpinBox(self)
        self.ringSubsectionSizeSpinBox.setFixedWidth(100)
        self.ringSubsectionSizeSpinBox.setMaximum(100.0)
        self.putInHorizontalLayout(ringSubectionSizeLabel, self.ringSubsectionSizeSpinBox)

        centerCoordinatesLabel = QLabel(self)
        centerCoordinatesLabel.setText("Real coordinates of ring center:")
        self.centerCoordinatesEditX = QLineEdit()
        self.centerCoordinatesEditX.setPlaceholderText("X")
        self.centerCoordinatesEditX.setFixedWidth(80)
        self.centerCoordinatesEditY = QLineEdit()
        self.centerCoordinatesEditY.setPlaceholderText("Y")
        self.centerCoordinatesEditY.setFixedWidth(80)
        self.putInHorizontalLayout(centerCoordinatesLabel, self.centerCoordinatesEditX, self.centerCoordinatesEditY)

        showDeviceCaptionsLabel = QLabel(self)
        showDeviceCaptionsLabel.setText("Show device captions:")
        showDeviceCaptionsLabel.setFixedWidth(500)
        self.showDeviceCaptionsCheckBox = QCheckBox(self)
        self.putInHorizontalLayout(showDeviceCaptionsLabel, self.showDeviceCaptionsCheckBox)

        useDbParametersLabel = QLabel(self)
        useDbParametersLabel.setText("Use parameters from database")
        useDbParametersLabel.setFixedWidth(500)
        self.useDbParametersCheckBox = QCheckBox(self)
        self.putInHorizontalLayout(useDbParametersLabel, self.useDbParametersCheckBox)

        self.setDefaultSettings()

    def putInHorizontalLayout(self, label, edit, secondEdit=None):
        layout = QHBoxLayout()
        layout.addWidget(label, Qt.AlignLeft)
        layout.addWidget(edit, Qt.AlignRight)
        if secondEdit is not None:
            layout.addWidget(secondEdit, Qt.AlignRight)
        self.vLayout.addLayout(layout)

    def setDefaultSettings(self):
        self.linacSectionSizeSpinBox.setValue(25)
        self.linacSubsectionSizeSpinBox.setValue(50)
        self.ringSectionSizeSpinBox.setValue(25)
        self.ringSubsectionSizeSpinBox.setValue(33.33)
        self.centerCoordinatesEditX.setText("300")
        self.centerCoordinatesEditY.setText("500")
        self.showDeviceCaptionsCheckBox.setChecked(True)
        self.useDbParametersCheckBox.setChecked(True)

    def saveSettings(self):
        sectionFirstColor = str(self.sectionColorChooser.getSelectedColor())
        sectionSecondColor = str(self.sectionSecondColorChooser.getSelectedColor())
        subsectionColor = str(self.subsectionColorChooser.getSelectedColor())
        subsectionSecondColor = str(self.subsectionSecondColorChooser.getSelectedColor())
        linacSectionSize = float(self.linacSectionSizeSpinBox.value())
        linacSubsectionSize = float(self.linacSubsectionSizeSpinBox.value())
        ringSectionSize = float(self.ringSectionSizeSpinBox.value())
        ringSubsectionSize = float(self.ringSubsectionSizeSpinBox.value())
        centerCoordinateX = float(self.centerCoordinatesEditX.text())
        centerCoordinateY = float(self.centerCoordinatesEditY.text())
        deviceCaptions = bool(self.showDeviceCaptionsCheckBox.isChecked())
        parametersFromDb = bool(self.useDbParametersCheckBox.isChecked())

        SettingsCloud.setParameter("sectionFirstColor", sectionFirstColor)
        SettingsCloud.setParameter("sectionSecondColor", sectionSecondColor)
        SettingsCloud.setParameter("subsectionFirstColor", subsectionColor)
        SettingsCloud.setParameter("subsectionSecondColor", subsectionSecondColor)
        SettingsCloud.setParameter("linacSectionSize", linacSectionSize)
        SettingsCloud.setParameter("linacSubsectionSize", linacSubsectionSize)
        SettingsCloud.setParameter("ringSectionSize", ringSectionSize)
        SettingsCloud.setParameter("ringSubsectionSize", ringSubsectionSize)
        SettingsCloud.setParameter("centerCoordinateX", centerCoordinateX)
        SettingsCloud.setParameter("centerCoordinateY", centerCoordinateY)
        SettingsCloud.setParameter("deviceCaptions", deviceCaptions)
        SettingsCloud.setParameter("parameterFromDb", parametersFromDb)
