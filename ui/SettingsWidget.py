from PyQt4.QtGui import QPushButton, QLabel , QWidget, QLineEdit, QHBoxLayout, QVBoxLayout, QDoubleSpinBox
from PyQt4.QtCore import QRect, Qt
from ColorChooser import ColorChooser

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
        sectionColorLabel.setText("Section color:")
        self.sectionColorChooser = ColorChooser()
        self.sectionColorChooser.setMaximumWidth(100)
        self.putInHorizontalLayout(sectionColorLabel, self.sectionColorChooser)

        subsectionColorLabel = QLabel(self)
        subsectionColorLabel.setText("Subsection color: ")
        self.subsectionColorChooser = ColorChooser(self)
        self.subsectionColorChooser.setMaximumWidth(100)
        self.putInHorizontalLayout(subsectionColorLabel, self.subsectionColorChooser)

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
        centerCoordinatesLabel.setText("Real coordinates of ring center")
        self.centerCoordinatesEditX = QLineEdit()
        self.centerCoordinatesEditX.setPlaceholderText("X")
        self.centerCoordinatesEditX.setFixedWidth(80)
        self.centerCoordinatesEditY = QLineEdit()
        self.centerCoordinatesEditY.setPlaceholderText("Y")
        self.centerCoordinatesEditY.setFixedWidth(80)
        self.putInHorizontalLayout(centerCoordinatesLabel, self.centerCoordinatesEditX, self.centerCoordinatesEditY)


    def putInHorizontalLayout(self, label, edit, secondEdit=None):
        layout = QHBoxLayout()
        layout.addWidget(label, Qt.AlignLeft)
        layout.addWidget(edit, Qt.AlignRight)
        if secondEdit is not None:
            layout.addWidget(secondEdit)
        self.vLayout.addLayout(layout)
