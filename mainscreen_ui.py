# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainscreen.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

from clockwidget import ClockWidget
from weatherwidget import WeatherWidget
import resources_rc

class Ui_MainScreen(object):
    def setupUi(self, MainScreen):
        if not MainScreen.objectName():
            MainScreen.setObjectName(u"MainScreen")
        MainScreen.setWindowModality(Qt.NonModal)
        MainScreen.setEnabled(True)
        MainScreen.resize(979, 815)
        MainScreen.setMinimumSize(QSize(0, 0))
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Base, brush)
        brush1 = QBrush(QColor(0, 0, 0, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        MainScreen.setPalette(palette)
        icon = QIcon()
        icon.addFile(u":/oas_icon/images/oas_icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainScreen.setWindowIcon(icon)
        MainScreen.setAutoFillBackground(False)
        self.gridLayout = QGridLayout(MainScreen)
        self.gridLayout.setSpacing(2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(5, 5, 5, 5)
        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_5, 9, 0, 1, 1)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.labelStation = QLabel(MainScreen)
        self.labelStation.setObjectName(u"labelStation")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelStation.sizePolicy().hasHeightForWidth())
        self.labelStation.setSizePolicy(sizePolicy)
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        brush2 = QBrush(QColor(146, 145, 144, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        self.labelStation.setPalette(palette1)
        font = QFont()
        font.setFamilies([u"FreeSans"])
        font.setPointSize(24)
        font.setBold(True)
        self.labelStation.setFont(font)
        self.labelStation.setAutoFillBackground(False)
        self.labelStation.setScaledContents(False)
        self.labelStation.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.labelStation)

        self.labelSlogan = QLabel(MainScreen)
        self.labelSlogan.setObjectName(u"labelSlogan")
        self.labelSlogan.setSizeIncrement(QSize(1, 1))
        palette2 = QPalette()
        palette2.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        self.labelSlogan.setPalette(palette2)
        font1 = QFont()
        font1.setFamilies([u"FreeSans"])
        font1.setPointSize(18)
        font1.setBold(True)
        self.labelSlogan.setFont(font1)
        self.labelSlogan.setAutoFillBackground(False)
        self.labelSlogan.setScaledContents(False)
        self.labelSlogan.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.labelSlogan)


        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(5, -1, 5, -1)
        self.labelTextLeft = QLabel(MainScreen)
        self.labelTextLeft.setObjectName(u"labelTextLeft")
        font2 = QFont()
        font2.setFamilies([u"FreeSans"])
        font2.setPointSize(21)
        font2.setBold(True)
        self.labelTextLeft.setFont(font2)
        self.labelTextLeft.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout.addWidget(self.labelTextLeft)

        self.labelTextRight = QLabel(MainScreen)
        self.labelTextRight.setObjectName(u"labelTextRight")
        self.labelTextRight.setFont(font2)
        self.labelTextRight.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.labelTextRight.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.labelTextRight)


        self.gridLayout.addLayout(self.horizontalLayout, 10, 0, 1, 2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(2, 2, 2, 2)
        self.clockWidget = ClockWidget(MainScreen)
        self.clockWidget.setObjectName(u"clockWidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.clockWidget.sizePolicy().hasHeightForWidth())
        self.clockWidget.setSizePolicy(sizePolicy1)
        self.clockWidget.setMinimumSize(QSize(530, 0))
        self.clockWidget.setAutoFillBackground(False)
        self.clockWidget.setProperty(u"clockType", 1)

        self.verticalLayout_3.addWidget(self.clockWidget)


        self.gridLayout.addLayout(self.verticalLayout_3, 1, 1, 9, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_4, 4, 0, 1, 1)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_7, 7, 0, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.buttonLED1 = QLabel(MainScreen)
        self.buttonLED1.setObjectName(u"buttonLED1")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.buttonLED1.sizePolicy().hasHeightForWidth())
        self.buttonLED1.setSizePolicy(sizePolicy2)
        self.buttonLED1.setMinimumSize(QSize(230, 120))
        self.buttonLED1.setFont(font)
        self.buttonLED1.setStyleSheet(u"background-color: rgb(255, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.buttonLED1.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.buttonLED1)

        self.verticalSpacer = QSpacerItem(20, 5, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.MinimumExpanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.buttonLED2 = QLabel(MainScreen)
        self.buttonLED2.setObjectName(u"buttonLED2")
        sizePolicy2.setHeightForWidth(self.buttonLED2.sizePolicy().hasHeightForWidth())
        self.buttonLED2.setSizePolicy(sizePolicy2)
        self.buttonLED2.setMinimumSize(QSize(230, 120))
        self.buttonLED2.setFont(font)
        self.buttonLED2.setStyleSheet(u"background-color: rgb(220, 220, 0);\n"
"color: rgb(255, 255, 255);")
        self.buttonLED2.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.buttonLED2)

        self.verticalSpacer_2 = QSpacerItem(20, 5, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.MinimumExpanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.buttonLED3 = QLabel(MainScreen)
        self.buttonLED3.setObjectName(u"buttonLED3")
        sizePolicy2.setHeightForWidth(self.buttonLED3.sizePolicy().hasHeightForWidth())
        self.buttonLED3.setSizePolicy(sizePolicy2)
        self.buttonLED3.setMinimumSize(QSize(230, 120))
        self.buttonLED3.setFont(font)
        self.buttonLED3.setStyleSheet(u"background-color: rgb(0, 200, 200);\n"
"color: rgb(255, 255, 255);")
        self.buttonLED3.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.buttonLED3)

        self.verticalSpacer_3 = QSpacerItem(20, 5, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.MinimumExpanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.buttonLED4 = QLabel(MainScreen)
        self.buttonLED4.setObjectName(u"buttonLED4")
        self.buttonLED4.setMinimumSize(QSize(230, 120))
        self.buttonLED4.setFont(font)
        self.buttonLED4.setStyleSheet(u"background-color: rgb(255, 0, 255);\n"
"color: rgb(255, 255, 255);")
        self.buttonLED4.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.buttonLED4)

        self.verticalLayout.setStretch(0, 10)
        self.verticalLayout.setStretch(1, 1)
        self.verticalLayout.setStretch(2, 10)
        self.verticalLayout.setStretch(3, 1)
        self.verticalLayout.setStretch(4, 10)
        self.verticalLayout.setStretch(5, 1)
        self.verticalLayout.setStretch(6, 10)

        self.gridLayout.addLayout(self.verticalLayout, 1, 2, 10, 1)

        self.LayoutBottom = QVBoxLayout()
        self.LayoutBottom.setObjectName(u"LayoutBottom")
        self.labelCurrentSong = QLabel(MainScreen)
        self.labelCurrentSong.setObjectName(u"labelCurrentSong")
        self.labelCurrentSong.setEnabled(True)
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.labelCurrentSong.sizePolicy().hasHeightForWidth())
        self.labelCurrentSong.setSizePolicy(sizePolicy3)
        self.labelCurrentSong.setFont(font2)
        self.labelCurrentSong.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.labelCurrentSong.setAlignment(Qt.AlignCenter)

        self.LayoutBottom.addWidget(self.labelCurrentSong)

        self.labelNews = QLabel(MainScreen)
        self.labelNews.setObjectName(u"labelNews")
        self.labelNews.setEnabled(True)
        sizePolicy3.setHeightForWidth(self.labelNews.sizePolicy().hasHeightForWidth())
        self.labelNews.setSizePolicy(sizePolicy3)
        font3 = QFont()
        font3.setFamilies([u"FreeSans"])
        font3.setPointSize(15)
        font3.setBold(True)
        self.labelNews.setFont(font3)
        self.labelNews.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.labelNews.setAlignment(Qt.AlignCenter)

        self.LayoutBottom.addWidget(self.labelNews)

        self.labelWarning = QLabel(MainScreen)
        self.labelWarning.setObjectName(u"labelWarning")
        sizePolicy3.setHeightForWidth(self.labelWarning.sizePolicy().hasHeightForWidth())
        self.labelWarning.setSizePolicy(sizePolicy3)
        font4 = QFont()
        font4.setFamilies([u"FreeSans"])
        font4.setPointSize(14)
        font4.setBold(True)
        self.labelWarning.setFont(font4)
        self.labelWarning.setStyleSheet(u"background-color: rgb(255, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.labelWarning.setAlignment(Qt.AlignCenter)

        self.LayoutBottom.addWidget(self.labelWarning)


        self.gridLayout.addLayout(self.LayoutBottom, 11, 0, 1, 3)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_6, 3, 0, 1, 1)

        self.AirLED_1 = QFrame(MainScreen)
        self.AirLED_1.setObjectName(u"AirLED_1")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.AirLED_1.sizePolicy().hasHeightForWidth())
        self.AirLED_1.setSizePolicy(sizePolicy4)
        self.AirLED_1.setMaximumSize(QSize(221, 16777215))
        self.horizontalLayout_2 = QHBoxLayout(self.AirLED_1)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 5)
        self.AirIcon_1 = QLabel(self.AirLED_1)
        self.AirIcon_1.setObjectName(u"AirIcon_1")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.AirIcon_1.sizePolicy().hasHeightForWidth())
        self.AirIcon_1.setSizePolicy(sizePolicy5)
        self.AirIcon_1.setStyleSheet(u"background-color: rgb(255, 0, 0);")
        self.AirIcon_1.setFrameShadow(QFrame.Plain)
        self.AirIcon_1.setPixmap(QPixmap(u":/mic_icon.png/images/mic_icon.png"))
        self.AirIcon_1.setScaledContents(False)
        self.AirIcon_1.setMargin(5)

        self.horizontalLayout_2.addWidget(self.AirIcon_1)

        self.AirLabel_1 = QLabel(self.AirLED_1)
        self.AirLabel_1.setObjectName(u"AirLabel_1")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Minimum)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.AirLabel_1.sizePolicy().hasHeightForWidth())
        self.AirLabel_1.setSizePolicy(sizePolicy6)
        self.AirLabel_1.setMinimumSize(QSize(140, 0))
        self.AirLabel_1.setMaximumSize(QSize(16777215, 16777215))
        self.AirLabel_1.setFont(font)
        self.AirLabel_1.setStyleSheet(u"background-color: rgb(255, 0, 0);")
        self.AirLabel_1.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.AirLabel_1)


        self.gridLayout.addWidget(self.AirLED_1, 1, 0, 1, 1)

        self.AirLED_4 = QFrame(MainScreen)
        self.AirLED_4.setObjectName(u"AirLED_4")
        sizePolicy4.setHeightForWidth(self.AirLED_4.sizePolicy().hasHeightForWidth())
        self.AirLED_4.setSizePolicy(sizePolicy4)
        self.AirLED_4.setMaximumSize(QSize(221, 16777215))
        self.AirLED_4.setFrameShape(QFrame.NoFrame)
        self.AirLED_4.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_3 = QHBoxLayout(self.AirLED_4)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 5)
        self.AirIcon_4 = QLabel(self.AirLED_4)
        self.AirIcon_4.setObjectName(u"AirIcon_4")
        sizePolicy5.setHeightForWidth(self.AirIcon_4.sizePolicy().hasHeightForWidth())
        self.AirIcon_4.setSizePolicy(sizePolicy5)
        self.AirIcon_4.setMaximumSize(QSize(59, 109))
        self.AirIcon_4.setStyleSheet(u"background-color: rgb(255, 0, 0);")
        self.AirIcon_4.setFrameShadow(QFrame.Plain)
        self.AirIcon_4.setPixmap(QPixmap(u":/stream_icon/images/antenna2.png"))
        self.AirIcon_4.setScaledContents(True)
        self.AirIcon_4.setMargin(5)

        self.horizontalLayout_3.addWidget(self.AirIcon_4)

        self.AirLabel_4 = QLabel(self.AirLED_4)
        self.AirLabel_4.setObjectName(u"AirLabel_4")
        sizePolicy6.setHeightForWidth(self.AirLabel_4.sizePolicy().hasHeightForWidth())
        self.AirLabel_4.setSizePolicy(sizePolicy6)
        self.AirLabel_4.setMinimumSize(QSize(140, 0))
        self.AirLabel_4.setMaximumSize(QSize(16777215, 16777215))
        self.AirLabel_4.setFont(font)
        self.AirLabel_4.setStyleSheet(u"background-color: rgb(255, 0, 0);")
        self.AirLabel_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.AirLabel_4)


        self.gridLayout.addWidget(self.AirLED_4, 6, 0, 1, 1)

        self.AirLED_3 = QFrame(MainScreen)
        self.AirLED_3.setObjectName(u"AirLED_3")
        sizePolicy4.setHeightForWidth(self.AirLED_3.sizePolicy().hasHeightForWidth())
        self.AirLED_3.setSizePolicy(sizePolicy4)
        self.AirLED_3.setMaximumSize(QSize(221, 16777215))
        self.horizontalLayout_32 = QHBoxLayout(self.AirLED_3)
        self.horizontalLayout_32.setSpacing(0)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.horizontalLayout_32.setContentsMargins(0, 0, 0, 5)
        self.AirIcon_3 = QLabel(self.AirLED_3)
        self.AirIcon_3.setObjectName(u"AirIcon_3")
        sizePolicy5.setHeightForWidth(self.AirIcon_3.sizePolicy().hasHeightForWidth())
        self.AirIcon_3.setSizePolicy(sizePolicy5)
        self.AirIcon_3.setStyleSheet(u"background-color: rgb(255, 0, 0);")
        self.AirIcon_3.setFrameShadow(QFrame.Plain)
        self.AirIcon_3.setPixmap(QPixmap(u":/timer_icon/images/timer_icon.png"))
        self.AirIcon_3.setScaledContents(False)
        self.AirIcon_3.setMargin(5)

        self.horizontalLayout_32.addWidget(self.AirIcon_3)

        self.AirLabel_3 = QLabel(self.AirLED_3)
        self.AirLabel_3.setObjectName(u"AirLabel_3")
        sizePolicy6.setHeightForWidth(self.AirLabel_3.sizePolicy().hasHeightForWidth())
        self.AirLabel_3.setSizePolicy(sizePolicy6)
        self.AirLabel_3.setMinimumSize(QSize(140, 0))
        self.AirLabel_3.setMaximumSize(QSize(16777215, 16777215))
        self.AirLabel_3.setFont(font)
        self.AirLabel_3.setStyleSheet(u"background-color: rgb(255, 0, 0);")
        self.AirLabel_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_32.addWidget(self.AirLabel_3)


        self.gridLayout.addWidget(self.AirLED_3, 5, 0, 1, 1)

        self.AirLED_2 = QFrame(MainScreen)
        self.AirLED_2.setObjectName(u"AirLED_2")
        sizePolicy4.setHeightForWidth(self.AirLED_2.sizePolicy().hasHeightForWidth())
        self.AirLED_2.setSizePolicy(sizePolicy4)
        self.AirLED_2.setMaximumSize(QSize(221, 16777215))
        self.Air2HorizontalLayout = QHBoxLayout(self.AirLED_2)
        self.Air2HorizontalLayout.setSpacing(0)
        self.Air2HorizontalLayout.setObjectName(u"Air2HorizontalLayout")
        self.Air2HorizontalLayout.setContentsMargins(0, 5, 0, 5)
        self.AirIcon_2 = QLabel(self.AirLED_2)
        self.AirIcon_2.setObjectName(u"AirIcon_2")
        sizePolicy5.setHeightForWidth(self.AirIcon_2.sizePolicy().hasHeightForWidth())
        self.AirIcon_2.setSizePolicy(sizePolicy5)
        self.AirIcon_2.setStyleSheet(u"background-color: rgb(255, 0, 0);")
        self.AirIcon_2.setFrameShadow(QFrame.Plain)
        self.AirIcon_2.setPixmap(QPixmap(u":/phone_icon/images/phone_icon.png"))
        self.AirIcon_2.setScaledContents(False)
        self.AirIcon_2.setMargin(5)

        self.Air2HorizontalLayout.addWidget(self.AirIcon_2)

        self.AirLabel_2 = QLabel(self.AirLED_2)
        self.AirLabel_2.setObjectName(u"AirLabel_2")
        sizePolicy6.setHeightForWidth(self.AirLabel_2.sizePolicy().hasHeightForWidth())
        self.AirLabel_2.setSizePolicy(sizePolicy6)
        self.AirLabel_2.setMinimumSize(QSize(140, 0))
        self.AirLabel_2.setMaximumSize(QSize(16777215, 16777215))
        self.AirLabel_2.setFont(font)
        self.AirLabel_2.setStyleSheet(u"background-color: rgb(255, 0, 0);")
        self.AirLabel_2.setAlignment(Qt.AlignCenter)

        self.Air2HorizontalLayout.addWidget(self.AirLabel_2)


        self.gridLayout.addWidget(self.AirLED_2, 2, 0, 1, 1)

        self.weatherWidget = WeatherWidget(MainScreen)
        self.weatherWidget.setObjectName(u"weatherWidget")
        sizePolicy4.setHeightForWidth(self.weatherWidget.sizePolicy().hasHeightForWidth())
        self.weatherWidget.setSizePolicy(sizePolicy4)
        self.weatherWidget.setMinimumSize(QSize(0, 135))

        self.gridLayout.addWidget(self.weatherWidget, 8, 0, 1, 1)

#if QT_CONFIG(shortcut)
        self.AirIcon_4.setBuddy(self.AirIcon_4)
        self.AirLabel_4.setBuddy(self.AirLabel_4)
#endif // QT_CONFIG(shortcut)

        self.retranslateUi(MainScreen)

        QMetaObject.connectSlotsByName(MainScreen)
    # setupUi

    def retranslateUi(self, MainScreen):
        MainScreen.setWindowTitle(QCoreApplication.translate("MainScreen", u"OnAirScreen", None))
        self.labelStation.setText(QCoreApplication.translate("MainScreen", u"labelStation", None))
        self.labelSlogan.setText(QCoreApplication.translate("MainScreen", u"labelSlogan", None))
        self.labelTextLeft.setText(QCoreApplication.translate("MainScreen", u"labelTextLeft", None))
        self.labelTextRight.setText(QCoreApplication.translate("MainScreen", u"labelTextRight", None))
        self.buttonLED1.setText(QCoreApplication.translate("MainScreen", u"LED1", None))
        self.buttonLED2.setText(QCoreApplication.translate("MainScreen", u"LED2", None))
        self.buttonLED3.setText(QCoreApplication.translate("MainScreen", u"LED3", None))
        self.buttonLED4.setText(QCoreApplication.translate("MainScreen", u"LED4", None))
        self.labelCurrentSong.setText(QCoreApplication.translate("MainScreen", u"labelCurrentSong", None))
        self.labelNews.setText(QCoreApplication.translate("MainScreen", u"labelNews", None))
        self.labelWarning.setText(QCoreApplication.translate("MainScreen", u"labelWarning", None))
        self.AirIcon_1.setText("")
        self.AirLabel_1.setText(QCoreApplication.translate("MainScreen", u"Mic\n"
"0:00", None))
        self.AirIcon_4.setText("")
        self.AirLabel_4.setText(QCoreApplication.translate("MainScreen", u"Stream\n"
"0:00", None))
        self.AirIcon_3.setText("")
        self.AirLabel_3.setText(QCoreApplication.translate("MainScreen", u"Timer\n"
"0:00", None))
        self.AirIcon_2.setText("")
        self.AirLabel_2.setText(QCoreApplication.translate("MainScreen", u"Phone\n"
"0:00", None))
    # retranslateUi

