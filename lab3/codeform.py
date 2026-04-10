import sys

from PySide6.QtCore import QPoint, QTimer
from PySide6.QtGui import QPainter, QColor, QPen, Qt
from PySide6.QtWidgets import QMainWindow, QApplication

from uiform import Ui_MainWindow

del_key = 16777223
ctr_key = 16777249

rel_event = 2
prs_event = 1

class Container:
    __array = []
    __size = 0
    __quick_slc = set()
    __active_ctr = False

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

    def pressed(self, whereas) -> bool:
        was_something_found = False
        for i, circ in enumerate(self.__array):
            print('we were pressed! trying to find')
            if circ.checkPress(whereas):
                self.__quick_slc.add(i)
                was_something_found = True
            if self.__active_ctr:
                continue
            else:
                break
        return was_something_found

    def deletion(self):
        for id in self.__quick_slc:
            del self.__array[id]
            self.__size -= 1

class Circle:
    __x = 0
    __y = 0
    __radius = 5
    __line_width = 1
    __state = False

    def __init__(self, x : int, y: int, radius=5):
        self.__x = x
        self.__y = y
        self.__radius = radius
        self.__line_width = radius // 5 + 1

    #def GetCoord(self):
    #    return self.__x, self.__y
    def printCoord(self):
        print('coords: ', self.__x, self.__y)

    def paint(self, painter):
        if self.__state:
            painter.setPen(QPen(QColor("cyan"), self.__line_width, Qt.DashLine))
        else:
            painter.setPen(QPen(QColor("green"), 0))
        painter.drawEllipse(QPoint(self.__x, self.__y), self.__radius, self.__radius)

    def checkPress(self, coords) -> bool:

        if  ((coords.x() - self.__x)**2 + (coords.y() - self.__y)**2) <= self.__radius**2:
            print('thats i am who was hurt!')
            self.__state = True
            return True
        else:
            return False


class MyWindow(QMainWindow, Ui_MainWindow):
    __cont = Container()
    def __init__(self):
        super().__init__()
        timer = QTimer(self)
        timer.timeout.connect(self.update)
        timer.start(100)

    def mousePressEvent(self, event, /):
        coords = event.position()
        if not self.__cont.pressed(coords):
            self.addCircle(coords)


    def keyReleaseEvent(self, event, /):
        self.__cont.keyboardUsed(event.key(), rel_event)

    def keyPressEvent(self, event, /):
        self.__cont.keyboardUsed(event.key(), prs_event)

    def addCircle(self, pos):
        print(pos.x(), pos.y())
        c = Circle(pos.x(), pos.y(), 30)
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
