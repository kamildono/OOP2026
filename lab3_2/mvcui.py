# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mvcui.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QMenuBar, QSizePolicy, QSlider, QSpinBox,
    QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.spinBox_1 = QSpinBox(self.centralwidget)
        self.spinBox_1.setObjectName(u"spinBox_1")
        self.spinBox_1.setGeometry(QRect(150, 230, 42, 22))
        self.spinBox_1.setMinimum(-1999)
        self.spinBox_1.setMaximum(1999)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(120, 280, 500, 100))
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.verticalSlider_1 = QSlider(self.centralwidget)
        self.verticalSlider_1.setObjectName(u"verticalSlider_1")
        self.verticalSlider_1.setGeometry(QRect(240, 90, 22, 160))
        self.verticalSlider_1.setMinimum(-500)
        self.verticalSlider_1.setMaximum(500)
        self.verticalSlider_1.setOrientation(Qt.Orientation.Vertical)
        self.verticalSlider_2 = QSlider(self.centralwidget)
        self.verticalSlider_2.setObjectName(u"verticalSlider_2")
        self.verticalSlider_2.setGeometry(QRect(460, 90, 22, 160))
        self.verticalSlider_2.setMinimum(-500)
        self.verticalSlider_2.setMaximum(500)
        self.verticalSlider_2.setOrientation(Qt.Orientation.Vertical)
        self.spinBox_2 = QSpinBox(self.centralwidget)
        self.spinBox_2.setObjectName(u"spinBox_2")
        self.spinBox_2.setGeometry(QRect(370, 230, 42, 22))
        self.spinBox_2.setMinimum(-1999)
        self.spinBox_2.setMaximum(1999)
        self.verticalSlider_3 = QSlider(self.centralwidget)
        self.verticalSlider_3.setObjectName(u"verticalSlider_3")
        self.verticalSlider_3.setGeometry(QRect(670, 90, 22, 160))
        self.verticalSlider_3.setMinimum(-500)
        self.verticalSlider_3.setMaximum(500)
        self.verticalSlider_3.setOrientation(Qt.Orientation.Vertical)
        self.spinBox_3 = QSpinBox(self.centralwidget)
        self.spinBox_3.setObjectName(u"spinBox_3")
        self.spinBox_3.setGeometry(QRect(580, 230, 42, 22))
        self.spinBox_3.setMinimum(-1999)
        self.spinBox_3.setMaximum(1999)
        self.lineEdit_1 = QLineEdit(self.centralwidget)
        self.lineEdit_1.setObjectName(u"lineEdit_1")
        self.lineEdit_1.setGeometry(QRect(120, 150, 113, 22))
        self.lineEdit_2 = QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(340, 150, 113, 22))
        self.lineEdit_3 = QLineEdit(self.centralwidget)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(550, 150, 113, 22))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"A <= B <= C", None))
    # retranslateUi

