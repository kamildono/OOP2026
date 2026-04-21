import sys

from PySide6.QtCore import QPoint, QTimer, QRect
from PySide6.QtGui import QPainter, QColor, QPen, Qt, QAction, QActionGroup
from PySide6.QtWidgets import QMainWindow, QApplication

from uiform import Ui_MainWindow

del_key = 16777223
ctr_key = 16777249

rel_event = 2
prs_event = 1

slovar = {
    "Круг" : 0,
    "Эллипс" : 1,
    "Квадрат" : 2,
    "Прямоугольник" : 3
}

class Container:
    __array = []
    __size = 0
    __active_ctr = False
    __select_all_when_multi_layer = False

    def __init__(self):
        print("Container: Im initialised!")

    def addItem(self, item):
        print("adding item!")
        self.__array.append(item)
        self.__size += 1

    def getAll(self):
        return self.__array

    def printAll(self):
        for circ in self.__array:
            circ.printCoord()

    def drawAll(self, painter):
        for circ in self.__array:
            #print('working at', circ)
            circ.paint(painter)

    def keyboardUsed(self, key, type):
        print('trying to resolve key')
        if key == del_key and type == rel_event:
            print('it was del key!')
            self.deletion()
        elif key == ctr_key and type == prs_event:
            print('it was ctr key!')
            self.__active_ctr = True
        else:
            print('it was other key!')
            self.__active_ctr = False
            pass
    def clearStates(self):
        for item in self.__array:
            item.disable()

    def pressed(self, whereas) -> bool:
        if not self.__active_ctr:
            self.clearStates()
        was_something_found = False
        for i, circ in enumerate(self.__array):
            print('we were pressed! trying to find')
            if not circ.checkPress(whereas):
                continue
            was_something_found = True

            #if not self.__active_ctr:
            if not self.__select_all_when_multi_layer:
                break

        return was_something_found

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

class PyShape:
    _cx = 0
    _cy = 0
    _width = 0
    _height = 0
    _colour = "green"
    _line_width = 1
    _state = False

    def __init__(self, x, y, w, h, colour="green"):
        print("init Shape")

        self._cx = x
        self._cy = y
        self._width = w
        self._height = h
        self._colour = QColor(colour)
        self._line_width = min(self._width, self._height) // 5 + 1

    def disable(self):
        self._state = False

    def enable(self):
        self._state = True

    def getState(self) -> bool:
        return self._state

    def printCoord(self):
        print('coords: ', self._cx, self._cy)

    def paint(self, painter):
        if self._state:
            painter.setPen(QPen(QColor("cyan"), self._line_width, Qt.SolidLine))
        else:
            painter.setPen(QPen(QColor(self._colour), 0))

class Circle(PyShape):

    def __init__(self, x, y, r, colour="green"):
        print("init Circle")
        super().__init__(x, y, r, r, colour)

    def paint(self, painter):
        super().paint(painter)
        painter.drawEllipse(QPoint(self._cx, self._cy), self._width, self._height)

    def checkPress(self, coords) -> bool:
        if  ((coords.x() - self._cx)**2 + (coords.y() - self._cy)**2) <= self._width**2:
            print('thats i Circle who was hurt!')
            self._state = not self._state
            return True
        else:
            return False

class Rect(PyShape):
    _top_left = 0
    _bot_right = 0

    def __init__(self, x, y, width, height, colour="green"):
        print("init Rect")
        super().__init__(x,y,width, height, colour)
        self._top_left = QPoint(self._cx - self._width, self._cy - self._height)
        self._bot_right = QPoint(self._cx + self._width, self._cy + self._height)

    def paint(self, painter):
        super().paint(painter)
        p1 = self._top_left
        p2 = self._bot_right
        painter.drawRect(QRect(p1, p2))

    def checkPress(self, coords) -> bool:
        if ((self._cx - self._width <= coords.x() <= self._cx + self._width) and \
            (self._cy - self._height <= coords.y() <= self._cy + self._height)):
            print('thats i Rect who was hurt!')
            self._state = not self._state
            return True
        else:
            return False

class Ellipse(PyShape):
    def __init__(self, x,y,a,b,colour="green"):
        print("init Ellipse")
        super().__init__(x,y,a,b,colour)

    def paint(self, painter):
        super().paint(painter)
        painter.drawEllipse(QPoint(self._cx, self._cy), self._width, self._height)

    def checkPress(self, coords) -> bool:
        if (((coords.x() - self._cx)/self._width)**2 + ((coords.y() - self._cy)/self._height)**2) <= 1:
            print('thats i Ellipse who was hurt!')
            self._state = not self._state
            return True
        else:
            return False

class MyWindow(QMainWindow, Ui_MainWindow):
    __cont = Container()
    __current_type = 0

    def __init__(self):
        super().__init__()

        self.setupUi(self)

        self.label.setText('тут клавиша')
        self.createMenu()
        self.type_group.triggered.connect(self.setType)

        timer = QTimer(self)
        timer.timeout.connect(self.update)
        timer.start(100)

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

    def mousePressEvent(self, event, /):
        coords = event.position()

        if not self.__cont.pressed(coords):
            self.addShape(coords)


    def keyTranslate(self, value) -> str:
        key_debug = 'other'
        if value == del_key:
            key_debug = 'del'
        elif value == ctr_key:
            key_debug = 'ctr'
        return key_debug

    def keyReleaseEvent(self, event, /):
        self.label.setText('rel ' + self.keyTranslate(event.key()))
        self.__cont.keyboardUsed(event.key(), rel_event)

    def keyPressEvent(self, event, /):
        self.label.setText('prs ' + self.keyTranslate(event.key()))
        self.__cont.keyboardUsed(event.key(), prs_event)

    def addShape(self, pos):
        print(pos.x(), pos.y())
        print("out print(self.__current_type)", self.__current_type)
        c = None
        if self.__current_type == 0:
            c = Circle(pos.x(), pos.y(), 30)
            print("print(self.__current_type)", self.__current_type)
        elif self.__current_type == 2:
            c = Square(pos.x(), pos.y(), 30)
        elif self.__current_type == 1:
            c = Ellipse(pos.x(), pos.y(), 30, 30)
        elif self.__current_type == 3:
            print("print(self.__current_type)", self.__current_type)
            c = Rect(pos.x(), pos.y(), 30, 30)

        self.__cont.addItem(c)
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
