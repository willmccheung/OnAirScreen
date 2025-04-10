# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settings.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QButtonGroup, QCheckBox, QComboBox,
    QDialog, QFormLayout, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QPlainTextEdit,
    QPushButton, QRadioButton, QSizePolicy, QSpacerItem,
    QSpinBox, QTabWidget, QTextBrowser, QVBoxLayout,
    QWidget)
import resources_rc

class Ui_Settings(object):
    def setupUi(self, Settings):
        if not Settings.objectName():
            Settings.setObjectName(u"Settings")
        Settings.resize(703, 846)
        Settings.setMinimumSize(QSize(640, 0))
        self.gridLayout = QGridLayout(Settings)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tabWidget = QTabWidget(Settings)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setEnabled(True)
        self.tabWidget.setTabPosition(QTabWidget.West)
        self.tabWidget.setDocumentMode(True)
        self.tab_general = QWidget()
        self.tab_general.setObjectName(u"tab_general")
        self.gridLayout_3 = QGridLayout(self.tab_general)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(10, 0, 0, 0)
        self.line = QFrame(self.tab_general)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_3.addWidget(self.line, 2, 0, 1, 1)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.LED1 = QCheckBox(self.tab_general)
        self.LED1.setObjectName(u"LED1")
        self.LED1.setEnabled(True)
        self.LED1.setChecked(True)

        self.verticalLayout_5.addWidget(self.LED1)

        self.LED1Text = QLineEdit(self.tab_general)
        self.LED1Text.setObjectName(u"LED1Text")
        self.LED1Text.setEnabled(True)
        self.LED1Text.setMinimumSize(QSize(0, 0))
        self.LED1Text.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.LED1Text)

        self.LED1Demo = QLabel(self.tab_general)
        self.LED1Demo.setObjectName(u"LED1Demo")
        self.LED1Demo.setMinimumSize(QSize(0, 50))
        font = QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.LED1Demo.setFont(font)
        self.LED1Demo.setAutoFillBackground(True)
        self.LED1Demo.setFrameShape(QFrame.StyledPanel)
        self.LED1Demo.setAlignment(Qt.AlignCenter)
        self.LED1Demo.setMargin(10)

        self.verticalLayout_5.addWidget(self.LED1Demo)

        self.LED1BGColor = QPushButton(self.tab_general)
        self.LED1BGColor.setObjectName(u"LED1BGColor")
        self.LED1BGColor.setEnabled(True)

        self.verticalLayout_5.addWidget(self.LED1BGColor)

        self.LED1FGColor = QPushButton(self.tab_general)
        self.LED1FGColor.setObjectName(u"LED1FGColor")
        self.LED1FGColor.setEnabled(True)

        self.verticalLayout_5.addWidget(self.LED1FGColor)

        self.LED1Autoflash = QCheckBox(self.tab_general)
        self.LED1Autoflash.setObjectName(u"LED1Autoflash")
        self.LED1Autoflash.setEnabled(True)

        self.verticalLayout_5.addWidget(self.LED1Autoflash)

        self.LED1Timedflash = QCheckBox(self.tab_general)
        self.LED1Timedflash.setObjectName(u"LED1Timedflash")
        self.LED1Timedflash.setEnabled(True)

        self.verticalLayout_5.addWidget(self.LED1Timedflash)


        self.horizontalLayout_5.addLayout(self.verticalLayout_5)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.LED2 = QCheckBox(self.tab_general)
        self.LED2.setObjectName(u"LED2")
        self.LED2.setEnabled(True)
        self.LED2.setChecked(True)

        self.verticalLayout_6.addWidget(self.LED2)

        self.LED2Text = QLineEdit(self.tab_general)
        self.LED2Text.setObjectName(u"LED2Text")
        self.LED2Text.setEnabled(True)
        self.LED2Text.setMinimumSize(QSize(0, 0))
        self.LED2Text.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.LED2Text)

        self.LED2Demo = QLabel(self.tab_general)
        self.LED2Demo.setObjectName(u"LED2Demo")
        self.LED2Demo.setMinimumSize(QSize(0, 50))
        self.LED2Demo.setFont(font)
        self.LED2Demo.setAutoFillBackground(True)
        self.LED2Demo.setFrameShape(QFrame.StyledPanel)
        self.LED2Demo.setAlignment(Qt.AlignCenter)
        self.LED2Demo.setMargin(10)

        self.verticalLayout_6.addWidget(self.LED2Demo)

        self.LED2BGColor = QPushButton(self.tab_general)
        self.LED2BGColor.setObjectName(u"LED2BGColor")
        self.LED2BGColor.setEnabled(True)

        self.verticalLayout_6.addWidget(self.LED2BGColor)

        self.LED2FGColor = QPushButton(self.tab_general)
        self.LED2FGColor.setObjectName(u"LED2FGColor")
        self.LED2FGColor.setEnabled(True)

        self.verticalLayout_6.addWidget(self.LED2FGColor)

        self.LED2Autoflash = QCheckBox(self.tab_general)
        self.LED2Autoflash.setObjectName(u"LED2Autoflash")
        self.LED2Autoflash.setEnabled(True)

        self.verticalLayout_6.addWidget(self.LED2Autoflash)

        self.LED2Timedflash = QCheckBox(self.tab_general)
        self.LED2Timedflash.setObjectName(u"LED2Timedflash")
        self.LED2Timedflash.setEnabled(True)

        self.verticalLayout_6.addWidget(self.LED2Timedflash)


        self.horizontalLayout_5.addLayout(self.verticalLayout_6)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.LED3 = QCheckBox(self.tab_general)
        self.LED3.setObjectName(u"LED3")
        self.LED3.setEnabled(True)
        self.LED3.setChecked(True)

        self.verticalLayout_7.addWidget(self.LED3)

        self.LED3Text = QLineEdit(self.tab_general)
        self.LED3Text.setObjectName(u"LED3Text")
        self.LED3Text.setEnabled(True)
        self.LED3Text.setMinimumSize(QSize(0, 0))
        self.LED3Text.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.LED3Text)

        self.LED3Demo = QLabel(self.tab_general)
        self.LED3Demo.setObjectName(u"LED3Demo")
        self.LED3Demo.setMinimumSize(QSize(0, 50))
        self.LED3Demo.setFont(font)
        self.LED3Demo.setAutoFillBackground(True)
        self.LED3Demo.setFrameShape(QFrame.StyledPanel)
        self.LED3Demo.setAlignment(Qt.AlignCenter)
        self.LED3Demo.setMargin(10)

        self.verticalLayout_7.addWidget(self.LED3Demo)

        self.LED3BGColor = QPushButton(self.tab_general)
        self.LED3BGColor.setObjectName(u"LED3BGColor")
        self.LED3BGColor.setEnabled(True)

        self.verticalLayout_7.addWidget(self.LED3BGColor)

        self.LED3FGColor = QPushButton(self.tab_general)
        self.LED3FGColor.setObjectName(u"LED3FGColor")
        self.LED3FGColor.setEnabled(True)

        self.verticalLayout_7.addWidget(self.LED3FGColor)

        self.LED3Autoflash = QCheckBox(self.tab_general)
        self.LED3Autoflash.setObjectName(u"LED3Autoflash")
        self.LED3Autoflash.setEnabled(True)

        self.verticalLayout_7.addWidget(self.LED3Autoflash)

        self.LED3Timedflash = QCheckBox(self.tab_general)
        self.LED3Timedflash.setObjectName(u"LED3Timedflash")
        self.LED3Timedflash.setEnabled(True)

        self.verticalLayout_7.addWidget(self.LED3Timedflash)


        self.horizontalLayout_5.addLayout(self.verticalLayout_7)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.LED4 = QCheckBox(self.tab_general)
        self.LED4.setObjectName(u"LED4")
        self.LED4.setEnabled(True)
        self.LED4.setChecked(True)

        self.verticalLayout_8.addWidget(self.LED4)

        self.LED4Text = QLineEdit(self.tab_general)
        self.LED4Text.setObjectName(u"LED4Text")
        self.LED4Text.setEnabled(True)
        self.LED4Text.setMinimumSize(QSize(0, 0))
        self.LED4Text.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.LED4Text)

        self.LED4Demo = QLabel(self.tab_general)
        self.LED4Demo.setObjectName(u"LED4Demo")
        self.LED4Demo.setMinimumSize(QSize(0, 50))
        self.LED4Demo.setFont(font)
        self.LED4Demo.setAutoFillBackground(True)
        self.LED4Demo.setFrameShape(QFrame.StyledPanel)
        self.LED4Demo.setAlignment(Qt.AlignCenter)
        self.LED4Demo.setMargin(10)

        self.verticalLayout_8.addWidget(self.LED4Demo)

        self.LED4BGColor = QPushButton(self.tab_general)
        self.LED4BGColor.setObjectName(u"LED4BGColor")
        self.LED4BGColor.setEnabled(True)

        self.verticalLayout_8.addWidget(self.LED4BGColor)

        self.LED4FGColor = QPushButton(self.tab_general)
        self.LED4FGColor.setObjectName(u"LED4FGColor")
        self.LED4FGColor.setEnabled(True)

        self.verticalLayout_8.addWidget(self.LED4FGColor)

        self.LED4Autoflash = QCheckBox(self.tab_general)
        self.LED4Autoflash.setObjectName(u"LED4Autoflash")
        self.LED4Autoflash.setEnabled(True)

        self.verticalLayout_8.addWidget(self.LED4Autoflash)

        self.LED4Timedflash = QCheckBox(self.tab_general)
        self.LED4Timedflash.setObjectName(u"LED4Timedflash")
        self.LED4Timedflash.setEnabled(True)

        self.verticalLayout_8.addWidget(self.LED4Timedflash)


        self.horizontalLayout_5.addLayout(self.verticalLayout_8)


        self.gridLayout_3.addLayout(self.horizontalLayout_5, 3, 0, 1, 1)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.tab_general)
        self.label.setObjectName(u"label")
        self.label.setEnabled(True)

        self.verticalLayout.addWidget(self.label)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.StationName = QLineEdit(self.tab_general)
        self.StationName.setObjectName(u"StationName")
        self.StationName.setEnabled(True)

        self.horizontalLayout_2.addWidget(self.StationName)

        self.StationNameColor = QPushButton(self.tab_general)
        self.StationNameColor.setObjectName(u"StationNameColor")
        self.StationNameColor.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.StationNameColor.sizePolicy().hasHeightForWidth())
        self.StationNameColor.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.StationNameColor)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(self.tab_general)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setEnabled(True)

        self.verticalLayout_2.addWidget(self.label_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.Slogan = QLineEdit(self.tab_general)
        self.Slogan.setObjectName(u"Slogan")
        self.Slogan.setEnabled(True)

        self.horizontalLayout_3.addWidget(self.Slogan)

        self.SloganColor = QPushButton(self.tab_general)
        self.SloganColor.setObjectName(u"SloganColor")
        self.SloganColor.setEnabled(True)
        sizePolicy.setHeightForWidth(self.SloganColor.sizePolicy().hasHeightForWidth())
        self.SloganColor.setSizePolicy(sizePolicy)

        self.horizontalLayout_3.addWidget(self.SloganColor)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.nameDemoLayout = QVBoxLayout()
        self.nameDemoLayout.setSpacing(0)
        self.nameDemoLayout.setObjectName(u"nameDemoLayout")
        self.StationNameDemo = QLabel(self.tab_general)
        self.StationNameDemo.setObjectName(u"StationNameDemo")
        self.StationNameDemo.setMinimumSize(QSize(0, 30))
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush)
        brush1 = QBrush(QColor(0, 0, 0, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        brush2 = QBrush(QColor(128, 128, 128, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        self.StationNameDemo.setPalette(palette)
        font1 = QFont()
        font1.setPointSize(19)
        font1.setBold(True)
        self.StationNameDemo.setFont(font1)
        self.StationNameDemo.setAutoFillBackground(True)
        self.StationNameDemo.setAlignment(Qt.AlignCenter)

        self.nameDemoLayout.addWidget(self.StationNameDemo)

        self.SloganDemo = QLabel(self.tab_general)
        self.SloganDemo.setObjectName(u"SloganDemo")
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        self.SloganDemo.setPalette(palette1)
        self.SloganDemo.setFont(font)
        self.SloganDemo.setAutoFillBackground(True)
        self.SloganDemo.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.SloganDemo.setWordWrap(False)
        self.SloganDemo.setMargin(4)

        self.nameDemoLayout.addWidget(self.SloganDemo)


        self.verticalLayout_3.addLayout(self.nameDemoLayout)


        self.horizontalLayout_7.addLayout(self.verticalLayout_3)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_5 = QLabel(self.tab_general)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_9.addWidget(self.label_5)

        self.LEDInactive = QLabel(self.tab_general)
        self.LEDInactive.setObjectName(u"LEDInactive")
        self.LEDInactive.setMinimumSize(QSize(0, 50))
        self.LEDInactive.setFont(font)
        self.LEDInactive.setAutoFillBackground(True)
        self.LEDInactive.setFrameShape(QFrame.StyledPanel)
        self.LEDInactive.setAlignment(Qt.AlignCenter)
        self.LEDInactive.setMargin(10)

        self.verticalLayout_9.addWidget(self.LEDInactive)

        self.LEDInactiveBGColor = QPushButton(self.tab_general)
        self.LEDInactiveBGColor.setObjectName(u"LEDInactiveBGColor")

        self.verticalLayout_9.addWidget(self.LEDInactiveBGColor)

        self.LEDInactiveFGColor = QPushButton(self.tab_general)
        self.LEDInactiveFGColor.setObjectName(u"LEDInactiveFGColor")

        self.verticalLayout_9.addWidget(self.LEDInactiveFGColor)

        self.LEDFont = QPushButton(self.tab_general)
        self.LEDFont.setObjectName(u"LEDFont")

        self.verticalLayout_9.addWidget(self.LEDFont)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer_5)


        self.horizontalLayout_7.addLayout(self.verticalLayout_9)

        self.horizontalLayout_7.setStretch(0, 2)
        self.horizontalLayout_7.setStretch(1, 1)

        self.gridLayout_3.addLayout(self.horizontalLayout_7, 0, 0, 1, 1)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.checkBox_NTPCheck = QCheckBox(self.tab_general)
        self.checkBox_NTPCheck.setObjectName(u"checkBox_NTPCheck")
        self.checkBox_NTPCheck.setChecked(True)

        self.verticalLayout_4.addWidget(self.checkBox_NTPCheck)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_16 = QLabel(self.tab_general)
        self.label_16.setObjectName(u"label_16")

        self.horizontalLayout_12.addWidget(self.label_16)

        self.NTPCheckServer = QLineEdit(self.tab_general)
        self.NTPCheckServer.setObjectName(u"NTPCheckServer")

        self.horizontalLayout_12.addWidget(self.NTPCheckServer)


        self.verticalLayout_4.addLayout(self.horizontalLayout_12)

        self.label_17 = QLabel(self.tab_general)
        self.label_17.setObjectName(u"label_17")

        self.verticalLayout_4.addWidget(self.label_17)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setSpacing(4)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.logoPath = QLineEdit(self.tab_general)
        self.logoPath.setObjectName(u"logoPath")

        self.horizontalLayout_13.addWidget(self.logoPath)

        self.logoButton = QPushButton(self.tab_general)
        self.logoButton.setObjectName(u"logoButton")

        self.horizontalLayout_13.addWidget(self.logoButton)

        self.resetLogoButton = QPushButton(self.tab_general)
        self.resetLogoButton.setObjectName(u"resetLogoButton")

        self.horizontalLayout_13.addWidget(self.resetLogoButton)


        self.verticalLayout_4.addLayout(self.horizontalLayout_13)

        self.radioButton_logo_upper = QRadioButton(self.tab_general)
        self.buttonGroup_logo_position = QButtonGroup(Settings)
        self.buttonGroup_logo_position.setObjectName(u"buttonGroup_logo_position")
        self.buttonGroup_logo_position.addButton(self.radioButton_logo_upper)
        self.radioButton_logo_upper.setObjectName(u"radioButton_logo_upper")

        self.verticalLayout_4.addWidget(self.radioButton_logo_upper)

        self.radioButton_logo_lower = QRadioButton(self.tab_general)
        self.buttonGroup_logo_position.addButton(self.radioButton_logo_lower)
        self.radioButton_logo_lower.setObjectName(u"radioButton_logo_lower")
        self.radioButton_logo_lower.setChecked(True)

        self.verticalLayout_4.addWidget(self.radioButton_logo_lower)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.verticalLayout_20 = QVBoxLayout()
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.checkBox_UpdateCheck = QCheckBox(self.tab_general)
        self.checkBox_UpdateCheck.setObjectName(u"checkBox_UpdateCheck")
        self.checkBox_UpdateCheck.setChecked(False)

        self.verticalLayout_20.addWidget(self.checkBox_UpdateCheck)

        self.checkBox_IncludeBetaVersions = QCheckBox(self.tab_general)
        self.checkBox_IncludeBetaVersions.setObjectName(u"checkBox_IncludeBetaVersions")
        self.checkBox_IncludeBetaVersions.setEnabled(False)

        self.verticalLayout_20.addWidget(self.checkBox_IncludeBetaVersions)


        self.horizontalLayout_16.addLayout(self.verticalLayout_20)

        self.updateCheckNowButton = QPushButton(self.tab_general)
        self.updateCheckNowButton.setObjectName(u"updateCheckNowButton")
        self.updateCheckNowButton.setEnabled(False)

        self.horizontalLayout_16.addWidget(self.updateCheckNowButton)


        self.verticalLayout_4.addLayout(self.horizontalLayout_16)

        self.updateKey = QLineEdit(self.tab_general)
        self.updateKey.setObjectName(u"updateKey")
        self.updateKey.setEnabled(False)

        self.verticalLayout_4.addWidget(self.updateKey)

        self.label_28 = QLabel(self.tab_general)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setEnabled(False)
        self.label_28.setWordWrap(True)

        self.verticalLayout_4.addWidget(self.label_28)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_4)


        self.horizontalLayout_8.addLayout(self.verticalLayout_4)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_11 = QLabel(self.tab_general)
        self.label_11.setObjectName(u"label_11")

        self.verticalLayout_10.addWidget(self.label_11)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.clockDigital = QRadioButton(self.tab_general)
        self.buttonGroup_clock_mode = QButtonGroup(Settings)
        self.buttonGroup_clock_mode.setObjectName(u"buttonGroup_clock_mode")
        self.buttonGroup_clock_mode.addButton(self.clockDigital)
        self.clockDigital.setObjectName(u"clockDigital")
        self.clockDigital.setChecked(True)

        self.horizontalLayout_9.addWidget(self.clockDigital)

        self.clockAnalog = QRadioButton(self.tab_general)
        self.buttonGroup_clock_mode.addButton(self.clockAnalog)
        self.clockAnalog.setObjectName(u"clockAnalog")

        self.horizontalLayout_9.addWidget(self.clockAnalog)


        self.verticalLayout_10.addLayout(self.horizontalLayout_9)

        self.digitalClockColorForm = QFormLayout()
        self.digitalClockColorForm.setObjectName(u"digitalClockColorForm")
        self.digitalClockColorForm.setFieldGrowthPolicy(QFormLayout.FieldsStayAtSizeHint)
        self.digitalClockColorForm.setLabelAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.digitalClockColorForm.setFormAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.digitalClockColorForm.setHorizontalSpacing(10)
        self.digitalClockColorForm.setVerticalSpacing(2)
        self.hoursLEDsLabel = QLabel(self.tab_general)
        self.hoursLEDsLabel.setObjectName(u"hoursLEDsLabel")

        self.digitalClockColorForm.setWidget(0, QFormLayout.LabelRole, self.hoursLEDsLabel)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(6)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.DigitalHourColor = QFrame(self.tab_general)
        self.DigitalHourColor.setObjectName(u"DigitalHourColor")
        self.DigitalHourColor.setMinimumSize(QSize(20, 20))
        self.DigitalHourColor.setAutoFillBackground(True)
        self.DigitalHourColor.setFrameShape(QFrame.StyledPanel)
        self.DigitalHourColor.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_6.addWidget(self.DigitalHourColor)

        self.DigitalHourColorButton = QPushButton(self.tab_general)
        self.DigitalHourColorButton.setObjectName(u"DigitalHourColorButton")

        self.horizontalLayout_6.addWidget(self.DigitalHourColorButton)


        self.digitalClockColorForm.setLayout(0, QFormLayout.FieldRole, self.horizontalLayout_6)

        self.secondsLEDsLabel = QLabel(self.tab_general)
        self.secondsLEDsLabel.setObjectName(u"secondsLEDsLabel")

        self.digitalClockColorForm.setWidget(2, QFormLayout.LabelRole, self.secondsLEDsLabel)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setSpacing(6)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.DigitalSecondColor = QFrame(self.tab_general)
        self.DigitalSecondColor.setObjectName(u"DigitalSecondColor")
        self.DigitalSecondColor.setMinimumSize(QSize(20, 20))
        self.DigitalSecondColor.setAutoFillBackground(True)
        self.DigitalSecondColor.setFrameShape(QFrame.StyledPanel)
        self.DigitalSecondColor.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_10.addWidget(self.DigitalSecondColor)

        self.DigitalSecondColorButton = QPushButton(self.tab_general)
        self.DigitalSecondColorButton.setObjectName(u"DigitalSecondColorButton")

        self.horizontalLayout_10.addWidget(self.DigitalSecondColorButton)


        self.digitalClockColorForm.setLayout(2, QFormLayout.FieldRole, self.horizontalLayout_10)

        self.digitsLEDsLabel = QLabel(self.tab_general)
        self.digitsLEDsLabel.setObjectName(u"digitsLEDsLabel")

        self.digitalClockColorForm.setWidget(3, QFormLayout.LabelRole, self.digitsLEDsLabel)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setSpacing(6)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.DigitalDigitColor = QFrame(self.tab_general)
        self.DigitalDigitColor.setObjectName(u"DigitalDigitColor")
        self.DigitalDigitColor.setMinimumSize(QSize(20, 20))
        self.DigitalDigitColor.setAutoFillBackground(True)
        self.DigitalDigitColor.setFrameShape(QFrame.StyledPanel)
        self.DigitalDigitColor.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_11.addWidget(self.DigitalDigitColor)

        self.DigitalDigitColorButton = QPushButton(self.tab_general)
        self.DigitalDigitColorButton.setObjectName(u"DigitalDigitColorButton")

        self.horizontalLayout_11.addWidget(self.DigitalDigitColorButton)


        self.digitalClockColorForm.setLayout(3, QFormLayout.FieldRole, self.horizontalLayout_11)


        self.verticalLayout_10.addLayout(self.digitalClockColorForm)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.verticalLayout_21 = QVBoxLayout()
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.showSeconds = QCheckBox(self.tab_general)
        self.showSeconds.setObjectName(u"showSeconds")
        self.showSeconds.setChecked(True)

        self.verticalLayout_21.addWidget(self.showSeconds)

        self.verticalLayout_28 = QVBoxLayout()
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(18, -1, -1, -1)
        self.seconds_separate = QRadioButton(self.tab_general)
        self.buttonGroup_show_seconds = QButtonGroup(Settings)
        self.buttonGroup_show_seconds.setObjectName(u"buttonGroup_show_seconds")
        self.buttonGroup_show_seconds.addButton(self.seconds_separate)
        self.seconds_separate.setObjectName(u"seconds_separate")
        self.seconds_separate.setChecked(True)

        self.verticalLayout_28.addWidget(self.seconds_separate)

        self.seconds_in_one_line = QRadioButton(self.tab_general)
        self.buttonGroup_show_seconds.addButton(self.seconds_in_one_line)
        self.seconds_in_one_line.setObjectName(u"seconds_in_one_line")

        self.verticalLayout_28.addWidget(self.seconds_in_one_line)


        self.verticalLayout_21.addLayout(self.verticalLayout_28)

        self.staticColon = QCheckBox(self.tab_general)
        self.staticColon.setObjectName(u"staticColon")

        self.verticalLayout_21.addWidget(self.staticColon)

        self.useTextclock = QCheckBox(self.tab_general)
        self.useTextclock.setObjectName(u"useTextclock")

        self.verticalLayout_21.addWidget(self.useTextclock)


        self.horizontalLayout_17.addLayout(self.verticalLayout_21)

        self.verticalLayout_22 = QVBoxLayout()
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.replaceNOW = QCheckBox(self.tab_general)
        self.replaceNOW.setObjectName(u"replaceNOW")
        self.replaceNOW.setChecked(True)

        self.verticalLayout_22.addWidget(self.replaceNOW)

        self.replaceNOWText = QLineEdit(self.tab_general)
        self.replaceNOWText.setObjectName(u"replaceNOWText")

        self.verticalLayout_22.addWidget(self.replaceNOWText)

        self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_22.addItem(self.verticalSpacer_10)


        self.horizontalLayout_17.addLayout(self.verticalLayout_22)


        self.verticalLayout_10.addLayout(self.horizontalLayout_17)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_10.addItem(self.verticalSpacer_7)


        self.horizontalLayout_8.addLayout(self.verticalLayout_10)


        self.gridLayout_3.addLayout(self.horizontalLayout_8, 1, 0, 1, 1)

        self.tabWidget.addTab(self.tab_general, "")
        self.tab_advanced = QWidget()
        self.tab_advanced.setObjectName(u"tab_advanced")
        self.gridLayout_2 = QGridLayout(self.tab_advanced)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(10, 0, 0, 0)
        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.label_10 = QLabel(self.tab_advanced)
        self.label_10.setObjectName(u"label_10")

        self.verticalLayout_15.addWidget(self.label_10)

        self.dateFormat = QLineEdit(self.tab_advanced)
        self.dateFormat.setObjectName(u"dateFormat")

        self.verticalLayout_15.addWidget(self.dateFormat)

        self.textBrowser_2 = QTextBrowser(self.tab_advanced)
        self.textBrowser_2.setObjectName(u"textBrowser_2")
        self.textBrowser_2.setAcceptDrops(False)
        self.textBrowser_2.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)

        self.verticalLayout_15.addWidget(self.textBrowser_2)


        self.gridLayout_2.addLayout(self.verticalLayout_15, 1, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 7, 0, 1, 1)

        self.verticalLayout_17 = QVBoxLayout()
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.label_22 = QLabel(self.tab_advanced)
        self.label_22.setObjectName(u"label_22")

        self.verticalLayout_17.addWidget(self.label_22)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.time_24h = QRadioButton(self.tab_advanced)
        self.time_24h.setObjectName(u"time_24h")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.time_24h.sizePolicy().hasHeightForWidth())
        self.time_24h.setSizePolicy(sizePolicy1)
        self.time_24h.setChecked(True)

        self.horizontalLayout.addWidget(self.time_24h)

        self.time_am_pm = QRadioButton(self.tab_advanced)
        self.time_am_pm.setObjectName(u"time_am_pm")

        self.horizontalLayout.addWidget(self.time_am_pm)


        self.verticalLayout_17.addLayout(self.horizontalLayout)


        self.gridLayout_2.addLayout(self.verticalLayout_17, 3, 0, 1, 1)

        self.verticalLayout_18 = QVBoxLayout()
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_13 = QLabel(self.tab_advanced)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_15.addWidget(self.label_13)

        self.label_27 = QLabel(self.tab_advanced)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setTextFormat(Qt.AutoText)
        self.label_27.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_27.setOpenExternalLinks(True)
        self.label_27.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextSelectableByMouse)

        self.horizontalLayout_15.addWidget(self.label_27)


        self.verticalLayout_18.addLayout(self.horizontalLayout_15)

        self.owmWidgetEnabled = QCheckBox(self.tab_advanced)
        self.owmWidgetEnabled.setObjectName(u"owmWidgetEnabled")

        self.verticalLayout_18.addWidget(self.owmWidgetEnabled)

        self.owmLayout = QFormLayout()
        self.owmLayout.setObjectName(u"owmLayout")
        self.owmLayout.setLabelAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.owmLayout.setFormAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label_14 = QLabel(self.tab_advanced)
        self.label_14.setObjectName(u"label_14")

        self.owmLayout.setWidget(0, QFormLayout.LabelRole, self.label_14)

        self.owmAPIKey = QLineEdit(self.tab_advanced)
        self.owmAPIKey.setObjectName(u"owmAPIKey")
        self.owmAPIKey.setMinimumSize(QSize(300, 0))

        self.owmLayout.setWidget(0, QFormLayout.FieldRole, self.owmAPIKey)

        self.label_23 = QLabel(self.tab_advanced)
        self.label_23.setObjectName(u"label_23")

        self.owmLayout.setWidget(1, QFormLayout.LabelRole, self.label_23)

        self.owmCityID = QLineEdit(self.tab_advanced)
        self.owmCityID.setObjectName(u"owmCityID")

        self.owmLayout.setWidget(1, QFormLayout.FieldRole, self.owmCityID)

        self.label_24 = QLabel(self.tab_advanced)
        self.label_24.setObjectName(u"label_24")

        self.owmLayout.setWidget(2, QFormLayout.LabelRole, self.label_24)

        self.owmLanguage = QComboBox(self.tab_advanced)
        self.owmLanguage.addItem("")
        self.owmLanguage.setObjectName(u"owmLanguage")

        self.owmLayout.setWidget(2, QFormLayout.FieldRole, self.owmLanguage)

        self.owmTestAPI = QPushButton(self.tab_advanced)
        self.owmTestAPI.setObjectName(u"owmTestAPI")

        self.owmLayout.setWidget(4, QFormLayout.FieldRole, self.owmTestAPI)

        self.label_25 = QLabel(self.tab_advanced)
        self.label_25.setObjectName(u"label_25")

        self.owmLayout.setWidget(4, QFormLayout.LabelRole, self.label_25)

        self.label_26 = QLabel(self.tab_advanced)
        self.label_26.setObjectName(u"label_26")

        self.owmLayout.setWidget(3, QFormLayout.LabelRole, self.label_26)

        self.owmUnit = QComboBox(self.tab_advanced)
        self.owmUnit.addItem("")
        self.owmUnit.setObjectName(u"owmUnit")

        self.owmLayout.setWidget(3, QFormLayout.FieldRole, self.owmUnit)


        self.verticalLayout_18.addLayout(self.owmLayout)

        self.verticalLayout_19 = QVBoxLayout()
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.owmTestOutput = QPlainTextEdit(self.tab_advanced)
        self.owmTestOutput.setObjectName(u"owmTestOutput")
        self.owmTestOutput.setReadOnly(True)

        self.verticalLayout_19.addWidget(self.owmTestOutput)


        self.verticalLayout_18.addLayout(self.verticalLayout_19)


        self.gridLayout_2.addLayout(self.verticalLayout_18, 6, 0, 1, 1)

        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setLabelAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.formLayout_2.setFormAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label_15 = QLabel(self.tab_advanced)
        self.label_15.setObjectName(u"label_15")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_15)

        self.textClockLanguage = QComboBox(self.tab_advanced)
        self.textClockLanguage.addItem("")
        self.textClockLanguage.addItem("")
        self.textClockLanguage.addItem("")
        self.textClockLanguage.addItem("")
        self.textClockLanguage.setObjectName(u"textClockLanguage")
        sizePolicy1.setHeightForWidth(self.textClockLanguage.sizePolicy().hasHeightForWidth())
        self.textClockLanguage.setSizePolicy(sizePolicy1)

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.textClockLanguage)


        self.verticalLayout_16.addLayout(self.formLayout_2)


        self.gridLayout_2.addLayout(self.verticalLayout_16, 5, 0, 1, 1)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setLabelAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.formLayout.setFormAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label_4 = QLabel(self.tab_advanced)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_4)

        self.udpport = QLineEdit(self.tab_advanced)
        self.udpport.setObjectName(u"udpport")
        sizePolicy.setHeightForWidth(self.udpport.sizePolicy().hasHeightForWidth())
        self.udpport.setSizePolicy(sizePolicy)
        self.udpport.setMinimumSize(QSize(0, 0))

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.udpport)

        self.label_12 = QLabel(self.tab_advanced)
        self.label_12.setObjectName(u"label_12")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_12)

        self.httpport = QLineEdit(self.tab_advanced)
        self.httpport.setObjectName(u"httpport")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.httpport)

        self.label_40 = QLabel(self.tab_advanced)
        self.label_40.setObjectName(u"label_40")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_40)

        self.multicast_group = QLineEdit(self.tab_advanced)
        self.multicast_group.setObjectName(u"multicast_group")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.multicast_group)


        self.gridLayout_2.addLayout(self.formLayout, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_advanced, "")
        self.tab_timers = QWidget()
        self.tab_timers.setObjectName(u"tab_timers")
        self.verticalLayout_27 = QVBoxLayout(self.tab_timers)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(10, 0, 0, 0)
        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.verticalLayout_23 = QVBoxLayout()
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.enableAIR1 = QCheckBox(self.tab_timers)
        self.enableAIR1.setObjectName(u"enableAIR1")
        self.enableAIR1.setChecked(True)

        self.verticalLayout_23.addWidget(self.enableAIR1)

        self.AIR1Text = QLineEdit(self.tab_timers)
        self.AIR1Text.setObjectName(u"AIR1Text")
        self.AIR1Text.setAlignment(Qt.AlignCenter)

        self.verticalLayout_23.addWidget(self.AIR1Text)

        self.AIR1Demo = QLabel(self.tab_timers)
        self.AIR1Demo.setObjectName(u"AIR1Demo")
        self.AIR1Demo.setMinimumSize(QSize(0, 50))
        self.AIR1Demo.setFont(font)
        self.AIR1Demo.setAutoFillBackground(True)
        self.AIR1Demo.setFrameShape(QFrame.StyledPanel)
        self.AIR1Demo.setAlignment(Qt.AlignCenter)

        self.verticalLayout_23.addWidget(self.AIR1Demo)

        self.AIR1BGColor = QPushButton(self.tab_timers)
        self.AIR1BGColor.setObjectName(u"AIR1BGColor")

        self.verticalLayout_23.addWidget(self.AIR1BGColor)

        self.AIR1FGColor = QPushButton(self.tab_timers)
        self.AIR1FGColor.setObjectName(u"AIR1FGColor")

        self.verticalLayout_23.addWidget(self.AIR1FGColor)

        self.AIR1IconPath = QLineEdit(self.tab_timers)
        self.AIR1IconPath.setObjectName(u"AIR1IconPath")

        self.verticalLayout_23.addWidget(self.AIR1IconPath)

        self.AIR1IconSelectButton = QPushButton(self.tab_timers)
        self.AIR1IconSelectButton.setObjectName(u"AIR1IconSelectButton")

        self.verticalLayout_23.addWidget(self.AIR1IconSelectButton)

        self.AIR1IconResetButton = QPushButton(self.tab_timers)
        self.AIR1IconResetButton.setObjectName(u"AIR1IconResetButton")

        self.verticalLayout_23.addWidget(self.AIR1IconResetButton)


        self.horizontalLayout_18.addLayout(self.verticalLayout_23)

        self.verticalLayout_26 = QVBoxLayout()
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.enableAIR2 = QCheckBox(self.tab_timers)
        self.enableAIR2.setObjectName(u"enableAIR2")
        self.enableAIR2.setChecked(True)

        self.verticalLayout_26.addWidget(self.enableAIR2)

        self.AIR2Text = QLineEdit(self.tab_timers)
        self.AIR2Text.setObjectName(u"AIR2Text")
        self.AIR2Text.setAlignment(Qt.AlignCenter)

        self.verticalLayout_26.addWidget(self.AIR2Text)

        self.AIR2Demo = QLabel(self.tab_timers)
        self.AIR2Demo.setObjectName(u"AIR2Demo")
        self.AIR2Demo.setMinimumSize(QSize(0, 50))
        self.AIR2Demo.setFont(font)
        self.AIR2Demo.setAutoFillBackground(True)
        self.AIR2Demo.setFrameShape(QFrame.StyledPanel)
        self.AIR2Demo.setAlignment(Qt.AlignCenter)

        self.verticalLayout_26.addWidget(self.AIR2Demo)

        self.AIR2BGColor = QPushButton(self.tab_timers)
        self.AIR2BGColor.setObjectName(u"AIR2BGColor")

        self.verticalLayout_26.addWidget(self.AIR2BGColor)

        self.AIR2FGColor = QPushButton(self.tab_timers)
        self.AIR2FGColor.setObjectName(u"AIR2FGColor")

        self.verticalLayout_26.addWidget(self.AIR2FGColor)

        self.AIR2IconPath = QLineEdit(self.tab_timers)
        self.AIR2IconPath.setObjectName(u"AIR2IconPath")

        self.verticalLayout_26.addWidget(self.AIR2IconPath)

        self.AIR2IconSelectButton = QPushButton(self.tab_timers)
        self.AIR2IconSelectButton.setObjectName(u"AIR2IconSelectButton")

        self.verticalLayout_26.addWidget(self.AIR2IconSelectButton)

        self.AIR2IconResetButton = QPushButton(self.tab_timers)
        self.AIR2IconResetButton.setObjectName(u"AIR2IconResetButton")

        self.verticalLayout_26.addWidget(self.AIR2IconResetButton)


        self.horizontalLayout_18.addLayout(self.verticalLayout_26)

        self.verticalLayout_24 = QVBoxLayout()
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.enableAIR3 = QCheckBox(self.tab_timers)
        self.enableAIR3.setObjectName(u"enableAIR3")
        self.enableAIR3.setChecked(True)

        self.verticalLayout_24.addWidget(self.enableAIR3)

        self.AIR3Text = QLineEdit(self.tab_timers)
        self.AIR3Text.setObjectName(u"AIR3Text")
        self.AIR3Text.setAlignment(Qt.AlignCenter)

        self.verticalLayout_24.addWidget(self.AIR3Text)

        self.AIR3Demo = QLabel(self.tab_timers)
        self.AIR3Demo.setObjectName(u"AIR3Demo")
        self.AIR3Demo.setMinimumSize(QSize(0, 50))
        self.AIR3Demo.setFont(font)
        self.AIR3Demo.setAutoFillBackground(True)
        self.AIR3Demo.setFrameShape(QFrame.StyledPanel)
        self.AIR3Demo.setAlignment(Qt.AlignCenter)

        self.verticalLayout_24.addWidget(self.AIR3Demo)

        self.AIR3BGColor = QPushButton(self.tab_timers)
        self.AIR3BGColor.setObjectName(u"AIR3BGColor")

        self.verticalLayout_24.addWidget(self.AIR3BGColor)

        self.AIR3FGColor = QPushButton(self.tab_timers)
        self.AIR3FGColor.setObjectName(u"AIR3FGColor")

        self.verticalLayout_24.addWidget(self.AIR3FGColor)

        self.AIR3IconPath = QLineEdit(self.tab_timers)
        self.AIR3IconPath.setObjectName(u"AIR3IconPath")

        self.verticalLayout_24.addWidget(self.AIR3IconPath)

        self.AIR3IconSelectButton = QPushButton(self.tab_timers)
        self.AIR3IconSelectButton.setObjectName(u"AIR3IconSelectButton")

        self.verticalLayout_24.addWidget(self.AIR3IconSelectButton)

        self.AIR3IconResetButton = QPushButton(self.tab_timers)
        self.AIR3IconResetButton.setObjectName(u"AIR3IconResetButton")

        self.verticalLayout_24.addWidget(self.AIR3IconResetButton)


        self.horizontalLayout_18.addLayout(self.verticalLayout_24)

        self.verticalLayout_25 = QVBoxLayout()
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.enableAIR4 = QCheckBox(self.tab_timers)
        self.enableAIR4.setObjectName(u"enableAIR4")
        self.enableAIR4.setChecked(True)

        self.verticalLayout_25.addWidget(self.enableAIR4)

        self.AIR4Text = QLineEdit(self.tab_timers)
        self.AIR4Text.setObjectName(u"AIR4Text")
        self.AIR4Text.setAlignment(Qt.AlignCenter)

        self.verticalLayout_25.addWidget(self.AIR4Text)

        self.AIR4Demo = QLabel(self.tab_timers)
        self.AIR4Demo.setObjectName(u"AIR4Demo")
        self.AIR4Demo.setMinimumSize(QSize(0, 50))
        self.AIR4Demo.setFont(font)
        self.AIR4Demo.setAutoFillBackground(True)
        self.AIR4Demo.setFrameShape(QFrame.StyledPanel)
        self.AIR4Demo.setAlignment(Qt.AlignCenter)

        self.verticalLayout_25.addWidget(self.AIR4Demo)

        self.AIR4BGColor = QPushButton(self.tab_timers)
        self.AIR4BGColor.setObjectName(u"AIR4BGColor")

        self.verticalLayout_25.addWidget(self.AIR4BGColor)

        self.AIR4FGColor = QPushButton(self.tab_timers)
        self.AIR4FGColor.setObjectName(u"AIR4FGColor")

        self.verticalLayout_25.addWidget(self.AIR4FGColor)

        self.AIR4IconPath = QLineEdit(self.tab_timers)
        self.AIR4IconPath.setObjectName(u"AIR4IconPath")

        self.verticalLayout_25.addWidget(self.AIR4IconPath)

        self.AIR4IconSelectButton = QPushButton(self.tab_timers)
        self.AIR4IconSelectButton.setObjectName(u"AIR4IconSelectButton")

        self.verticalLayout_25.addWidget(self.AIR4IconSelectButton)

        self.AIR4IconResetButton = QPushButton(self.tab_timers)
        self.AIR4IconResetButton.setObjectName(u"AIR4IconResetButton")

        self.verticalLayout_25.addWidget(self.AIR4IconResetButton)


        self.horizontalLayout_18.addLayout(self.verticalLayout_25)


        self.verticalLayout_27.addLayout(self.horizontalLayout_18)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.label_39 = QLabel(self.tab_timers)
        self.label_39.setObjectName(u"label_39")

        self.horizontalLayout_19.addWidget(self.label_39)

        self.AIRMinWidth = QSpinBox(self.tab_timers)
        self.AIRMinWidth.setObjectName(u"AIRMinWidth")
        self.AIRMinWidth.setMinimum(200)
        self.AIRMinWidth.setMaximum(500)

        self.horizontalLayout_19.addWidget(self.AIRMinWidth)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_19.addItem(self.horizontalSpacer_4)


        self.verticalLayout_27.addLayout(self.horizontalLayout_19)

        self.line_2 = QFrame(self.tab_timers)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_27.addWidget(self.line_2)

        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_27.addItem(self.verticalSpacer_9)

        self.tabWidget.addTab(self.tab_timers, "")
        self.tab_fonts = QWidget()
        self.tab_fonts.setObjectName(u"tab_fonts")
        self.gridLayout_7 = QGridLayout(self.tab_fonts)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.label_38 = QLabel(self.tab_fonts)
        self.label_38.setObjectName(u"label_38")

        self.gridLayout_6.addWidget(self.label_38, 3, 0, 1, 1)

        self.label_29 = QLabel(self.tab_fonts)
        self.label_29.setObjectName(u"label_29")

        self.gridLayout_6.addWidget(self.label_29, 4, 0, 1, 1)

        self.label_35 = QLabel(self.tab_fonts)
        self.label_35.setObjectName(u"label_35")

        self.gridLayout_6.addWidget(self.label_35, 0, 0, 1, 1)

        self.label_32 = QLabel(self.tab_fonts)
        self.label_32.setObjectName(u"label_32")

        self.gridLayout_6.addWidget(self.label_32, 7, 0, 1, 1)

        self.label_34 = QLabel(self.tab_fonts)
        self.label_34.setObjectName(u"label_34")

        self.gridLayout_6.addWidget(self.label_34, 9, 0, 1, 1)

        self.label_30 = QLabel(self.tab_fonts)
        self.label_30.setObjectName(u"label_30")

        self.gridLayout_6.addWidget(self.label_30, 5, 0, 1, 1)

        self.label_33 = QLabel(self.tab_fonts)
        self.label_33.setObjectName(u"label_33")

        self.gridLayout_6.addWidget(self.label_33, 8, 0, 1, 1)

        self.label_36 = QLabel(self.tab_fonts)
        self.label_36.setObjectName(u"label_36")

        self.gridLayout_6.addWidget(self.label_36, 1, 0, 1, 1)

        self.label_31 = QLabel(self.tab_fonts)
        self.label_31.setObjectName(u"label_31")

        self.gridLayout_6.addWidget(self.label_31, 6, 0, 1, 1)

        self.ExampleFont_AIR1 = QLabel(self.tab_fonts)
        self.ExampleFont_AIR1.setObjectName(u"ExampleFont_AIR1")

        self.gridLayout_6.addWidget(self.ExampleFont_AIR1, 0, 1, 1, 1)

        self.ExampleFont_AIR2 = QLabel(self.tab_fonts)
        self.ExampleFont_AIR2.setObjectName(u"ExampleFont_AIR2")

        self.gridLayout_6.addWidget(self.ExampleFont_AIR2, 1, 1, 1, 1)

        self.label_37 = QLabel(self.tab_fonts)
        self.label_37.setObjectName(u"label_37")

        self.gridLayout_6.addWidget(self.label_37, 2, 0, 1, 1)

        self.ExampleFont_AIR3 = QLabel(self.tab_fonts)
        self.ExampleFont_AIR3.setObjectName(u"ExampleFont_AIR3")

        self.gridLayout_6.addWidget(self.ExampleFont_AIR3, 2, 1, 1, 1)

        self.ExampleFont_AIR4 = QLabel(self.tab_fonts)
        self.ExampleFont_AIR4.setObjectName(u"ExampleFont_AIR4")

        self.gridLayout_6.addWidget(self.ExampleFont_AIR4, 3, 1, 1, 1)

        self.ExampleFont_LED1 = QLabel(self.tab_fonts)
        self.ExampleFont_LED1.setObjectName(u"ExampleFont_LED1")

        self.gridLayout_6.addWidget(self.ExampleFont_LED1, 4, 1, 1, 1)

        self.ExampleFont_LED2 = QLabel(self.tab_fonts)
        self.ExampleFont_LED2.setObjectName(u"ExampleFont_LED2")

        self.gridLayout_6.addWidget(self.ExampleFont_LED2, 5, 1, 1, 1)

        self.ExampleFont_LED3 = QLabel(self.tab_fonts)
        self.ExampleFont_LED3.setObjectName(u"ExampleFont_LED3")

        self.gridLayout_6.addWidget(self.ExampleFont_LED3, 6, 1, 1, 1)

        self.ExampleFont_LED4 = QLabel(self.tab_fonts)
        self.ExampleFont_LED4.setObjectName(u"ExampleFont_LED4")

        self.gridLayout_6.addWidget(self.ExampleFont_LED4, 7, 1, 1, 1)

        self.ExampleFont_StationName = QLabel(self.tab_fonts)
        self.ExampleFont_StationName.setObjectName(u"ExampleFont_StationName")

        self.gridLayout_6.addWidget(self.ExampleFont_StationName, 8, 1, 1, 1)

        self.ExampleFont_Slogan = QLabel(self.tab_fonts)
        self.ExampleFont_Slogan.setObjectName(u"ExampleFont_Slogan")

        self.gridLayout_6.addWidget(self.ExampleFont_Slogan, 9, 1, 1, 1)

        self.SetFont_AIR3 = QPushButton(self.tab_fonts)
        self.SetFont_AIR3.setObjectName(u"SetFont_AIR3")

        self.gridLayout_6.addWidget(self.SetFont_AIR3, 2, 2, 1, 1)

        self.SetFont_AIR1 = QPushButton(self.tab_fonts)
        self.SetFont_AIR1.setObjectName(u"SetFont_AIR1")

        self.gridLayout_6.addWidget(self.SetFont_AIR1, 0, 2, 1, 1)

        self.SetFont_AIR2 = QPushButton(self.tab_fonts)
        self.SetFont_AIR2.setObjectName(u"SetFont_AIR2")

        self.gridLayout_6.addWidget(self.SetFont_AIR2, 1, 2, 1, 1)

        self.SetFont_AIR4 = QPushButton(self.tab_fonts)
        self.SetFont_AIR4.setObjectName(u"SetFont_AIR4")

        self.gridLayout_6.addWidget(self.SetFont_AIR4, 3, 2, 1, 1)

        self.SetFont_LED1 = QPushButton(self.tab_fonts)
        self.SetFont_LED1.setObjectName(u"SetFont_LED1")

        self.gridLayout_6.addWidget(self.SetFont_LED1, 4, 2, 1, 1)

        self.SetFont_LED2 = QPushButton(self.tab_fonts)
        self.SetFont_LED2.setObjectName(u"SetFont_LED2")

        self.gridLayout_6.addWidget(self.SetFont_LED2, 5, 2, 1, 1)

        self.SetFont_LED3 = QPushButton(self.tab_fonts)
        self.SetFont_LED3.setObjectName(u"SetFont_LED3")

        self.gridLayout_6.addWidget(self.SetFont_LED3, 6, 2, 1, 1)

        self.SetFont_LED4 = QPushButton(self.tab_fonts)
        self.SetFont_LED4.setObjectName(u"SetFont_LED4")

        self.gridLayout_6.addWidget(self.SetFont_LED4, 7, 2, 1, 1)

        self.SetFont_StationName = QPushButton(self.tab_fonts)
        self.SetFont_StationName.setObjectName(u"SetFont_StationName")

        self.gridLayout_6.addWidget(self.SetFont_StationName, 8, 2, 1, 1)

        self.SetFont_Slogan = QPushButton(self.tab_fonts)
        self.SetFont_Slogan.setObjectName(u"SetFont_Slogan")

        self.gridLayout_6.addWidget(self.SetFont_Slogan, 9, 2, 1, 1)

        self.gridLayout_6.setColumnStretch(0, 1)
        self.gridLayout_6.setColumnStretch(1, 4)
        self.gridLayout_6.setColumnStretch(2, 1)

        self.gridLayout_7.addLayout(self.gridLayout_6, 0, 1, 1, 1)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_7.addItem(self.verticalSpacer_8, 1, 1, 1, 1)

        self.tabWidget.addTab(self.tab_fonts, "")
        self.tab_about = QWidget()
        self.tab_about.setObjectName(u"tab_about")
        self.gridLayout_4 = QGridLayout(self.tab_about)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(10, 0, 0, 0)
        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_3, 5, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_2, 3, 0, 1, 1)

        self.label_6 = QLabel(self.tab_about)
        self.label_6.setObjectName(u"label_6")
        font2 = QFont()
        font2.setPointSize(24)
        font2.setBold(True)
        self.label_6.setFont(font2)
        self.label_6.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_6, 0, 0, 1, 1)

        self.versionLabel = QLabel(self.tab_about)
        self.versionLabel.setObjectName(u"versionLabel")
        self.versionLabel.setAlignment(Qt.AlignCenter)
        self.versionLabel.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextSelectableByKeyboard|Qt.TextSelectableByMouse)

        self.gridLayout_4.addWidget(self.versionLabel, 1, 0, 1, 1)

        self.label_8 = QLabel(self.tab_about)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setPixmap(QPixmap(u":/oas_icon_256/images/oas_icon_256.png"))
        self.label_8.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_8, 4, 0, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_3 = QLabel(self.tab_about)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_12.addWidget(self.label_3)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setSpacing(20)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setSpacing(4)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_18 = QLabel(self.tab_about)
        self.label_18.setObjectName(u"label_18")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_18.sizePolicy().hasHeightForWidth())
        self.label_18.setSizePolicy(sizePolicy2)
        self.label_18.setMinimumSize(QSize(50, 51))
        self.label_18.setMaximumSize(QSize(50, 51))
        self.label_18.setPixmap(QPixmap(u":/thirdparty/images/pyinstaller.png"))
        self.label_18.setScaledContents(True)

        self.verticalLayout_13.addWidget(self.label_18)

        self.label_20 = QLabel(self.tab_about)
        self.label_20.setObjectName(u"label_20")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_20.sizePolicy().hasHeightForWidth())
        self.label_20.setSizePolicy(sizePolicy3)
        font3 = QFont()
        font3.setPointSize(10)
        self.label_20.setFont(font3)
        self.label_20.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.verticalLayout_13.addWidget(self.label_20)


        self.horizontalLayout_14.addLayout(self.verticalLayout_13)

        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setSpacing(3)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_19 = QLabel(self.tab_about)
        self.label_19.setObjectName(u"label_19")
        sizePolicy2.setHeightForWidth(self.label_19.sizePolicy().hasHeightForWidth())
        self.label_19.setSizePolicy(sizePolicy2)
        self.label_19.setMinimumSize(QSize(50, 52))
        self.label_19.setMaximumSize(QSize(50, 52))
        self.label_19.setPixmap(QPixmap(u":/thirdparty/images/pyqt.png"))
        self.label_19.setScaledContents(True)

        self.verticalLayout_14.addWidget(self.label_19)

        self.label_21 = QLabel(self.tab_about)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setFont(font3)
        self.label_21.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.verticalLayout_14.addWidget(self.label_21)


        self.horizontalLayout_14.addLayout(self.verticalLayout_14)


        self.verticalLayout_12.addLayout(self.horizontalLayout_14)


        self.horizontalLayout_4.addLayout(self.verticalLayout_12)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)

        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_11.addItem(self.verticalSpacer_6)

        self.label_9 = QLabel(self.tab_about)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_11.addWidget(self.label_9)

        self.label_7 = QLabel(self.tab_about)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_11.addWidget(self.label_7)


        self.horizontalLayout_4.addLayout(self.verticalLayout_11)


        self.gridLayout_4.addLayout(self.horizontalLayout_4, 12, 0, 1, 1)

        self.ResetSettingsButton = QPushButton(self.tab_about)
        self.ResetSettingsButton.setObjectName(u"ResetSettingsButton")
        self.ResetSettingsButton.setEnabled(False)

        self.gridLayout_4.addWidget(self.ResetSettingsButton, 8, 0, 1, 1)

        self.enableResetButton = QCheckBox(self.tab_about)
        self.enableResetButton.setObjectName(u"enableResetButton")

        self.gridLayout_4.addWidget(self.enableResetButton, 7, 0, 1, 1)

        self.distributionLabel = QLabel(self.tab_about)
        self.distributionLabel.setObjectName(u"distributionLabel")
        self.distributionLabel.setAlignment(Qt.AlignCenter)
        self.distributionLabel.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextSelectableByKeyboard|Qt.TextSelectableByMouse)

        self.gridLayout_4.addWidget(self.distributionLabel, 2, 0, 1, 1)

        self.settingspathLabel = QLabel(self.tab_about)
        self.settingspathLabel.setObjectName(u"settingspathLabel")
        self.settingspathLabel.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextSelectableByKeyboard|Qt.TextSelectableByMouse)

        self.gridLayout_4.addWidget(self.settingspathLabel, 6, 0, 1, 1)

        self.tabWidget.addTab(self.tab_about, "")
        self.tab_license = QWidget()
        self.tab_license.setObjectName(u"tab_license")
        self.gridLayout_5 = QGridLayout(self.tab_license)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(10, 0, 0, 0)
        self.plainTextEdit = QPlainTextEdit(self.tab_license)
        self.plainTextEdit.setObjectName(u"plainTextEdit")

        self.gridLayout_5.addWidget(self.plainTextEdit, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_license, "")

        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)

        self.global_button_bar = QHBoxLayout()
        self.global_button_bar.setObjectName(u"global_button_bar")
        self.ExitButton = QPushButton(Settings)
        self.ExitButton.setObjectName(u"ExitButton")
        self.ExitButton.setEnabled(True)

        self.global_button_bar.addWidget(self.ExitButton)

        self.RebootButton = QPushButton(Settings)
        self.RebootButton.setObjectName(u"RebootButton")

        self.global_button_bar.addWidget(self.RebootButton)

        self.ShutdownButton = QPushButton(Settings)
        self.ShutdownButton.setObjectName(u"ShutdownButton")

        self.global_button_bar.addWidget(self.ShutdownButton)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.global_button_bar.addItem(self.horizontalSpacer_3)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.global_button_bar.addItem(self.horizontalSpacer)

        self.CloseButton = QPushButton(Settings)
        self.CloseButton.setObjectName(u"CloseButton")
        self.CloseButton.setEnabled(True)

        self.global_button_bar.addWidget(self.CloseButton)

        self.ApplyButton = QPushButton(Settings)
        self.ApplyButton.setObjectName(u"ApplyButton")
        self.ApplyButton.setEnabled(True)

        self.global_button_bar.addWidget(self.ApplyButton)


        self.gridLayout.addLayout(self.global_button_bar, 1, 0, 1, 1)

#if QT_CONFIG(shortcut)
        self.label.setBuddy(self.StationName)
        self.label_2.setBuddy(self.Slogan)
        self.label_16.setBuddy(self.NTPCheckServer)
        self.label_17.setBuddy(self.logoPath)
        self.hoursLEDsLabel.setBuddy(self.DigitalHourColorButton)
        self.secondsLEDsLabel.setBuddy(self.DigitalSecondColorButton)
        self.digitsLEDsLabel.setBuddy(self.DigitalDigitColorButton)
        self.label_10.setBuddy(self.dateFormat)
        self.label_14.setBuddy(self.owmAPIKey)
        self.label_23.setBuddy(self.owmCityID)
        self.label_24.setBuddy(self.owmLanguage)
        self.label_25.setBuddy(self.owmTestAPI)
        self.label_26.setBuddy(self.owmUnit)
        self.label_15.setBuddy(self.textClockLanguage)
        self.label_4.setBuddy(self.udpport)
        self.label_12.setBuddy(self.httpport)
        self.label_40.setBuddy(self.multicast_group)
        self.label_39.setBuddy(self.AIRMinWidth)
        self.label_38.setBuddy(self.SetFont_AIR4)
        self.label_29.setBuddy(self.SetFont_LED1)
        self.label_35.setBuddy(self.SetFont_AIR1)
        self.label_32.setBuddy(self.SetFont_LED4)
        self.label_34.setBuddy(self.SetFont_Slogan)
        self.label_30.setBuddy(self.SetFont_LED2)
        self.label_33.setBuddy(self.SetFont_StationName)
        self.label_36.setBuddy(self.SetFont_AIR2)
        self.label_31.setBuddy(self.SetFont_LED3)
        self.label_37.setBuddy(self.SetFont_AIR3)
#endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.StationName, self.StationNameColor)
        QWidget.setTabOrder(self.StationNameColor, self.Slogan)
        QWidget.setTabOrder(self.Slogan, self.SloganColor)
        QWidget.setTabOrder(self.SloganColor, self.LEDInactiveBGColor)
        QWidget.setTabOrder(self.LEDInactiveBGColor, self.LEDInactiveFGColor)
        QWidget.setTabOrder(self.LEDInactiveFGColor, self.LEDFont)
        QWidget.setTabOrder(self.LEDFont, self.checkBox_NTPCheck)
        QWidget.setTabOrder(self.checkBox_NTPCheck, self.NTPCheckServer)
        QWidget.setTabOrder(self.NTPCheckServer, self.clockDigital)
        QWidget.setTabOrder(self.clockDigital, self.clockAnalog)
        QWidget.setTabOrder(self.clockAnalog, self.logoPath)
        QWidget.setTabOrder(self.logoPath, self.logoButton)
        QWidget.setTabOrder(self.logoButton, self.resetLogoButton)
        QWidget.setTabOrder(self.resetLogoButton, self.DigitalHourColorButton)
        QWidget.setTabOrder(self.DigitalHourColorButton, self.DigitalSecondColorButton)
        QWidget.setTabOrder(self.DigitalSecondColorButton, self.DigitalDigitColorButton)
        QWidget.setTabOrder(self.DigitalDigitColorButton, self.checkBox_UpdateCheck)
        QWidget.setTabOrder(self.checkBox_UpdateCheck, self.checkBox_IncludeBetaVersions)
        QWidget.setTabOrder(self.checkBox_IncludeBetaVersions, self.updateCheckNowButton)
        QWidget.setTabOrder(self.updateCheckNowButton, self.updateKey)
        QWidget.setTabOrder(self.updateKey, self.showSeconds)
        QWidget.setTabOrder(self.showSeconds, self.staticColon)
        QWidget.setTabOrder(self.staticColon, self.useTextclock)
        QWidget.setTabOrder(self.useTextclock, self.plainTextEdit)
        QWidget.setTabOrder(self.plainTextEdit, self.LED1)
        QWidget.setTabOrder(self.LED1, self.LED1Text)
        QWidget.setTabOrder(self.LED1Text, self.LED2)
        QWidget.setTabOrder(self.LED2, self.LED2Text)
        QWidget.setTabOrder(self.LED2Text, self.LED3)
        QWidget.setTabOrder(self.LED3, self.LED3Text)
        QWidget.setTabOrder(self.LED3Text, self.LED4)
        QWidget.setTabOrder(self.LED4, self.LED4Text)
        QWidget.setTabOrder(self.LED4Text, self.LED1BGColor)
        QWidget.setTabOrder(self.LED1BGColor, self.LED1FGColor)
        QWidget.setTabOrder(self.LED1FGColor, self.LED1Autoflash)
        QWidget.setTabOrder(self.LED1Autoflash, self.LED1Timedflash)
        QWidget.setTabOrder(self.LED1Timedflash, self.LED2BGColor)
        QWidget.setTabOrder(self.LED2BGColor, self.LED2FGColor)
        QWidget.setTabOrder(self.LED2FGColor, self.LED2Autoflash)
        QWidget.setTabOrder(self.LED2Autoflash, self.LED2Timedflash)
        QWidget.setTabOrder(self.LED2Timedflash, self.LED3BGColor)
        QWidget.setTabOrder(self.LED3BGColor, self.LED3FGColor)
        QWidget.setTabOrder(self.LED3FGColor, self.LED3Autoflash)
        QWidget.setTabOrder(self.LED3Autoflash, self.LED3Timedflash)
        QWidget.setTabOrder(self.LED3Timedflash, self.LED4BGColor)
        QWidget.setTabOrder(self.LED4BGColor, self.LED4FGColor)
        QWidget.setTabOrder(self.LED4FGColor, self.LED4Autoflash)
        QWidget.setTabOrder(self.LED4Autoflash, self.LED4Timedflash)
        QWidget.setTabOrder(self.LED4Timedflash, self.udpport)
        QWidget.setTabOrder(self.udpport, self.httpport)
        QWidget.setTabOrder(self.httpport, self.dateFormat)
        QWidget.setTabOrder(self.dateFormat, self.textBrowser_2)
        QWidget.setTabOrder(self.textBrowser_2, self.time_24h)
        QWidget.setTabOrder(self.time_24h, self.time_am_pm)
        QWidget.setTabOrder(self.time_am_pm, self.textClockLanguage)
        QWidget.setTabOrder(self.textClockLanguage, self.owmWidgetEnabled)
        QWidget.setTabOrder(self.owmWidgetEnabled, self.owmAPIKey)
        QWidget.setTabOrder(self.owmAPIKey, self.owmCityID)
        QWidget.setTabOrder(self.owmCityID, self.owmLanguage)
        QWidget.setTabOrder(self.owmLanguage, self.owmUnit)
        QWidget.setTabOrder(self.owmUnit, self.owmTestAPI)
        QWidget.setTabOrder(self.owmTestAPI, self.tabWidget)
        QWidget.setTabOrder(self.tabWidget, self.owmTestOutput)
        QWidget.setTabOrder(self.owmTestOutput, self.enableResetButton)
        QWidget.setTabOrder(self.enableResetButton, self.ResetSettingsButton)
        QWidget.setTabOrder(self.ResetSettingsButton, self.ExitButton)
        QWidget.setTabOrder(self.ExitButton, self.RebootButton)
        QWidget.setTabOrder(self.RebootButton, self.ShutdownButton)
        QWidget.setTabOrder(self.ShutdownButton, self.CloseButton)
        QWidget.setTabOrder(self.CloseButton, self.ApplyButton)

        self.retranslateUi(Settings)
        self.CloseButton.clicked.connect(Settings.close)
        self.owmWidgetEnabled.clicked["bool"].connect(self.owmTestOutput.setEnabled)
        self.clockDigital.toggled.connect(self.secondsLEDsLabel.setEnabled)
        self.owmWidgetEnabled.clicked["bool"].connect(self.label_23.setEnabled)
        self.owmWidgetEnabled.clicked["bool"].connect(self.label_24.setEnabled)
        self.checkBox_UpdateCheck.clicked["bool"].connect(self.checkBox_IncludeBetaVersions.setEnabled)
        self.owmWidgetEnabled.clicked["bool"].connect(self.owmTestAPI.setEnabled)
        self.LED2.clicked["bool"].connect(self.LED2FGColor.setEnabled)
        self.LED1.clicked["bool"].connect(self.LED1Text.setEnabled)
        self.LED3.clicked["bool"].connect(self.LED3FGColor.setEnabled)
        self.LED4.clicked["bool"].connect(self.LED4FGColor.setEnabled)
        self.LED1.clicked["bool"].connect(self.LED1BGColor.setEnabled)
        self.LED3.clicked["bool"].connect(self.LED3Timedflash.setEnabled)
        self.LED1.clicked["bool"].connect(self.LED1Autoflash.setEnabled)
        self.LED4.clicked["bool"].connect(self.LED4Timedflash.setEnabled)
        self.LED1.clicked["bool"].connect(self.LED1FGColor.setEnabled)
        self.LED2.clicked["bool"].connect(self.LED2Autoflash.setEnabled)
        self.LED1Text.textChanged.connect(self.LED1Demo.setText)
        self.LED1.clicked["bool"].connect(self.LED1Timedflash.setEnabled)
        self.LED3.clicked["bool"].connect(self.LED3Autoflash.setEnabled)
        self.LED2.clicked["bool"].connect(self.LED2Demo.setEnabled)
        self.LED2.clicked["bool"].connect(self.LED2Timedflash.setEnabled)
        self.LED4.clicked["bool"].connect(self.LED4Autoflash.setEnabled)
        self.LED2.clicked["bool"].connect(self.LED2BGColor.setEnabled)
        self.clockDigital.toggled.connect(self.DigitalSecondColorButton.setEnabled)
        self.Slogan.textChanged.connect(self.SloganDemo.setText)
        self.LED3.clicked["bool"].connect(self.LED3BGColor.setEnabled)
        self.owmWidgetEnabled.clicked["bool"].connect(self.owmAPIKey.setEnabled)
        self.LED1.clicked["bool"].connect(self.LED1Demo.setEnabled)
        self.LED4.clicked["bool"].connect(self.LED4BGColor.setEnabled)
        self.LED2.clicked["bool"].connect(self.LED2Text.setEnabled)
        self.owmWidgetEnabled.clicked["bool"].connect(self.label_25.setEnabled)
        self.clockDigital.toggled.connect(self.DigitalHourColorButton.setEnabled)
        self.checkBox_NTPCheck.clicked["bool"].connect(self.NTPCheckServer.setEnabled)
        self.checkBox_UpdateCheck.clicked["bool"].connect(self.updateKey.setEnabled)
        self.LED3.clicked["bool"].connect(self.LED3Demo.setEnabled)
        self.LED3.clicked["bool"].connect(self.LED3Text.setEnabled)
        self.checkBox_UpdateCheck.clicked["bool"].connect(self.updateCheckNowButton.setEnabled)
        self.LED3Text.textChanged.connect(self.LED3Demo.setText)
        self.owmWidgetEnabled.clicked["bool"].connect(self.owmUnit.setEnabled)
        self.LED4.clicked["bool"].connect(self.LED4Text.setEnabled)
        self.clockDigital.toggled.connect(self.DigitalDigitColorButton.setEnabled)
        self.LED4.clicked["bool"].connect(self.LED4Demo.setEnabled)
        self.checkBox_NTPCheck.clicked["bool"].connect(self.label_16.setEnabled)
        self.owmWidgetEnabled.clicked["bool"].connect(self.owmCityID.setEnabled)
        self.checkBox_UpdateCheck.clicked["bool"].connect(self.label_28.setEnabled)
        self.clockDigital.toggled.connect(self.hoursLEDsLabel.setEnabled)
        self.LED2Text.textChanged.connect(self.LED2Demo.setText)
        self.owmWidgetEnabled.clicked["bool"].connect(self.label_26.setEnabled)
        self.StationName.textChanged.connect(self.StationNameDemo.setText)
        self.owmWidgetEnabled.clicked["bool"].connect(self.owmLanguage.setEnabled)
        self.clockDigital.toggled.connect(self.digitsLEDsLabel.setEnabled)
        self.LED4Text.textChanged.connect(self.LED4Demo.setText)
        self.owmWidgetEnabled.clicked["bool"].connect(self.label_14.setEnabled)
        self.enableResetButton.clicked["bool"].connect(self.ResetSettingsButton.setEnabled)
        self.enableAIR1.clicked["bool"].connect(self.AIR1Text.setEnabled)
        self.enableAIR1.clicked["bool"].connect(self.AIR1Demo.setEnabled)
        self.enableAIR1.clicked["bool"].connect(self.AIR1BGColor.setEnabled)
        self.enableAIR1.clicked["bool"].connect(self.AIR1FGColor.setEnabled)
        self.enableAIR2.clicked["bool"].connect(self.AIR2Text.setEnabled)
        self.enableAIR2.clicked["bool"].connect(self.AIR2Demo.setEnabled)
        self.enableAIR2.clicked["bool"].connect(self.AIR2BGColor.setEnabled)
        self.enableAIR2.clicked["bool"].connect(self.AIR2FGColor.setEnabled)
        self.enableAIR3.clicked["bool"].connect(self.AIR3Text.setEnabled)
        self.enableAIR3.clicked["bool"].connect(self.AIR3Demo.setEnabled)
        self.enableAIR3.clicked["bool"].connect(self.AIR3BGColor.setEnabled)
        self.enableAIR3.clicked["bool"].connect(self.AIR3FGColor.setEnabled)
        self.enableAIR4.clicked["bool"].connect(self.AIR4Text.setEnabled)
        self.enableAIR4.clicked["bool"].connect(self.AIR4Demo.setEnabled)
        self.enableAIR4.clicked["bool"].connect(self.AIR4BGColor.setEnabled)
        self.enableAIR4.clicked["bool"].connect(self.AIR4FGColor.setEnabled)
        self.AIR1Text.textChanged.connect(self.AIR1Demo.setText)
        self.AIR2Text.textChanged.connect(self.AIR2Demo.setText)
        self.AIR3Text.textChanged.connect(self.AIR3Demo.setText)
        self.AIR4Text.textChanged.connect(self.AIR4Demo.setText)
        self.replaceNOW.clicked["bool"].connect(self.replaceNOWText.setEnabled)
        self.showSeconds.clicked["bool"].connect(self.seconds_separate.setEnabled)
        self.showSeconds.clicked["bool"].connect(self.seconds_in_one_line.setEnabled)

        self.tabWidget.setCurrentIndex(0)
        self.ApplyButton.setDefault(True)


        QMetaObject.connectSlotsByName(Settings)
    # setupUi

    def retranslateUi(self, Settings):
        Settings.setWindowTitle(QCoreApplication.translate("Settings", u"OnAirScreen Settings", None))
        self.LED1.setText(QCoreApplication.translate("Settings", u"Status LED 1", None))
        self.LED1Text.setText(QCoreApplication.translate("Settings", u"ON AIR", None))
        self.LED1Demo.setText(QCoreApplication.translate("Settings", u"ON AIR", None))
        self.LED1BGColor.setText(QCoreApplication.translate("Settings", u"Active BG Color", None))
        self.LED1FGColor.setText(QCoreApplication.translate("Settings", u"Active Text Color", None))
        self.LED1Autoflash.setText(QCoreApplication.translate("Settings", u"Autoflash", None))
        self.LED1Timedflash.setText(QCoreApplication.translate("Settings", u"20sec flash", None))
        self.LED2.setText(QCoreApplication.translate("Settings", u"Status LED 2", None))
        self.LED2Text.setText(QCoreApplication.translate("Settings", u"PHONE", None))
        self.LED2Demo.setText(QCoreApplication.translate("Settings", u"PHONE", None))
        self.LED2BGColor.setText(QCoreApplication.translate("Settings", u"Active BG Color", None))
        self.LED2FGColor.setText(QCoreApplication.translate("Settings", u"Active Text Color", None))
        self.LED2Autoflash.setText(QCoreApplication.translate("Settings", u"Autoflash", None))
        self.LED2Timedflash.setText(QCoreApplication.translate("Settings", u"20sec flash", None))
        self.LED3.setText(QCoreApplication.translate("Settings", u"Status LED 3", None))
        self.LED3Text.setText(QCoreApplication.translate("Settings", u"DOORBELL", None))
        self.LED3Demo.setText(QCoreApplication.translate("Settings", u"DOORBELL", None))
        self.LED3BGColor.setText(QCoreApplication.translate("Settings", u"Active BG Color", None))
        self.LED3FGColor.setText(QCoreApplication.translate("Settings", u"Active Text Color", None))
        self.LED3Autoflash.setText(QCoreApplication.translate("Settings", u"Autoflash", None))
        self.LED3Timedflash.setText(QCoreApplication.translate("Settings", u"20sec flash", None))
        self.LED4.setText(QCoreApplication.translate("Settings", u"Status LED 4", None))
        self.LED4Text.setText(QCoreApplication.translate("Settings", u"ARI", None))
        self.LED4Demo.setText(QCoreApplication.translate("Settings", u"ARI", None))
        self.LED4BGColor.setText(QCoreApplication.translate("Settings", u"Active BG Color", None))
        self.LED4FGColor.setText(QCoreApplication.translate("Settings", u"Active Text Color", None))
        self.LED4Autoflash.setText(QCoreApplication.translate("Settings", u"Autoflash", None))
        self.LED4Timedflash.setText(QCoreApplication.translate("Settings", u"20sec flash", None))
        self.label.setText(QCoreApplication.translate("Settings", u"Station Name", None))
        self.StationName.setText(QCoreApplication.translate("Settings", u"StationName", None))
        self.StationNameColor.setText(QCoreApplication.translate("Settings", u"Color", None))
        self.label_2.setText(QCoreApplication.translate("Settings", u"Slogan", None))
        self.Slogan.setText(QCoreApplication.translate("Settings", u"Slogan", None))
        self.SloganColor.setText(QCoreApplication.translate("Settings", u"Color", None))
        self.StationNameDemo.setText(QCoreApplication.translate("Settings", u"StationName", None))
        self.SloganDemo.setText(QCoreApplication.translate("Settings", u"Slogan", None))
        self.label_5.setText(QCoreApplication.translate("Settings", u"Inactive LED Colors", None))
        self.LEDInactive.setText(QCoreApplication.translate("Settings", u"DEMOTEXT", None))
        self.LEDInactiveBGColor.setText(QCoreApplication.translate("Settings", u"BG Color", None))
        self.LEDInactiveFGColor.setText(QCoreApplication.translate("Settings", u"Text Color", None))
        self.LEDFont.setText(QCoreApplication.translate("Settings", u"Set LED Font", None))
        self.checkBox_NTPCheck.setText(QCoreApplication.translate("Settings", u"Enable NTP-Check and warning", None))
        self.label_16.setText(QCoreApplication.translate("Settings", u"NTP-Check Server:", None))
#if QT_CONFIG(tooltip)
        self.NTPCheckServer.setToolTip(QCoreApplication.translate("Settings", u"<html><head/><body><p><span style=\" font-size:11pt;\">pool.ntp.org is unreliable from time to time, it is adviced to use/install a timeserver that is in your local network and which is always available</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.NTPCheckServer.setText(QCoreApplication.translate("Settings", u"NTPCheckServer", None))
        self.label_17.setText(QCoreApplication.translate("Settings", u"Logo Path", None))
        self.logoButton.setText(QCoreApplication.translate("Settings", u"...", None))
        self.resetLogoButton.setText(QCoreApplication.translate("Settings", u"reset", None))
        self.radioButton_logo_upper.setText(QCoreApplication.translate("Settings", u"Prefer logo in upper part of clock", None))
        self.radioButton_logo_lower.setText(QCoreApplication.translate("Settings", u"Prefer logo in lower part of clock", None))
        self.checkBox_UpdateCheck.setText(QCoreApplication.translate("Settings", u"Check for updates", None))
        self.checkBox_IncludeBetaVersions.setText(QCoreApplication.translate("Settings", u"Include beta versions", None))
        self.updateCheckNowButton.setText(QCoreApplication.translate("Settings", u"Check now", None))
        self.updateKey.setPlaceholderText(QCoreApplication.translate("Settings", u"paste your update key here", None))
        self.label_28.setText(QCoreApplication.translate("Settings", u"To obtain the latest updates of the precompiled (paid) versions, you need a valid update key.", None))
        self.label_11.setText(QCoreApplication.translate("Settings", u"OnAir Clock Mode / Colors", None))
        self.clockDigital.setText(QCoreApplication.translate("Settings", u"Digital", None))
        self.clockAnalog.setText(QCoreApplication.translate("Settings", u"Analog", None))
        self.hoursLEDsLabel.setText(QCoreApplication.translate("Settings", u"Hours LEDs", None))
        self.DigitalHourColorButton.setText(QCoreApplication.translate("Settings", u"Set", None))
        self.secondsLEDsLabel.setText(QCoreApplication.translate("Settings", u"Seconds LEDs", None))
        self.DigitalSecondColorButton.setText(QCoreApplication.translate("Settings", u"Set", None))
        self.digitsLEDsLabel.setText(QCoreApplication.translate("Settings", u"Digits LEDs", None))
        self.DigitalDigitColorButton.setText(QCoreApplication.translate("Settings", u"Set", None))
        self.showSeconds.setText(QCoreApplication.translate("Settings", u"Show seconds", None))
        self.seconds_separate.setText(QCoreApplication.translate("Settings", u"separate", None))
        self.seconds_in_one_line.setText(QCoreApplication.translate("Settings", u"in one line", None))
        self.staticColon.setText(QCoreApplication.translate("Settings", u"Static colon", None))
        self.useTextclock.setText(QCoreApplication.translate("Settings", u"Use textclock", None))
        self.replaceNOW.setText(QCoreApplication.translate("Settings", u"Replace \"IPs\" after 10s", None))
        self.replaceNOWText.setText("")
        self.replaceNOWText.setPlaceholderText(QCoreApplication.translate("Settings", u"Replace with this text", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_general), QCoreApplication.translate("Settings", u"General Settings", None))
        self.label_10.setText(QCoreApplication.translate("Settings", u"Date format", None))
        self.dateFormat.setText(QCoreApplication.translate("Settings", u"dddd, dd. MMMM yyyy", None))
        self.textBrowser_2.setHtml(QCoreApplication.translate("Settings", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'.AppleSystemUIFont'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'.SF NS Text'; font-size:11pt; font-weight:600;\">Date format placeholders</span></p>\n"
"<table border=\"0\" style=\" margin-top:5px; margin-bottom:0px; margin-left:0px; margin-right:0px;\" cellspacing=\"2\" cellpadding=\"1\">\n"
"<tr>\n"
"<td>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'.SF NS Text'; font-size:11pt;\">d</span></p></td>\n"
"<td>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; mar"
                        "gin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'.SF NS Text'; font-size:11pt;\">the day as number without a leading zero (1 to 31)</span></p></td></tr>\n"
"<tr>\n"
"<td>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'.SF NS Text'; font-size:11pt;\">dd</span></p></td>\n"
"<td>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'.SF NS Text'; font-size:11pt;\">the day as number with a leading zero (01 to 31)</span></p></td></tr>\n"
"<tr>\n"
"<td>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'.SF NS Text'; font-size:11pt;\">ddd</span></p></td>\n"
"<td>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px"
                        ";\"><span style=\" font-family:'.SF NS Text'; font-size:11pt;\">the abbreviated localized day name (e.g. 'Mon' to 'Sun') [System localized]</span></p></td></tr>\n"
"<tr>\n"
"<td>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'.SF NS Text'; font-size:11pt;\">dddd</span></p></td>\n"
"<td>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'.SF NS Text'; font-size:11pt;\">the long localized day name (e.g. 'Monday' to 'Sunday') [System localized]</span></p></td></tr>\n"
"<tr>\n"
"<td>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'.SF NS Text'; font-size:11pt;\">M</span></p></td>\n"
"<td>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0p"
                        "x;\"><span style=\" font-family:'.SF NS Text'; font-size:11pt;\">the month as number without a leading zero (1-12)</span></p></td></tr>\n"
"<tr>\n"
"<td>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'.SF NS Text'; font-size:11pt;\">MM</span></p></td>\n"
"<td>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'.SF NS Text'; font-size:11pt;\">the month as number with a leading zero (01-12)</span></p></td></tr>\n"
"<tr>\n"
"<td>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'.SF NS Text'; font-size:11pt;\">MMM</span></p></td>\n"
"<td>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'.SF NS Text'; font-"
                        "size:11pt;\">the abbreviated localized month name (e.g. 'Jan' to 'Dec') [System localized]</span></p></td></tr>\n"
"<tr>\n"
"<td>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'.SF NS Text'; font-size:11pt;\">MMMM</span></p></td>\n"
"<td>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'.SF NS Text'; font-size:11pt;\">the long localized month name (e.g. 'January' to 'December') [System localized]</span></p></td></tr>\n"
"<tr>\n"
"<td>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'.SF NS Text'; font-size:11pt;\">yy</span></p></td>\n"
"<td>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'.SF NS Tex"
                        "t'; font-size:11pt;\">the year as two digit number (00-99)</span></p></td></tr>\n"
"<tr>\n"
"<td>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'.SF NS Text'; font-size:11pt;\">yyyy</span></p></td>\n"
"<td>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'.SF NS Text'; font-size:11pt;\">the year as four digit number</span></p></td></tr></table></body></html>", None))
        self.label_22.setText(QCoreApplication.translate("Settings", u"Time format", None))
        self.time_24h.setText(QCoreApplication.translate("Settings", u"24 hours", None))
        self.time_am_pm.setText(QCoreApplication.translate("Settings", u"AM/PM", None))
        self.label_13.setText(QCoreApplication.translate("Settings", u"Weather Widget (openweathermap.org)", None))
        self.label_27.setText(QCoreApplication.translate("Settings", u"<html><head/><body><p><a href=\"https://www.astrastudio.de/wiki/onairscreen#weather-widget\"><span style=\" text-decoration: underline; color:#0069d9;\">WeatherWidget Guide</span></a></p></body></html>", None))
        self.owmWidgetEnabled.setText(QCoreApplication.translate("Settings", u"show Weather Widget", None))
        self.label_14.setText(QCoreApplication.translate("Settings", u"API Key", None))
        self.owmAPIKey.setText("")
        self.label_23.setText(QCoreApplication.translate("Settings", u"City ID", None))
        self.label_24.setText(QCoreApplication.translate("Settings", u"Language", None))
        self.owmLanguage.setItemText(0, QCoreApplication.translate("Settings", u"Suaheli", None))

        self.owmTestAPI.setText(QCoreApplication.translate("Settings", u"Make API Call", None))
        self.label_25.setText(QCoreApplication.translate("Settings", u"Test API", None))
        self.label_26.setText(QCoreApplication.translate("Settings", u"Unit", None))
        self.owmUnit.setItemText(0, QCoreApplication.translate("Settings", u"metric", None))

        self.label_15.setText(QCoreApplication.translate("Settings", u"Textclock Language", None))
        self.textClockLanguage.setItemText(0, QCoreApplication.translate("Settings", u"Suaheli", None))
        self.textClockLanguage.setItemText(1, QCoreApplication.translate("Settings", u"English", None))
        self.textClockLanguage.setItemText(2, QCoreApplication.translate("Settings", u"German", None))
        self.textClockLanguage.setItemText(3, QCoreApplication.translate("Settings", u"French", None))

        self.label_4.setText(QCoreApplication.translate("Settings", u"UDP Port", None))
        self.label_12.setText(QCoreApplication.translate("Settings", u"HTTP Port", None))
        self.label_40.setText(QCoreApplication.translate("Settings", u"Multicast Address", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_advanced), QCoreApplication.translate("Settings", u"Advanced Settings", None))
        self.enableAIR1.setText(QCoreApplication.translate("Settings", u"Timer AIR1 (Mic)", None))
        self.AIR1Text.setText(QCoreApplication.translate("Settings", u"AIR 1 DEMO", None))
        self.AIR1Demo.setText(QCoreApplication.translate("Settings", u"AIR 1 DEMO", None))
        self.AIR1BGColor.setText(QCoreApplication.translate("Settings", u"Active BG Color", None))
        self.AIR1FGColor.setText(QCoreApplication.translate("Settings", u"Active Text Color", None))
        self.AIR1IconSelectButton.setText(QCoreApplication.translate("Settings", u"Select Icon", None))
        self.AIR1IconResetButton.setText(QCoreApplication.translate("Settings", u"Reset Icon", None))
        self.enableAIR2.setText(QCoreApplication.translate("Settings", u"Timer AIR2 (Phone)", None))
        self.AIR2Text.setText(QCoreApplication.translate("Settings", u"AIR 2 DEMO", None))
        self.AIR2Demo.setText(QCoreApplication.translate("Settings", u"AIR 1 DEMO", None))
        self.AIR2BGColor.setText(QCoreApplication.translate("Settings", u"Active BG Color", None))
        self.AIR2FGColor.setText(QCoreApplication.translate("Settings", u"Active Text Color", None))
        self.AIR2IconSelectButton.setText(QCoreApplication.translate("Settings", u"Select Icon", None))
        self.AIR2IconResetButton.setText(QCoreApplication.translate("Settings", u"Reset Icon", None))
        self.enableAIR3.setText(QCoreApplication.translate("Settings", u"Timer AIR3 (Timer)", None))
        self.AIR3Text.setText(QCoreApplication.translate("Settings", u"AIR 3 DEMO", None))
        self.AIR3Demo.setText(QCoreApplication.translate("Settings", u"AIR 1 DEMO", None))
        self.AIR3BGColor.setText(QCoreApplication.translate("Settings", u"Active BG Color", None))
        self.AIR3FGColor.setText(QCoreApplication.translate("Settings", u"Active Text Color", None))
        self.AIR3IconSelectButton.setText(QCoreApplication.translate("Settings", u"Select Icon", None))
        self.AIR3IconResetButton.setText(QCoreApplication.translate("Settings", u"Reset Icon", None))
        self.enableAIR4.setText(QCoreApplication.translate("Settings", u"Timer AIR4 (Stream)", None))
        self.AIR4Text.setText(QCoreApplication.translate("Settings", u"AIR 4 DEMO", None))
        self.AIR4Demo.setText(QCoreApplication.translate("Settings", u"AIR 1 DEMO", None))
        self.AIR4BGColor.setText(QCoreApplication.translate("Settings", u"Active BG Color", None))
        self.AIR4FGColor.setText(QCoreApplication.translate("Settings", u"Active Text Color", None))
        self.AIR4IconSelectButton.setText(QCoreApplication.translate("Settings", u"Select Icon", None))
        self.AIR4IconResetButton.setText(QCoreApplication.translate("Settings", u"Reset Icon", None))
        self.label_39.setText(QCoreApplication.translate("Settings", u"Miminum Timer Width", None))
        self.AIRMinWidth.setSuffix(QCoreApplication.translate("Settings", u" px", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_timers), QCoreApplication.translate("Settings", u"Timers", None))
        self.label_38.setText(QCoreApplication.translate("Settings", u"AIR4", None))
        self.label_29.setText(QCoreApplication.translate("Settings", u"LED1", None))
        self.label_35.setText(QCoreApplication.translate("Settings", u"AIR1", None))
        self.label_32.setText(QCoreApplication.translate("Settings", u"LED4", None))
        self.label_34.setText(QCoreApplication.translate("Settings", u"Slogan", None))
        self.label_30.setText(QCoreApplication.translate("Settings", u"LED2", None))
        self.label_33.setText(QCoreApplication.translate("Settings", u"Station Name", None))
        self.label_36.setText(QCoreApplication.translate("Settings", u"AIR2", None))
        self.label_31.setText(QCoreApplication.translate("Settings", u"LED3", None))
        self.ExampleFont_AIR1.setText(QCoreApplication.translate("Settings", u"This is an example text", None))
        self.ExampleFont_AIR2.setText(QCoreApplication.translate("Settings", u"This is an example text", None))
        self.label_37.setText(QCoreApplication.translate("Settings", u"AIR3", None))
        self.ExampleFont_AIR3.setText(QCoreApplication.translate("Settings", u"This is an example text", None))
        self.ExampleFont_AIR4.setText(QCoreApplication.translate("Settings", u"This is an example text", None))
        self.ExampleFont_LED1.setText(QCoreApplication.translate("Settings", u"This is an example text", None))
        self.ExampleFont_LED2.setText(QCoreApplication.translate("Settings", u"This is an example text", None))
        self.ExampleFont_LED3.setText(QCoreApplication.translate("Settings", u"This is an example text", None))
        self.ExampleFont_LED4.setText(QCoreApplication.translate("Settings", u"This is an example text", None))
        self.ExampleFont_StationName.setText(QCoreApplication.translate("Settings", u"This is an example text", None))
        self.ExampleFont_Slogan.setText(QCoreApplication.translate("Settings", u"This is an example text", None))
        self.SetFont_AIR3.setText(QCoreApplication.translate("Settings", u"Set Font", None))
        self.SetFont_AIR1.setText(QCoreApplication.translate("Settings", u"Set Font", None))
        self.SetFont_AIR2.setText(QCoreApplication.translate("Settings", u"Set Font", None))
        self.SetFont_AIR4.setText(QCoreApplication.translate("Settings", u"Set Font", None))
        self.SetFont_LED1.setText(QCoreApplication.translate("Settings", u"Set Font", None))
        self.SetFont_LED2.setText(QCoreApplication.translate("Settings", u"Set Font", None))
        self.SetFont_LED3.setText(QCoreApplication.translate("Settings", u"Set Font", None))
        self.SetFont_LED4.setText(QCoreApplication.translate("Settings", u"Set Font", None))
        self.SetFont_StationName.setText(QCoreApplication.translate("Settings", u"Set Font", None))
        self.SetFont_Slogan.setText(QCoreApplication.translate("Settings", u"Set Font", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_fonts), QCoreApplication.translate("Settings", u"Fonts", None))
        self.label_6.setText(QCoreApplication.translate("Settings", u"OnAirScreen", None))
        self.versionLabel.setText(QCoreApplication.translate("Settings", u"Version: ???", None))
        self.label_8.setText("")
        self.label_3.setText(QCoreApplication.translate("Settings", u"Powered by:", None))
        self.label_18.setText("")
        self.label_20.setText(QCoreApplication.translate("Settings", u"PyInstaller", None))
        self.label_19.setText("")
        self.label_21.setText(QCoreApplication.translate("Settings", u"PyQT", None))
        self.label_9.setText(QCoreApplication.translate("Settings", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\"font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"http://www.astrastudio.de\"><span style=\" text-decoration: underline; color:#0057ae;\">http://www.astrastudio.de</span></a></p></body></html>", None))
        self.label_7.setText(QCoreApplication.translate("Settings", u"\u00a9 2012-2024 Sascha Ludwig", None))
        self.ResetSettingsButton.setText(QCoreApplication.translate("Settings", u"Reset all OnAirScreen settings to default", None))
        self.enableResetButton.setText(QCoreApplication.translate("Settings", u"Enable Reset all settings button", None))
        self.distributionLabel.setText(QCoreApplication.translate("Settings", u"Distribution: ???", None))
        self.settingspathLabel.setText(QCoreApplication.translate("Settings", u"Settings Path: ???", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_about), QCoreApplication.translate("Settings", u"About", None))
        self.plainTextEdit.setPlainText(QCoreApplication.translate("Settings", u"##################################################################\n"
"#\n"
"# OnAirScreen\n"
"# Copyright (c) 2012-2024 Sascha Ludwig, astrastudio.de\n"
"# All rights reserved.\n"
"#\n"
"# You may use this file under the terms of the BSD license as follows:\n"
"#\n"
"# \"Redistribution and use in source and binary forms, with or without\n"
"# modification, are permitted provided that the following conditions are\n"
"# met:\n"
"#   * Redistributions of source code must retain the above copyright\n"
"#     notice, this list of conditions and the following disclaimer.\n"
"#   * Redistributions in binary form must reproduce the above copyright\n"
"#     notice, this list of conditions and the following disclaimer in\n"
"#     the documentation and/or other materials provided with the\n"
"#     distribution.\n"
"#\n"
"# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS\n"
"# \"AS IS\" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT\n"
"# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABI"
                        "LITY AND FITNESS FOR\n"
"# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT\n"
"# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,\n"
"# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT\n"
"# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,\n"
"# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY\n"
"# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT\n"
"# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE\n"
"# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.\"\n"
"#\n"
"##################################################################\n"
"\n"
"##################################################################\n"
"3rd party licenses\n"
"##################################################################\n"
"\n"
"                    GNU GENERAL PUBLIC LICENSE\n"
"                       Version 3, 29 June 2007\n"
"\n"
" Copyright (C) 2007 Free Software Founda"
                        "tion, Inc. <http://fsf.org/>\n"
" Everyone is permitted to copy and distribute verbatim copies\n"
" of this license document, but changing it is not allowed.\n"
"\n"
"                            Preamble\n"
"\n"
"  The GNU General Public License is a free, copyleft license for\n"
"software and other kinds of works.\n"
"\n"
"  The licenses for most software and other practical works are designed\n"
"to take away your freedom to share and change the works.  By contrast,\n"
"the GNU General Public License is intended to guarantee your freedom to\n"
"share and change all versions of a program--to make sure it remains free\n"
"software for all its users.  We, the Free Software Foundation, use the\n"
"GNU General Public License for most of our software; it applies also to\n"
"any other work released this way by its authors.  You can apply it to\n"
"your programs, too.\n"
"\n"
"  When we speak of free software, we are referring to freedom, not\n"
"price.  Our General Public Licenses are designed to make sure that you"
                        "\n"
"have the freedom to distribute copies of free software (and charge for\n"
"them if you wish), that you receive source code or can get it if you\n"
"want it, that you can change the software or use pieces of it in new\n"
"free programs, and that you know you can do these things.\n"
"\n"
"  To protect your rights, we need to prevent others from denying you\n"
"these rights or asking you to surrender the rights.  Therefore, you have\n"
"certain responsibilities if you distribute copies of the software, or if\n"
"you modify it: responsibilities to respect the freedom of others.\n"
"\n"
"  For example, if you distribute copies of such a program, whether\n"
"gratis or for a fee, you must pass on to the recipients the same\n"
"freedoms that you received.  You must make sure that they, too, receive\n"
"or can get the source code.  And you must show them these terms so they\n"
"know their rights.\n"
"\n"
"  Developers that use the GNU GPL protect your rights with two steps:\n"
"(1) assert copyright on the software"
                        ", and (2) offer you this License\n"
"giving you legal permission to copy, distribute and/or modify it.\n"
"\n"
"  For the developers' and authors' protection, the GPL clearly explains\n"
"that there is no warranty for this free software.  For both users' and\n"
"authors' sake, the GPL requires that modified versions be marked as\n"
"changed, so that their problems will not be attributed erroneously to\n"
"authors of previous versions.\n"
"\n"
"  Some devices are designed to deny users access to install or run\n"
"modified versions of the software inside them, although the manufacturer\n"
"can do so.  This is fundamentally incompatible with the aim of\n"
"protecting users' freedom to change the software.  The systematic\n"
"pattern of such abuse occurs in the area of products for individuals to\n"
"use, which is precisely where it is most unacceptable.  Therefore, we\n"
"have designed this version of the GPL to prohibit the practice for those\n"
"products.  If such problems arise substantially in other domains,"
                        " we\n"
"stand ready to extend this provision to those domains in future versions\n"
"of the GPL, as needed to protect the freedom of users.\n"
"\n"
"  Finally, every program is threatened constantly by software patents.\n"
"States should not allow patents to restrict development and use of\n"
"software on general-purpose computers, but in those that do, we wish to\n"
"avoid the special danger that patents applied to a free program could\n"
"make it effectively proprietary.  To prevent this, the GPL assures that\n"
"patents cannot be used to render the program non-free.\n"
"\n"
"  The precise terms and conditions for copying, distribution and\n"
"modification follow.\n"
"\n"
"                       TERMS AND CONDITIONS\n"
"\n"
"  0. Definitions.\n"
"\n"
"  \"This License\" refers to version 3 of the GNU General Public License.\n"
"\n"
"  \"Copyright\" also means copyright-like laws that apply to other kinds of\n"
"works, such as semiconductor masks.\n"
"\n"
"  \"The Program\" refers to any copyrightable work li"
                        "censed under this\n"
"License.  Each licensee is addressed as \"you\".  \"Licensees\" and\n"
"\"recipients\" may be individuals or organizations.\n"
"\n"
"  To \"modify\" a work means to copy from or adapt all or part of the work\n"
"in a fashion requiring copyright permission, other than the making of an\n"
"exact copy.  The resulting work is called a \"modified version\" of the\n"
"earlier work or a work \"based on\" the earlier work.\n"
"\n"
"  A \"covered work\" means either the unmodified Program or a work based\n"
"on the Program.\n"
"\n"
"  To \"propagate\" a work means to do anything with it that, without\n"
"permission, would make you directly or secondarily liable for\n"
"infringement under applicable copyright law, except executing it on a\n"
"computer or modifying a private copy.  Propagation includes copying,\n"
"distribution (with or without modification), making available to the\n"
"public, and in some countries other activities as well.\n"
"\n"
"  To \"convey\" a work means any kind of propagat"
                        "ion that enables other\n"
"parties to make or receive copies.  Mere interaction with a user through\n"
"a computer network, with no transfer of a copy, is not conveying.\n"
"\n"
"  An interactive user interface displays \"Appropriate Legal Notices\"\n"
"to the extent that it includes a convenient and prominently visible\n"
"feature that (1) displays an appropriate copyright notice, and (2)\n"
"tells the user that there is no warranty for the work (except to the\n"
"extent that warranties are provided), that licensees may convey the\n"
"work under this License, and how to view a copy of this License.  If\n"
"the interface presents a list of user commands or options, such as a\n"
"menu, a prominent item in the list meets this criterion.\n"
"\n"
"  1. Source Code.\n"
"\n"
"  The \"source code\" for a work means the preferred form of the work\n"
"for making modifications to it.  \"Object code\" means any non-source\n"
"form of a work.\n"
"\n"
"  A \"Standard Interface\" means an interface that either is an officia"
                        "l\n"
"standard defined by a recognized standards body, or, in the case of\n"
"interfaces specified for a particular programming language, one that\n"
"is widely used among developers working in that language.\n"
"\n"
"  The \"System Libraries\" of an executable work include anything, other\n"
"than the work as a whole, that (a) is included in the normal form of\n"
"packaging a Major Component, but which is not part of that Major\n"
"Component, and (b) serves only to enable use of the work with that\n"
"Major Component, or to implement a Standard Interface for which an\n"
"implementation is available to the public in source code form.  A\n"
"\"Major Component\", in this context, means a major essential component\n"
"(kernel, window system, and so on) of the specific operating system\n"
"(if any) on which the executable work runs, or a compiler used to\n"
"produce the work, or an object code interpreter used to run it.\n"
"\n"
"  The \"Corresponding Source\" for a work in object code form means all\n"
"the sourc"
                        "e code needed to generate, install, and (for an executable\n"
"work) run the object code and to modify the work, including scripts to\n"
"control those activities.  However, it does not include the work's\n"
"System Libraries, or general-purpose tools or generally available free\n"
"programs which are used unmodified in performing those activities but\n"
"which are not part of the work.  For example, Corresponding Source\n"
"includes interface definition files associated with source files for\n"
"the work, and the source code for shared libraries and dynamically\n"
"linked subprograms that the work is specifically designed to require,\n"
"such as by intimate data communication or control flow between those\n"
"subprograms and other parts of the work.\n"
"\n"
"  The Corresponding Source need not include anything that users\n"
"can regenerate automatically from other parts of the Corresponding\n"
"Source.\n"
"\n"
"  The Corresponding Source for a work in source code form is that\n"
"same work.\n"
"\n"
"  2. Basi"
                        "c Permissions.\n"
"\n"
"  All rights granted under this License are granted for the term of\n"
"copyright on the Program, and are irrevocable provided the stated\n"
"conditions are met.  This License explicitly affirms your unlimited\n"
"permission to run the unmodified Program.  The output from running a\n"
"covered work is covered by this License only if the output, given its\n"
"content, constitutes a covered work.  This License acknowledges your\n"
"rights of fair use or other equivalent, as provided by copyright law.\n"
"\n"
"  You may make, run and propagate covered works that you do not\n"
"convey, without conditions so long as your license otherwise remains\n"
"in force.  You may convey covered works to others for the sole purpose\n"
"of having them make modifications exclusively for you, or provide you\n"
"with facilities for running those works, provided that you comply with\n"
"the terms of this License in conveying all material for which you do\n"
"not control copyright.  Those thus making or runni"
                        "ng the covered works\n"
"for you must do so exclusively on your behalf, under your direction\n"
"and control, on terms that prohibit them from making any copies of\n"
"your copyrighted material outside their relationship with you.\n"
"\n"
"  Conveying under any other circumstances is permitted solely under\n"
"the conditions stated below.  Sublicensing is not allowed; section 10\n"
"makes it unnecessary.\n"
"\n"
"  3. Protecting Users' Legal Rights From Anti-Circumvention Law.\n"
"\n"
"  No covered work shall be deemed part of an effective technological\n"
"measure under any applicable law fulfilling obligations under article\n"
"11 of the WIPO copyright treaty adopted on 20 December 1996, or\n"
"similar laws prohibiting or restricting circumvention of such\n"
"measures.\n"
"\n"
"  When you convey a covered work, you waive any legal power to forbid\n"
"circumvention of technological measures to the extent such circumvention\n"
"is effected by exercising rights under this License with respect to\n"
"the covered"
                        " work, and you disclaim any intention to limit operation or\n"
"modification of the work as a means of enforcing, against the work's\n"
"users, your or third parties' legal rights to forbid circumvention of\n"
"technological measures.\n"
"\n"
"  4. Conveying Verbatim Copies.\n"
"\n"
"  You may convey verbatim copies of the Program's source code as you\n"
"receive it, in any medium, provided that you conspicuously and\n"
"appropriately publish on each copy an appropriate copyright notice;\n"
"keep intact all notices stating that this License and any\n"
"non-permissive terms added in accord with section 7 apply to the code;\n"
"keep intact all notices of the absence of any warranty; and give all\n"
"recipients a copy of this License along with the Program.\n"
"\n"
"  You may charge any price or no price for each copy that you convey,\n"
"and you may offer support or warranty protection for a fee.\n"
"\n"
"  5. Conveying Modified Source Versions.\n"
"\n"
"  You may convey a work based on the Program, or the modif"
                        "ications to\n"
"produce it from the Program, in the form of source code under the\n"
"terms of section 4, provided that you also meet all of these conditions:\n"
"\n"
"    a) The work must carry prominent notices stating that you modified\n"
"    it, and giving a relevant date.\n"
"\n"
"    b) The work must carry prominent notices stating that it is\n"
"    released under this License and any conditions added under section\n"
"    7.  This requirement modifies the requirement in section 4 to\n"
"    \"keep intact all notices\".\n"
"\n"
"    c) You must license the entire work, as a whole, under this\n"
"    License to anyone who comes into possession of a copy.  This\n"
"    License will therefore apply, along with any applicable section 7\n"
"    additional terms, to the whole of the work, and all its parts,\n"
"    regardless of how they are packaged.  This License gives no\n"
"    permission to license the work in any other way, but it does not\n"
"    invalidate such permission if you have separately recei"
                        "ved it.\n"
"\n"
"    d) If the work has interactive user interfaces, each must display\n"
"    Appropriate Legal Notices; however, if the Program has interactive\n"
"    interfaces that do not display Appropriate Legal Notices, your\n"
"    work need not make them do so.\n"
"\n"
"  A compilation of a covered work with other separate and independent\n"
"works, which are not by their nature extensions of the covered work,\n"
"and which are not combined with it such as to form a larger program,\n"
"in or on a volume of a storage or distribution medium, is called an\n"
"\"aggregate\" if the compilation and its resulting copyright are not\n"
"used to limit the access or legal rights of the compilation's users\n"
"beyond what the individual works permit.  Inclusion of a covered work\n"
"in an aggregate does not cause this License to apply to the other\n"
"parts of the aggregate.\n"
"\n"
"  6. Conveying Non-Source Forms.\n"
"\n"
"  You may convey a covered work in object code form under the terms\n"
"of sections 4 an"
                        "d 5, provided that you also convey the\n"
"machine-readable Corresponding Source under the terms of this License,\n"
"in one of these ways:\n"
"\n"
"    a) Convey the object code in, or embodied in, a physical product\n"
"    (including a physical distribution medium), accompanied by the\n"
"    Corresponding Source fixed on a durable physical medium\n"
"    customarily used for software interchange.\n"
"\n"
"    b) Convey the object code in, or embodied in, a physical product\n"
"    (including a physical distribution medium), accompanied by a\n"
"    written offer, valid for at least three years and valid for as\n"
"    long as you offer spare parts or customer support for that product\n"
"    model, to give anyone who possesses the object code either (1) a\n"
"    copy of the Corresponding Source for all the software in the\n"
"    product that is covered by this License, on a durable physical\n"
"    medium customarily used for software interchange, for a price no\n"
"    more than your reasonable cost of "
                        "physically performing this\n"
"    conveying of source, or (2) access to copy the\n"
"    Corresponding Source from a network server at no charge.\n"
"\n"
"    c) Convey individual copies of the object code with a copy of the\n"
"    written offer to provide the Corresponding Source.  This\n"
"    alternative is allowed only occasionally and noncommercially, and\n"
"    only if you received the object code with such an offer, in accord\n"
"    with subsection 6b.\n"
"\n"
"    d) Convey the object code by offering access from a designated\n"
"    place (gratis or for a charge), and offer equivalent access to the\n"
"    Corresponding Source in the same way through the same place at no\n"
"    further charge.  You need not require recipients to copy the\n"
"    Corresponding Source along with the object code.  If the place to\n"
"    copy the object code is a network server, the Corresponding Source\n"
"    may be on a different server (operated by you or a third party)\n"
"    that supports equivalent copying f"
                        "acilities, provided you maintain\n"
"    clear directions next to the object code saying where to find the\n"
"    Corresponding Source.  Regardless of what server hosts the\n"
"    Corresponding Source, you remain obligated to ensure that it is\n"
"    available for as long as needed to satisfy these requirements.\n"
"\n"
"    e) Convey the object code using peer-to-peer transmission, provided\n"
"    you inform other peers where the object code and Corresponding\n"
"    Source of the work are being offered to the general public at no\n"
"    charge under subsection 6d.\n"
"\n"
"  A separable portion of the object code, whose source code is excluded\n"
"from the Corresponding Source as a System Library, need not be\n"
"included in conveying the object code work.\n"
"\n"
"  A \"User Product\" is either (1) a \"consumer product\", which means any\n"
"tangible personal property which is normally used for personal, family,\n"
"or household purposes, or (2) anything designed or sold for incorporation\n"
"into a dw"
                        "elling.  In determining whether a product is a consumer product,\n"
"doubtful cases shall be resolved in favor of coverage.  For a particular\n"
"product received by a particular user, \"normally used\" refers to a\n"
"typical or common use of that class of product, regardless of the status\n"
"of the particular user or of the way in which the particular user\n"
"actually uses, or expects or is expected to use, the product.  A product\n"
"is a consumer product regardless of whether the product has substantial\n"
"commercial, industrial or non-consumer uses, unless such uses represent\n"
"the only significant mode of use of the product.\n"
"\n"
"  \"Installation Information\" for a User Product means any methods,\n"
"procedures, authorization keys, or other information required to install\n"
"and execute modified versions of a covered work in that User Product from\n"
"a modified version of its Corresponding Source.  The information must\n"
"suffice to ensure that the continued functioning of the modified objec"
                        "t\n"
"code is in no case prevented or interfered with solely because\n"
"modification has been made.\n"
"\n"
"  If you convey an object code work under this section in, or with, or\n"
"specifically for use in, a User Product, and the conveying occurs as\n"
"part of a transaction in which the right of possession and use of the\n"
"User Product is transferred to the recipient in perpetuity or for a\n"
"fixed term (regardless of how the transaction is characterized), the\n"
"Corresponding Source conveyed under this section must be accompanied\n"
"by the Installation Information.  But this requirement does not apply\n"
"if neither you nor any third party retains the ability to install\n"
"modified object code on the User Product (for example, the work has\n"
"been installed in ROM).\n"
"\n"
"  The requirement to provide Installation Information does not include a\n"
"requirement to continue to provide support service, warranty, or updates\n"
"for a work that has been modified or installed by the recipient, or for\n"
""
                        "the User Product in which it has been modified or installed.  Access to a\n"
"network may be denied when the modification itself materially and\n"
"adversely affects the operation of the network or violates the rules and\n"
"protocols for communication across the network.\n"
"\n"
"  Corresponding Source conveyed, and Installation Information provided,\n"
"in accord with this section must be in a format that is publicly\n"
"documented (and with an implementation available to the public in\n"
"source code form), and must require no special password or key for\n"
"unpacking, reading or copying.\n"
"\n"
"  7. Additional Terms.\n"
"\n"
"  \"Additional permissions\" are terms that supplement the terms of this\n"
"License by making exceptions from one or more of its conditions.\n"
"Additional permissions that are applicable to the entire Program shall\n"
"be treated as though they were included in this License, to the extent\n"
"that they are valid under applicable law.  If additional permissions\n"
"apply only to pa"
                        "rt of the Program, that part may be used separately\n"
"under those permissions, but the entire Program remains governed by\n"
"this License without regard to the additional permissions.\n"
"\n"
"  When you convey a copy of a covered work, you may at your option\n"
"remove any additional permissions from that copy, or from any part of\n"
"it.  (Additional permissions may be written to require their own\n"
"removal in certain cases when you modify the work.)  You may place\n"
"additional permissions on material, added by you to a covered work,\n"
"for which you have or can give appropriate copyright permission.\n"
"\n"
"  Notwithstanding any other provision of this License, for material you\n"
"add to a covered work, you may (if authorized by the copyright holders of\n"
"that material) supplement the terms of this License with terms:\n"
"\n"
"    a) Disclaiming warranty or limiting liability differently from the\n"
"    terms of sections 15 and 16 of this License; or\n"
"\n"
"    b) Requiring preservation of sp"
                        "ecified reasonable legal notices or\n"
"    author attributions in that material or in the Appropriate Legal\n"
"    Notices displayed by works containing it; or\n"
"\n"
"    c) Prohibiting misrepresentation of the origin of that material, or\n"
"    requiring that modified versions of such material be marked in\n"
"    reasonable ways as different from the original version; or\n"
"\n"
"    d) Limiting the use for publicity purposes of names of licensors or\n"
"    authors of the material; or\n"
"\n"
"    e) Declining to grant rights under trademark law for use of some\n"
"    trade names, trademarks, or service marks; or\n"
"\n"
"    f) Requiring indemnification of licensors and authors of that\n"
"    material by anyone who conveys the material (or modified versions of\n"
"    it) with contractual assumptions of liability to the recipient, for\n"
"    any liability that these contractual assumptions directly impose on\n"
"    those licensors and authors.\n"
"\n"
"  All other non-permissive additional terms a"
                        "re considered \"further\n"
"restrictions\" within the meaning of section 10.  If the Program as you\n"
"received it, or any part of it, contains a notice stating that it is\n"
"governed by this License along with a term that is a further\n"
"restriction, you may remove that term.  If a license document contains\n"
"a further restriction but permits relicensing or conveying under this\n"
"License, you may add to a covered work material governed by the terms\n"
"of that license document, provided that the further restriction does\n"
"not survive such relicensing or conveying.\n"
"\n"
"  If you add terms to a covered work in accord with this section, you\n"
"must place, in the relevant source files, a statement of the\n"
"additional terms that apply to those files, or a notice indicating\n"
"where to find the applicable terms.\n"
"\n"
"  Additional terms, permissive or non-permissive, may be stated in the\n"
"form of a separately written license, or stated as exceptions;\n"
"the above requirements apply either wa"
                        "y.\n"
"\n"
"  8. Termination.\n"
"\n"
"  You may not propagate or modify a covered work except as expressly\n"
"provided under this License.  Any attempt otherwise to propagate or\n"
"modify it is void, and will automatically terminate your rights under\n"
"this License (including any patent licenses granted under the third\n"
"paragraph of section 11).\n"
"\n"
"  However, if you cease all violation of this License, then your\n"
"license from a particular copyright holder is reinstated (a)\n"
"provisionally, unless and until the copyright holder explicitly and\n"
"finally terminates your license, and (b) permanently, if the copyright\n"
"holder fails to notify you of the violation by some reasonable means\n"
"prior to 60 days after the cessation.\n"
"\n"
"  Moreover, your license from a particular copyright holder is\n"
"reinstated permanently if the copyright holder notifies you of the\n"
"violation by some reasonable means, this is the first time you have\n"
"received notice of violation of this License (for"
                        " any work) from that\n"
"copyright holder, and you cure the violation prior to 30 days after\n"
"your receipt of the notice.\n"
"\n"
"  Termination of your rights under this section does not terminate the\n"
"licenses of parties who have received copies or rights from you under\n"
"this License.  If your rights have been terminated and not permanently\n"
"reinstated, you do not qualify to receive new licenses for the same\n"
"material under section 10.\n"
"\n"
"  9. Acceptance Not Required for Having Copies.\n"
"\n"
"  You are not required to accept this License in order to receive or\n"
"run a copy of the Program.  Ancillary propagation of a covered work\n"
"occurring solely as a consequence of using peer-to-peer transmission\n"
"to receive a copy likewise does not require acceptance.  However,\n"
"nothing other than this License grants you permission to propagate or\n"
"modify any covered work.  These actions infringe copyright if you do\n"
"not accept this License.  Therefore, by modifying or propagating a\n"
""
                        "covered work, you indicate your acceptance of this License to do so.\n"
"\n"
"  10. Automatic Licensing of Downstream Recipients.\n"
"\n"
"  Each time you convey a covered work, the recipient automatically\n"
"receives a license from the original licensors, to run, modify and\n"
"propagate that work, subject to this License.  You are not responsible\n"
"for enforcing compliance by third parties with this License.\n"
"\n"
"  An \"entity transaction\" is a transaction transferring control of an\n"
"organization, or substantially all assets of one, or subdividing an\n"
"organization, or merging organizations.  If propagation of a covered\n"
"work results from an entity transaction, each party to that\n"
"transaction who receives a copy of the work also receives whatever\n"
"licenses to the work the party's predecessor in interest had or could\n"
"give under the previous paragraph, plus a right to possession of the\n"
"Corresponding Source of the work from the predecessor in interest, if\n"
"the predecessor has it"
                        " or can get it with reasonable efforts.\n"
"\n"
"  You may not impose any further restrictions on the exercise of the\n"
"rights granted or affirmed under this License.  For example, you may\n"
"not impose a license fee, royalty, or other charge for exercise of\n"
"rights granted under this License, and you may not initiate litigation\n"
"(including a cross-claim or counterclaim in a lawsuit) alleging that\n"
"any patent claim is infringed by making, using, selling, offering for\n"
"sale, or importing the Program or any portion of it.\n"
"\n"
"  11. Patents.\n"
"\n"
"  A \"contributor\" is a copyright holder who authorizes use under this\n"
"License of the Program or a work on which the Program is based.  The\n"
"work thus licensed is called the contributor's \"contributor version\".\n"
"\n"
"  A contributor's \"essential patent claims\" are all patent claims\n"
"owned or controlled by the contributor, whether already acquired or\n"
"hereafter acquired, that would be infringed by some manner, permitted\n"
"by "
                        "this License, of making, using, or selling its contributor version,\n"
"but do not include claims that would be infringed only as a\n"
"consequence of further modification of the contributor version.  For\n"
"purposes of this definition, \"control\" includes the right to grant\n"
"patent sublicenses in a manner consistent with the requirements of\n"
"this License.\n"
"\n"
"  Each contributor grants you a non-exclusive, worldwide, royalty-free\n"
"patent license under the contributor's essential patent claims, to\n"
"make, use, sell, offer for sale, import and otherwise run, modify and\n"
"propagate the contents of its contributor version.\n"
"\n"
"  In the following three paragraphs, a \"patent license\" is any express\n"
"agreement or commitment, however denominated, not to enforce a patent\n"
"(such as an express permission to practice a patent or covenant not to\n"
"sue for patent infringement).  To \"grant\" such a patent license to a\n"
"party means to make such an agreement or commitment not to enforce a"
                        "\n"
"patent against the party.\n"
"\n"
"  If you convey a covered work, knowingly relying on a patent license,\n"
"and the Corresponding Source of the work is not available for anyone\n"
"to copy, free of charge and under the terms of this License, through a\n"
"publicly available network server or other readily accessible means,\n"
"then you must either (1) cause the Corresponding Source to be so\n"
"available, or (2) arrange to deprive yourself of the benefit of the\n"
"patent license for this particular work, or (3) arrange, in a manner\n"
"consistent with the requirements of this License, to extend the patent\n"
"license to downstream recipients.  \"Knowingly relying\" means you have\n"
"actual knowledge that, but for the patent license, your conveying the\n"
"covered work in a country, or your recipient's use of the covered work\n"
"in a country, would infringe one or more identifiable patents in that\n"
"country that you have reason to believe are valid.\n"
"\n"
"  If, pursuant to or in connection with a"
                        " single transaction or\n"
"arrangement, you convey, or propagate by procuring conveyance of, a\n"
"covered work, and grant a patent license to some of the parties\n"
"receiving the covered work authorizing them to use, propagate, modify\n"
"or convey a specific copy of the covered work, then the patent license\n"
"you grant is automatically extended to all recipients of the covered\n"
"work and works based on it.\n"
"\n"
"  A patent license is \"discriminatory\" if it does not include within\n"
"the scope of its coverage, prohibits the exercise of, or is\n"
"conditioned on the non-exercise of one or more of the rights that are\n"
"specifically granted under this License.  You may not convey a covered\n"
"work if you are a party to an arrangement with a third party that is\n"
"in the business of distributing software, under which you make payment\n"
"to the third party based on the extent of your activity of conveying\n"
"the work, and under which the third party grants, to any of the\n"
"parties who would rece"
                        "ive the covered work from you, a discriminatory\n"
"patent license (a) in connection with copies of the covered work\n"
"conveyed by you (or copies made from those copies), or (b) primarily\n"
"for and in connection with specific products or compilations that\n"
"contain the covered work, unless you entered into that arrangement,\n"
"or that patent license was granted, prior to 28 March 2007.\n"
"\n"
"  Nothing in this License shall be construed as excluding or limiting\n"
"any implied license or other defenses to infringement that may\n"
"otherwise be available to you under applicable patent law.\n"
"\n"
"  12. No Surrender of Others' Freedom.\n"
"\n"
"  If conditions are imposed on you (whether by court order, agreement or\n"
"otherwise) that contradict the conditions of this License, they do not\n"
"excuse you from the conditions of this License.  If you cannot convey a\n"
"covered work so as to satisfy simultaneously your obligations under this\n"
"License and any other pertinent obligations, then as a con"
                        "sequence you may\n"
"not convey it at all.  For example, if you agree to terms that obligate you\n"
"to collect a royalty for further conveying from those to whom you convey\n"
"the Program, the only way you could satisfy both those terms and this\n"
"License would be to refrain entirely from conveying the Program.\n"
"\n"
"  13. Use with the GNU Affero General Public License.\n"
"\n"
"  Notwithstanding any other provision of this License, you have\n"
"permission to link or combine any covered work with a work licensed\n"
"under version 3 of the GNU Affero General Public License into a single\n"
"combined work, and to convey the resulting work.  The terms of this\n"
"License will continue to apply to the part which is the covered work,\n"
"but the special requirements of the GNU Affero General Public License,\n"
"section 13, concerning interaction through a network will apply to the\n"
"combination as such.\n"
"\n"
"  14. Revised Versions of this License.\n"
"\n"
"  The Free Software Foundation may publish rev"
                        "ised and/or new versions of\n"
"the GNU General Public License from time to time.  Such new versions will\n"
"be similar in spirit to the present version, but may differ in detail to\n"
"address new problems or concerns.\n"
"\n"
"  Each version is given a distinguishing version number.  If the\n"
"Program specifies that a certain numbered version of the GNU General\n"
"Public License \"or any later version\" applies to it, you have the\n"
"option of following the terms and conditions either of that numbered\n"
"version or of any later version published by the Free Software\n"
"Foundation.  If the Program does not specify a version number of the\n"
"GNU General Public License, you may choose any version ever published\n"
"by the Free Software Foundation.\n"
"\n"
"  If the Program specifies that a proxy can decide which future\n"
"versions of the GNU General Public License can be used, that proxy's\n"
"public statement of acceptance of a version permanently authorizes you\n"
"to choose that version for the Progr"
                        "am.\n"
"\n"
"  Later license versions may give you additional or different\n"
"permissions.  However, no additional obligations are imposed on any\n"
"author or copyright holder as a result of your choosing to follow a\n"
"later version.\n"
"\n"
"  15. Disclaimer of Warranty.\n"
"\n"
"  THERE IS NO WARRANTY FOR THE PROGRAM, TO THE EXTENT PERMITTED BY\n"
"APPLICABLE LAW.  EXCEPT WHEN OTHERWISE STATED IN WRITING THE COPYRIGHT\n"
"HOLDERS AND/OR OTHER PARTIES PROVIDE THE PROGRAM \"AS IS\" WITHOUT WARRANTY\n"
"OF ANY KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING, BUT NOT LIMITED TO,\n"
"THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR\n"
"PURPOSE.  THE ENTIRE RISK AS TO THE QUALITY AND PERFORMANCE OF THE PROGRAM\n"
"IS WITH YOU.  SHOULD THE PROGRAM PROVE DEFECTIVE, YOU ASSUME THE COST OF\n"
"ALL NECESSARY SERVICING, REPAIR OR CORRECTION.\n"
"\n"
"  16. Limitation of Liability.\n"
"\n"
"  IN NO EVENT UNLESS REQUIRED BY APPLICABLE LAW OR AGREED TO IN WRITING\n"
"WILL ANY COPYRIGHT HOLDER, OR ANY"
                        " OTHER PARTY WHO MODIFIES AND/OR CONVEYS\n"
"THE PROGRAM AS PERMITTED ABOVE, BE LIABLE TO YOU FOR DAMAGES, INCLUDING ANY\n"
"GENERAL, SPECIAL, INCIDENTAL OR CONSEQUENTIAL DAMAGES ARISING OUT OF THE\n"
"USE OR INABILITY TO USE THE PROGRAM (INCLUDING BUT NOT LIMITED TO LOSS OF\n"
"DATA OR DATA BEING RENDERED INACCURATE OR LOSSES SUSTAINED BY YOU OR THIRD\n"
"PARTIES OR A FAILURE OF THE PROGRAM TO OPERATE WITH ANY OTHER PROGRAMS),\n"
"EVEN IF SUCH HOLDER OR OTHER PARTY HAS BEEN ADVISED OF THE POSSIBILITY OF\n"
"SUCH DAMAGES.\n"
"\n"
"  17. Interpretation of Sections 15 and 16.\n"
"\n"
"  If the disclaimer of warranty and limitation of liability provided\n"
"above cannot be given local legal effect according to their terms,\n"
"reviewing courts shall apply local law that most closely approximates\n"
"an absolute waiver of all civil liability in connection with the\n"
"Program, unless a warranty or assumption of liability accompanies a\n"
"copy of the Program in return for a fee.\n"
"\n"
"                     END O"
                        "F TERMS AND CONDITIONS\n"
"\n"
"            How to Apply These Terms to Your New Programs\n"
"\n"
"  If you develop a new program, and you want it to be of the greatest\n"
"possible use to the public, the best way to achieve this is to make it\n"
"free software which everyone can redistribute and change under these terms.\n"
"\n"
"  To do so, attach the following notices to the program.  It is safest\n"
"to attach them to the start of each source file to most effectively\n"
"state the exclusion of warranty; and each file should have at least\n"
"the \"copyright\" line and a pointer to where the full notice is found.\n"
"\n"
"    <one line to give the program's name and a brief idea of what it does.>\n"
"    Copyright (C) <year>  <name of author>\n"
"\n"
"    This program is free software: you can redistribute it and/or modify\n"
"    it under the terms of the GNU General Public License as published by\n"
"    the Free Software Foundation, either version 3 of the License, or\n"
"    (at your option) any later v"
                        "ersion.\n"
"\n"
"    This program is distributed in the hope that it will be useful,\n"
"    but WITHOUT ANY WARRANTY; without even the implied warranty of\n"
"    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the\n"
"    GNU General Public License for more details.\n"
"\n"
"    You should have received a copy of the GNU General Public License\n"
"    along with this program.  If not, see <http://www.gnu.org/licenses/>.\n"
"\n"
"Also add information on how to contact you by electronic and paper mail.\n"
"\n"
"  If the program does terminal interaction, make it output a short\n"
"notice like this when it starts in an interactive mode:\n"
"\n"
"    <program>  Copyright (C) <year>  <name of author>\n"
"    This program comes with ABSOLUTELY NO WARRANTY; for details type `show w'.\n"
"    This is free software, and you are welcome to redistribute it\n"
"    under certain conditions; type `show c' for details.\n"
"\n"
"The hypothetical commands `show w' and `show c' should show the appropriate\n"
"parts"
                        " of the General Public License.  Of course, your program's commands\n"
"might be different; for a GUI interface, you would use an \"about box\".\n"
"\n"
"  You should also get your employer (if you work as a programmer) or school,\n"
"if any, to sign a \"copyright disclaimer\" for the program, if necessary.\n"
"For more information on this, and how to apply and follow the GNU GPL, see\n"
"<http://www.gnu.org/licenses/>.\n"
"\n"
"  The GNU General Public License does not permit incorporating your program\n"
"into proprietary programs.  If your program is a subroutine library, you\n"
"may consider it more useful to permit linking proprietary applications with\n"
"the library.  If this is what you want to do, use the GNU Lesser General\n"
"Public License instead of this License.  But first, please read\n"
"<http://www.gnu.org/philosophy/why-not-lgpl.html>.\n"
"\n"
"########################################################\n"
"\n"
"Parts of analog clockwidget:\n"
"###################################################"
                        "#####\n"
"##\n"
"## Copyright (C) 2010 Riverbank Computing Limited.\n"
"## Copyright (C) 2010 Nokia Corporation and/or its subsidiary(-ies).\n"
"## All rights reserved.\n"
"##\n"
"## $QT_BEGIN_LICENSE:BSD$\n"
"## You may use this file under the terms of the BSD license as follows:\n"
"##\n"
"## \"Redistribution and use in source and binary forms, with or without\n"
"## modification, are permitted provided that the following conditions are\n"
"## met:\n"
"##   * Redistributions of source code must retain the above copyright\n"
"##     notice, this list of conditions and the following disclaimer.\n"
"##   * Redistributions in binary form must reproduce the above copyright\n"
"##     notice, this list of conditions and the following disclaimer in\n"
"##     the documentation and/or other materials provided with the\n"
"##     distribution.\n"
"##   * Neither the name of Nokia Corporation and its Subsidiary(-ies) nor\n"
"##     the names of its contributors may be used to endorse or promote\n"
"##     products der"
                        "ived from this software without specific prior written\n"
"##     permission.\n"
"##\n"
"## THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS\n"
"## \"AS IS\" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT\n"
"## LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR\n"
"## A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT\n"
"## OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,\n"
"## SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT\n"
"## LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,\n"
"## DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY\n"
"## THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT\n"
"## (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE\n"
"## OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.\"\n"
"## $QT_END_LICENSE$\n"
"##\n"
"########################################################", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_license), QCoreApplication.translate("Settings", u"License", None))
        self.ExitButton.setText(QCoreApplication.translate("Settings", u"Quit", None))
        self.RebootButton.setText(QCoreApplication.translate("Settings", u"Reboot", None))
        self.ShutdownButton.setText(QCoreApplication.translate("Settings", u"Shutdown", None))
        self.CloseButton.setText(QCoreApplication.translate("Settings", u"Close", None))
        self.ApplyButton.setText(QCoreApplication.translate("Settings", u"Apply && Save", None))
    # retranslateUi

