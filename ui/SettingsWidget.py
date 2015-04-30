from PyQt4.QtGui import QPushButton, QLabel, QGridLayout, QWidget, QLineEdit, QHBoxLayout, QVBoxLayout
from PyQt4.QtCore import QRect, Qt
from ColorChooser import ColorChooser

class SettingsWidget(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)

        #self.setStyleSheet("background-color:orange;")
        self.setFixedWidth(500)
        self.setFixedHeight(400)

        self.setStyleSheet("font-size:20px;")

        # self.settingsLabel = QLabel(self)
        # self.settingsLabel.setText("Default settings")
        # self.settingsLabel.setStyleSheet("font-size:25px;")

        self.vLayout = QVBoxLayout()
        self.setLayout(self.vLayout)

        settingsLabel = QLabel(self)
        settingsLabel.setText("Default settings")
        settingsLabel.setStyleSheet("font-size:25px;")
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
        self.linacSectionSizeEdit = QLineEdit(self)
        self.putInHorizontalLayout(linacSectionSizeLabel, self.linacSectionSizeEdit)

        linaccSubsectionSizeLabel = QLabel(self)
        linaccSubsectionSizeLabel.setText("Linac subsection size: ")
        self.linacSubsectionSizeEdit = QLineEdit(self)
        self.putInHorizontalLayout(linaccSubsectionSizeLabel, self.linacSubsectionSizeEdit)

        ringSectionSizeLabel = QLabel(self)
        ringSectionSizeLabel.setText("Ring section size: ")
        self.ringSectionSizeEdit = QLineEdit(self)
        self.putInHorizontalLayout(ringSectionSizeLabel, self.ringSectionSizeEdit)

        ringSubectionSizeLabel = QLabel(self)
        ringSubectionSizeLabel.setText("Ring subsection size: ")
        self.ringSubsectionSizeEdit = QLineEdit(self)
        self.putInHorizontalLayout(ringSubectionSizeLabel, self.ringSubsectionSizeEdit)


        centerCoordinatesLabel = QLabel(self)
        centerCoordinatesLabel.setText("Real coordinates of ring center")
        self.centerCoordinatesEditX = QLineEdit()
        self.centerCoordinatesEditX.setPlaceholderText("X")
        self.centerCoordinatesEditY = QLineEdit()
        self.centerCoordinatesEditY.setPlaceholderText("Y")
        self.putInHorizontalLayout(centerCoordinatesLabel, self.centerCoordinatesEditX, self.centerCoordinatesEditY)


        # sectionColorLabel = QLabel(self)
        # sectionColorLabel.setText("Section color: ")
        # sectionColorLabel.setGeometry(QRect(5,20,125,100))
        # sectionColorChooser = ColorChooser(self)
        # sectionColorChooser.setGeometry(QRect(135,55,30,30))
        #
        # subsectionColorLabel = QLabel(self)
        # subsectionColorLabel.setText("Subsection color: ")
        # subsectionColorLabel.setGeometry(QRect(5,60,145,100))
        # subsectionColorChooser = ColorChooser(self)
        # subsectionColorChooser.setGeometry(QRect(155,95,30,30))
        #
        # linacSectionSizeLabel = QLabel(self)
        # linacSectionSizeLabel.setText("Linac section size: ")
        # linacSectionSizeLabel.setGeometry(QRect(5, 140, 160, 30))
        # linacSectionSizeEdit = QLineEdit(self)
        # linacSectionSizeEdit.setGeometry(QRect(170, 140, 50, 30))
        #
        # linacSectionSizeLabel = QLabel(self)
        # linacSectionSizeLabel.setText("Linac section size: ")
        # linacSectionSizeLabel.setGeometry(QRect(5, 140, 160, 30))
        # linacSectionSizeEdit = QLineEdit(self)
        # linacSectionSizeEdit.setGeometry(QRect(170, 140, 50, 30))


    def putInHorizontalLayout(self, label, edit, secondEdit=None):
        layout = QHBoxLayout()
        layout.addWidget(label)
        layout.addWidget(edit)
        if secondEdit is not None:
            layout.addWidget(secondEdit)
        self.vLayout.addLayout(layout)
