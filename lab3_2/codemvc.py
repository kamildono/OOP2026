import sys
from random import randint

from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QMainWindow, QApplication

from mvcui import Ui_MainWindow

path_to_txt = 'data.txt'
limits = [0, 100]

class Model:
    __a = 0
    __b = 0
    __c = 0

    observers = []
    def __init__(self, subscriber=None):
        if subscriber is not None:
            self.observers.append(subscriber)

        with open(path_to_txt, 'r') as f:
            data = f.readline()
        #print(data, type(data))

        try:
            self.__a, self.__b, self.__c = data.split()
            print("try", self.__a, self.__b, self.__c)
            self.__a = int(self.__a)
            self.__b = int(self.__b)
            self.__c = int(self.__c)


        except:
            print('Something went terribly wrong!')
            sys.exit()
        f.close()
        print('init', self.__a, self.__b, self.__c)
        self.writeValues([[self.__a], [self.__b], [self.__c]])
        print(self.observers)

    def writeFile(self):

        if not isinstance(self.__a, int):
            if isinstance(self.__a, str) and self.__a.isdecimal():
                self.__a = int(self.__a)
            else: self.__a = 0
            print('a was not an integer!')

        if not isinstance(self.__b, int):
            if isinstance(self.__b, str) and self.__b.isdecimal():
                self.__b = int(self.__b)
            else:
                self.__b = 50
            print('b was not an integer!')

        if not isinstance(self.__c, int):
            if isinstance(self.__c, str) and self.__c.isdecimal():
                self.__c = int(self.__c)
            else:
                self.__c = 100
            print('c was not an integer!')

        print('writeFile', self.__a, self.__b, self.__c)
        with open(path_to_txt, 'w') as f:
            f.write(str(self.__a) + ' ' + str(self.__b) + ' ' + str(self.__c))
        f.close()

    def getAll(self):
        return [self.__a, self.__b, self.__c ]

    def sendValue(self):
        print('***** SENDING TO UI! *****')
        for e in self.observers:
            e.updateFromModel(self.getAll())

    def recieveValues(self, object):
        print("def recieveValues(self, object):", *object)

        textes = object[0:3]
        spins = object[3:6]
        sliders = object[6:9]

        two_d_data = [textes, spins, sliders]

        self.writeValues(two_d_data)

    def correctValues(self, two_d_data):
        #a = self.correctA(two_d_data[0])
        print('checking a')
        a = self.correctUnified(two_d_data[0], self.__a)
        if a < limits[0]:
            a = limits[0]
        else: a = min(a, limits[1])
        flag_a = (a != self.__a)

        #c = self.correctC(two_d_data[2])
        print('checking c')
        c = self.correctUnified(two_d_data[2], self.__c)
        if c > limits[1]:
            c = limits[1]
        else:
            c = max(c, limits[0])
        flag_c = (c != self.__c)

        # b = self.correctB(two_d_data[1])
        print('checking b')
        b = self.correctUnified(two_d_data[1], self.__b)
        if b < a:
            b = a
        elif b > c:
            b = c
        flag_b = (b != self.__b)

        print(flag_a, flag_b, flag_c)
        while not a <= b <= c:
            print('chort!')
            if flag_b and (b > c or b < a):
                print("changing b")
                b = self.__b
            if flag_a:
                print("changing a")
                if a <= b:
                    continue
                b = min(a + randint(1, 5), limits[1])
                if a <= c:
                    continue
                c = min(b + randint(1, 5), limits[1])
                #continue
            if flag_c:
                print("changing c")
                if c >= b:
                    continue
                b = max(c - randint(1, 5), limits[0])
                if c >= a:
                    continue
                a = max(b - randint(1, 5), limits[0])

        changed_data = [a, b, c]
        return changed_data

    def correctUnified(self, arr, self_what):
        print("def correctUnifed() array :", arr)
        users_value = self_what
        for x in arr:
            if isinstance(x, str):
                if not x.isdecimal():
                    break
            if int(x) == self_what:
                continue
            users_value = int(x)
        print("def correctUnifed() value :", users_value)
        return users_value

    def writeValues(self, two_d_data):
        arr = self.correctValues(two_d_data)
        print("def writeValues(self, data):", arr)
        self.__a = arr[0]
        self.__b = arr[1]
        self.__c = arr[2]
        self.writeFile()
        self.sendValue()

    def __del__(self):
        self.writeFile()

class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.label.setPixmap(QPixmap('laba3_2.png'))

        self.m = Model(self)
        #self.m.observers.append(self)

        self.spinBox_1.returnPressed.connect(self.sendToModel)
        self.spinBox_2.returnPressed.connect(self.sendToModel)
        self.spinBox_3.returnPressed.connect(self.sendToModel)

        self.lineEdit_1.returnPressed.connect(self.sendToModel)
        self.lineEdit_2.returnPressed.connect(self.sendToModel)
        self.lineEdit_3.returnPressed.connect(self.sendToModel)

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

        values = [t1, s1, v1, t2, s2, v2, t3, s3, v3]
        print("***** SENDING TO MODEL *****")
        print("def sendToModel(self):", *values)
        self.m.recieveValues(values)

    def updateFromModel(self, object):
        print(object)
        self.lineEdit_1.setText(str(object[0]))
        self.spinBox_1.setValue(int(object[0]))
        self.verticalSlider_1.setValue(int(object[0]))

        self.lineEdit_2.setText(str(object[1]))
        self.spinBox_2.setValue(int(object[1]))
        self.verticalSlider_2.setValue(int(object[1]))

        self.lineEdit_3.setText(str(object[2]))
        self.spinBox_3.setValue(int(object[2]))
        self.verticalSlider_3.setValue(int(object[2]))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MyWindow()
    w.show()
    sys.exit(app.exec())
