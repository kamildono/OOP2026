import sys

from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QMainWindow, QApplication

from mvcui import Ui_MainWindow

path_to_txt = 'data.txt'

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
        self.__a, self.__b, self.__c = map(int, data.split())
        print('init', self.__a, self.__b, self.__c)
        f.close()
        print(self.observers)
        self.sendValue()

    def writeFile(self):
        print('writeFile', self.__a, self.__b, self.__c)
        with open(path_to_txt, 'w') as f:
            f.write(str(self.__a) + ' ' + str(self.__b) + ' ' + str(self.__c))
        f.close()

    def getAll(self):
        return [self.__a, self.__b, self.__c ]

    def sendValue(self):
        print('sending!')
        for e in self.observers:
            e.updateFromModel(self.getAll())

    def recieveValues(self, object):
        print("def recieveValues(self, object):", *object)

        textes = []
        spins = []
        sliders = []

        for i in range(0, len(object), 3):
            textes.append(object[i])
            spins.append(object[i+1])
            sliders.append(object[i+2])
        two_d_data = [textes, spins, sliders]

        #analysis = self.analyzeData(data)
        #new_data = []
        #for i, x in enumerate(analysis):
        #    if not x: continue
        #    new_data.append(self.syncValues(data[i]))
        self.writeValues(two_d_data)

    def correctValues(self, two_d_data):
        a = self.correctA(two_d_data[0])
        b = self.correctB(two_d_data[1])
        c = self.correctC(two_d_data[2])
        if not a <= b <= c:
            print('govno!')
        changed_data = [a, b, c]
        return changed_data

    def correctA(self, a_arr):
        print("correctA:", a_arr)
        users_value = self.__a
        for x in a_arr:
            if int(x) == self.__a:
                continue
            users_value = int(x)
        print("correctA:", users_value)
        return users_value

    def correctB(self, b_arr):
        print("correctB:", b_arr)
        users_value = self.__b
        for x in b_arr:
            if int(x) == self.__b:
                continue
            users_value = int(x)
        print("correctB:", users_value)
        return users_value

    def correctC(self, c_arr):
        print("correctC:", c_arr)
        users_value = self.__c
        for x in c_arr:
            if int(x) == self.__c:
                continue
            users_value = int(x)
        print("correctC:", users_value)
        return users_value

    def writeValues(self, two_d_data):
        arr = self.correctValues(two_d_data)
        print("def writeValues(self, data):", arr)
        self.__a = arr[0]
        self.__b = arr[1]
        self.__c = arr[2]
        self.writeFile()
        self.sendValue()

    """
    def syncValues(self, vals):
        print('before sync', vals)

        print('after sync', vals, '\n')
        return vals

    def analyzeData(self, vals) -> list:
        gr_need_change = [False, False, False]
        atributes = [self.__a, self.__b, self.__c]
        for i, (atr, arr) in enumerate(zip(atributes, vals)):
            print("atr, arr:", atr, arr)
            if atr not in arr:
                gr_need_change[i] = True
        return gr_need_change
    """

    def __del__(self):
        self.writeFile()

class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.label.setPixmap(QPixmap('laba3_2.png'))

        """
        self.lineEdit_1.setText('10')
        self.spinBox_1.setValue(10)
        self.verticalSlider_1.setValue(10)

        self.lineEdit_2.setText('20')
        self.spinBox_2.setValue(20)
        self.verticalSlider_2.setValue(20)

        self.lineEdit_3.setText('30')
        self.spinBox_3.setValue(30)
        self.verticalSlider_3.setValue(30)
        
        """
        self.m = Model(self)
        #self.m.observers.append(self)

        self.spinBox_1.valueChanged.connect(self.sendToModel)
        self.spinBox_2.valueChanged.connect(self.sendToModel)
        self.spinBox_3.valueChanged.connect(self.sendToModel)

        self.lineEdit_1.returnPressed.connect(self.sendToModel)
        self.lineEdit_2.returnPressed.connect(self.sendToModel)
        self.lineEdit_3.returnPressed.connect(self.sendToModel)

        self.verticalSlider_1.sliderReleased.connect(self.sendToModel)
        self.verticalSlider_2.sliderReleased.connect(self.sendToModel)
        self.verticalSlider_3.sliderReleased.connect(self.sendToModel)

    def sendToModel(self):
        t1 = self.lineEdit_1.text()
        t2 = self.lineEdit_2.text()
        t3 = self.lineEdit_3.text()

        s1 = self.spinBox_1.value()
        s2 = self.spinBox_2.value()
        s3 = self.spinBox_3.value()

        v1 = self.verticalSlider_1.value()
        v2 = self.verticalSlider_2.value()
        v3 = self.verticalSlider_3.value()
        values = [t1, t2, t3, s1, s2, s3, v1, v2, v3]
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
