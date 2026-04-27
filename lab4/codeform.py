import sys

from PySide6.QtCore import QPoint, QTimer, QRect
from PySide6.QtGui import QPainter, QColor, QPen, Qt, QAction, QActionGroup, QKeySequence
from PySide6.QtWidgets import QMainWindow, QApplication, QColorDialog

from uiform import Ui_MainWindow
from codeshapes import *


slovar = {
    "Круг" : 0,
    "Эллипс" : 1,
    "Квадрат" : 2,
    "Прямоугольник" : 3
}

class Container:

    def __init__(self):
        self.__array = list()
        self.__size = 0
        self.__active_ctr = False
        self.__select_all_when_multi_layer = False
        print("Container: Im initialised!")

    def addItem(self, item):
        print("adding item!")
        self.__array.append(item)
        self.__size += 1

    def setCtrl(self, state):
        self.__active_ctr = state

    def getAll(self):
        return self.__array

    def printAll(self):
        for item in self.__array:
            item.printCoord()

    def drawAll(self, painter):
        for item in self.__array:
            #print('working at', circ)
            item.paint(painter)

    def clearStates(self):
        for item in self.__array:
            item.disable()

    def moveItems(self, dx, dy, bounds):
        for item in self.__array:
            if item.getState():
                item.move(dx, dy, bounds)

    def resizeItems(self, dw, dh, bounds):
        for item in self.__array:
            if item.getState():
                item.resize(dw, dh, bounds)

    def pressed(self, coord) -> bool:
        was_something_found = list()

        for i, item in enumerate(reversed(self.__array)):
            print('we were pressed! trying to find')
            if item.checkPress(coord):
                was_something_found.append(item)
                if self.__select_all_when_multi_layer: continue
                else: break

        if not len(was_something_found):
            return False

        if not self.__active_ctr:
            self.clearStates()
            for e in was_something_found:
                e.enable()
        else:
            for e in was_something_found:
                if e.getState():
                    e.disable()
                else:
                    e.enable()

        return True

    def deletion(self):
        to_del = []
        for circ in self.__array:
            if circ.getState():
                print('will delete: ', circ)
                to_del.append(circ)
                #self.__array.remove(circ)
                self.__size -= 1
        for x in to_del:
            self.__array.remove(x)
            del x

    def hasSelected(self):
        for item in self.__array:
            if item.getState():
                return True
        return False

    def fixWindowResize(self, bounds):
        for item in self.__array:
            item.fitWindow(bounds)

    def colorSelected(self, color):
        for item in self.__array:
            if item.getState():
                item.setColor(color)


class MyWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.__cont = Container()
        self.__current_type = 0
        self.__active_shift = False

        self.label.setText('тут клавиша')
        self.createMenu()
        self.type_group.triggered.connect(self.setType)

        timer = QTimer(self)
        timer.timeout.connect(self.update)
        timer.start(16)

    def createMenu(self):
        self.action_circ = QAction("Круг", self)
        self.action_circ.setCheckable(True)
        self.action_circ.setChecked(True)
        self.menu.addAction(self.action_circ)

        self.action_elipse = QAction("Эллипс", self)
        self.action_elipse.setCheckable(True)
        self.menu.addAction(self.action_elipse)

        self.action_square = QAction("Квадрат", self)
        self.action_square.setCheckable(True)
        self.menu.addAction(self.action_square)

        self.action_rect = QAction("Прямоугольник", self)
        self.action_rect.setCheckable(True)
        self.menu.addAction(self.action_rect)

        self.type_group = QActionGroup(self)
        self.type_group.addAction(self.action_circ)
        self.type_group.addAction(self.action_elipse)
        self.type_group.addAction(self.action_square)
        self.type_group.addAction(self.action_rect)


    def setType(self, sender):
        print("def setType:", sender.text())
        self.__current_type = slovar[sender.text()]

    def resizeEvent(self, event):
        super().resizeEvent(event)

        self.__cont.fixWindowResize(self.rect())
        self.update()

    def mousePressEvent(self, event, /):
        coords = event.position()

        if self.__cont.pressed(coords):
            return

        if self.__cont.hasSelected():
            self.__cont.clearStates()
            return

        self.addShape(coords)

    def keyReleaseEvent(self, event, /):
        self.label.setText('rel ' + QKeySequence(event.key()).toString())
        if event.key() == Qt.Key_Control:
            self.__cont.setCtrl(False)
        if event.key() == Qt.Key_Shift:
            self.__active_shift = False

    def keyPressEvent(self, event, /):
        self.label.setText('prs ' + QKeySequence(event.key()).toString())

        if event.key() == Qt.Key_Control:
            self.__cont.setCtrl(True)

        if event.key() == Qt.Key_Delete:
            self.__cont.deletion()

        if event.key() == Qt.Key_Shift:
            self.__active_shift = True

        if event.key() == Qt.Key_C:
            color = QColorDialog.getColor()
            if color.isValid():
                self.__cont.colorSelected(color)
            #self.update()
        step = 5
        if not self.__active_shift:
            if event.key() == Qt.Key_Left:
                self.__cont.moveItems(-step, 0, self.rect())
            if event.key() == Qt.Key_Right:
                self.__cont.moveItems(step, 0, self.rect())
            if event.key() == Qt.Key_Up:
                self.__cont.moveItems(0, -step, self.rect())
            if event.key() == Qt.Key_Down:
                self.__cont.moveItems(0, step, self.rect())
        else:
            if event.key() == Qt.Key_Up:
                self.__cont.resizeItems(step, step, self.rect())
            if event.key() == Qt.Key_Down:
                self.__cont.resizeItems(-step, -step, self.rect())

    def addShape(self, pos):
        print(pos.x(), pos.y())
        print("out print(self.__current_type)", self.__current_type)
        c = None
        type = None
        if self.__current_type == 0:
            typee = Circle
        elif self.__current_type == 1:
            typee = Ellipse
        elif self.__current_type == 2:
            typee = Square
        elif self.__current_type == 3:
            typee = Rect

        if typee is None:
            return

        obj = typee(pos.x(), pos.y())
        if obj.canBePlaced(self.rect()):
            self.__cont.addItem(obj)
        else:
            print("Фигура выходит за границы окна")

        self.__cont.printAll()

    def paintEvent(self, event, /):
        painter = QPainter(self)
        painter.setBrush(QColor("green"))
        self.__cont.drawAll(painter)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())
