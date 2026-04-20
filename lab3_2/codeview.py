import sys

from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QMainWindow, QApplication

from mvcui import Ui_MainWindow
from codemvc import Model

class MyWindow(QMainWindow, Ui_MainWindow):
    __number_elems = 3
    __textes = ['' for i in range(__number_elems)]
    __spins = [0 for i in range(__number_elems)]
    __sliders = [0 for i in range(__number_elems)]
    __a = 0
    __b = 0
    __c = 0

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.label.setPixmap(QPixmap('laba3_2.png'))

        self.m = Model(self)
        # self.m.observers.append(self)

        self.spinBox_1.editingFinished.connect(self.sendToModel)
        self.spinBox_2.editingFinished.connect(self.sendToModel)
        self.spinBox_3.editingFinished.connect(self.sendToModel)

        self.lineEdit_1.editingFinished.connect(self.sendToModel)
        self.lineEdit_2.editingFinished.connect(self.sendToModel)
        self.lineEdit_3.editingFinished.connect(self.sendToModel)

        self.verticalSlider_1.sliderReleased.connect(self.sendToModel)
        self.verticalSlider_2.sliderReleased.connect(self.sendToModel)
        self.verticalSlider_3.sliderReleased.connect(self.sendToModel)

    def sendToModel(self):
        t1 = self.lineEdit_1.text()
        s1 = self.spinBox_1.value()
        v1 = self.verticalSlider_1.value()

        t2 = self.lineEdit_2.text()
        s2 = self.spinBox_2.value()
        v2 = self.verticalSlider_2.value()

        t3 = self.lineEdit_3.text()
        s3 = self.spinBox_3.value()
        v3 = self.verticalSlider_3.value()

        t1, t2, t3 = self.correctStr(t1, t2, t3)
        new_values = [t1, s1, v1, t2, s2, v2, t3, s3, v3]
        old_values = self.getValues1D()
        print("new_values, old_values", new_values, old_values)

        temp_a = self.__a
        temp_b = self.__b
        temp_c = self.__c
        for i, (x, y) in enumerate(zip(new_values, old_values)):
            x = int(x)
            y = int(y)

            if x == y:
                continue
            if i < self.__number_elems:
                temp_a = x
            elif self.__number_elems <= i < self.__number_elems*2:
                temp_b = x
            elif i >= self.__number_elems*2:
                temp_c = x

        if not self.checkChanges(old_values, new_values):
            print('nothing changed, aborting package')
            self.updateFromSelf()
            return

        send_arr = [temp_a, temp_b, temp_c]
        print("***** SENDING TO MODEL *****")
        print("def sendToModel(self):", *send_arr)
        self.m.recieveValues(send_arr)

    def updateFromModel(self, objectt):
        print("** UPDATE BY MODL **")
        print(objectt)

        for i, e in enumerate(objectt):
            print('e:', e)
            self.__textes[i] = str(e)
            self.__spins[i] = int(e)
            self.__sliders[i] = int(e)
        self.setValues()

    def updateFromSelf(self):
        print("** UPDATE BY SELF **")
        self.setValues()

    def setValues(self) -> None:
        self.lineEdit_1.setText(self.__textes[0])
        self.spinBox_1.setValue(self.__spins[0])
        self.verticalSlider_1.setValue(self.__sliders[0])
        self.__a = self.__spins[0]

        self.lineEdit_2.setText(self.__textes[1])
        self.spinBox_2.setValue(self.__spins[1])
        self.verticalSlider_2.setValue(self.__sliders[1])
        self.__b = self.__spins[1]

        self.lineEdit_3.setText(self.__textes[2])
        self.spinBox_3.setValue(self.__spins[2])
        self.verticalSlider_3.setValue(self.__sliders[2])
        self.__c = self.__spins[2]

    def getValues1D(self):
        arr = []
        for i in range(self.__number_elems):
            arr.append(self.__textes[i])
            arr.append(self.__spins[i])
            arr.append(self.__sliders[i])

        return arr

    def getValues2D(self):
        arr = [self.__textes, self.__spins, self.__sliders]
        return arr

    def checkChanges(self, were, now):
        for x, y in zip(were, now):
            #print('x,y:', x, y)
            if x != y:
                return True
        return False

    def correctStr(self, *args):
        buf = []
        arr = []
        reserve = " ".join(map(str, [i**2 for i in range(4, 4+self.__number_elems)]))
        reserve = list(map(int, reserve.split()))

        if args is not None:
            arr = args
        else:
            arr = self.__textes
        for i, e in enumerate(arr):
            print(e)
            if e.isdecimal():
                buf.append(e)
                continue

            to_buf = self.__textes[i]
            if not to_buf.isdecimal():
                to_buf = reserve[i]

            buf.append(to_buf)
        return buf


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MyWindow()
    w.show()
    sys.exit(app.exec())