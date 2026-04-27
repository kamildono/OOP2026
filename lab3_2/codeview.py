import sys

from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QMainWindow, QApplication

from mvcui import Ui_MainWindow
from codemvc import Model

class MyWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        self.__a = 0
        self.__b = 0
        self.__c = 0

        super().__init__()
        self.setupUi(self)

        self.label.setPixmap(QPixmap('laba3_2.png'))

        self.model = Model()
        self.model.addObersver(self)
        self.model.notify()

        self.spinBox_1.editingFinished.connect(lambda: self.onChangedA(self.spinBox_1.value()))
        self.spinBox_2.editingFinished.connect(lambda: self.onChangedB(self.spinBox_2.value()))
        self.spinBox_3.editingFinished.connect(lambda: self.onChangedC(self.spinBox_3.value()))

        self.lineEdit_1.editingFinished.connect(lambda: self.onChangedA(self.lineEdit_1.text()))
        self.lineEdit_2.editingFinished.connect(lambda: self.onChangedB(self.lineEdit_2.text()))
        self.lineEdit_3.editingFinished.connect(lambda: self.onChangedC(self.lineEdit_3.text()))

        self.verticalSlider_1.sliderReleased.connect(lambda: self.onChangedA(self.verticalSlider_1.value()))
        self.verticalSlider_2.sliderReleased.connect(lambda: self.onChangedB(self.verticalSlider_2.value()))
        self.verticalSlider_3.sliderReleased.connect(lambda: self.onChangedC(self.verticalSlider_3.value()))

    def onChangedA(self, val):
        print("def changedA(self, val)", val)

        try:
            val = int(val)
        except:
            self.setValues()
            return

        if val == self.__a:
            print('nothing changed, aborting package')
            self.setValues()
            return

        self.model.setA(val)

    def onChangedB(self, val):
        print("def changedB(self, val)", val)

        try:
            val = int(val)
        except:
            self.setValues()
            return

        if val == self.__b:
            print('nothing changed, aborting package')
            self.setValues()
            return

        self.model.setB(val)

    def onChangedC(self, val):
        print("def changedC(self, val)", val)

        try:
            val = int(val)
        except:
            self.setValues()
            return

        if val == self.__c:
            print('nothing changed, aborting package')
            self.setValues()
            return

        self.model.setC(val)

    def setValues(self, a=None, b=None, c=None):
        if a is not None:
            self.__a = a
        if b is not None:
            self.__b = b
        if c is not None:
            self.__c = c

        self.lineEdit_1.setText(str(self.__a))
        self.spinBox_1.setValue(int(self.__a))
        self.verticalSlider_1.setValue(int(self.__a))

        self.lineEdit_2.setText(str(self.__b))
        self.spinBox_2.setValue(int(self.__b))
        self.verticalSlider_2.setValue(int(self.__b))

        self.lineEdit_3.setText(str(self.__c))
        self.spinBox_3.setValue(int(self.__c))
        self.verticalSlider_3.setValue(int(self.__c))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("windowsvista")
    w = MyWindow()
    w.show()
    sys.exit(app.exec())