# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'test.ui'
##
## Created by: Qt User Interface Compiler version 6.11.0
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
from PySide6.QtWidgets import (QApplication, QCalendarWidget, QCheckBox, QDial,
    QGridLayout, QLabel, QMainWindow, QMenuBar,
    QProgressBar, QPushButton, QRadioButton, QScrollArea,
    QSizePolicy, QSlider, QSpacerItem, QStatusBar,
    QTabWidget, QTimeEdit, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(826, 475)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setEnabled(True)
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 2, 0, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_4, 1, 1, 1, 1)

        self.horizontalSlider = QSlider(self.centralwidget)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setOrientation(Qt.Orientation.Horizontal)

        self.gridLayout.addWidget(self.horizontalSlider, 3, 0, 1, 1)

        self.label3 = QLabel(self.centralwidget)
        self.label3.setObjectName(u"label3")

        self.gridLayout.addWidget(self.label3, 5, 3, 1, 1)

        self.label2 = QLabel(self.centralwidget)
        self.label2.setObjectName(u"label2")
        self.label2.setMouseTracking(False)

        self.gridLayout.addWidget(self.label2, 4, 2, 1, 1)

        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.dial = QDial(self.tab)
        self.dial.setObjectName(u"dial")
        self.dial.setGeometry(QRect(9, 9, 100, 100))
        self.timeEdit = QTimeEdit(self.tab)
        self.timeEdit.setObjectName(u"timeEdit")
        self.timeEdit.setGeometry(QRect(100, 20, 48, 22))
        self.label1 = QLabel(self.tab)
        self.label1.setObjectName(u"label1")
        self.label1.setGeometry(QRect(110, 130, 49, 16))
        self.progressBar = QProgressBar(self.tab)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(30, 180, 118, 23))
        self.progressBar.setValue(24)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_3 = QGridLayout(self.tab_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_2, 0, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer, 3, 0, 1, 1)

        self.calendarWidget = QCalendarWidget(self.tab_2)
        self.calendarWidget.setObjectName(u"calendarWidget")

        self.gridLayout_3.addWidget(self.calendarWidget, 1, 0, 2, 2)

        self.radioButton = QRadioButton(self.tab_2)
        self.radioButton.setObjectName(u"radioButton")

        self.gridLayout_3.addWidget(self.radioButton, 0, 0, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_3, 1, 2, 1, 1)

        self.tabWidget.addTab(self.tab_2, "")

        self.gridLayout.addWidget(self.tabWidget, 1, 0, 1, 1)

        self.checkBox = QCheckBox(self.centralwidget)
        self.checkBox.setObjectName(u"checkBox")

        self.gridLayout.addWidget(self.checkBox, 0, 1, 1, 1)

        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setMinimumSize(QSize(100, 100))
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.scrollArea.setWidgetResizable(False)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 198, 317))
        self.pushButton = QPushButton(self.scrollAreaWidgetContents)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(60, 146, 75, 24))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout.addWidget(self.scrollArea, 0, 2, 2, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setEnabled(True)
        self.menubar.setGeometry(QRect(0, 0, 826, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        self.statusbar.setEnabled(True)
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.dial.rangeChanged.connect(self.timeEdit.stepUp)
        self.horizontalSlider.valueChanged.connect(self.tabWidget.setCurrentIndex)
        self.dial.actionTriggered.connect(self.label1.setNum)
        self.dial.valueChanged.connect(self.progressBar.setValue)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label3.setText(QCoreApplication.translate("MainWindow", u"Event", None))
        self.label2.setText(QCoreApplication.translate("MainWindow", u"Mouse", None))
        self.label1.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Tab 1", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"RadioButton", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Tab 2", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u0411\u043e\u043b\u044c\u0448\u0435!", None))
    # retranslateUi

