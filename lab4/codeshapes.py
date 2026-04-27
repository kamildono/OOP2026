from PySide6.QtCore import QPoint, QRect
from PySide6.QtGui import QColor, QPen, Qt

class PyShape:

    def __init__(self, x, y, w=30, h=30, colour="green"):
        print("init Shape")

        self._cx = x
        self._cy = y
        self._width = w
        self._height = h
        self._color = QColor(colour)
        self._line_width = min(self._width, self._height) // 5 + 1
        self._state = False

    def canBePlaced(self, bounds):
        return self.checkBounds(self._cx, self._cy, self._width, self._height, bounds)

    def checkBounds(self, x, y, w, h, bounds):

        if x - w >= 0 and y - h >= 0 \
            and x + w <= bounds.width() and y + h <= bounds.height():
                return True

        return False

    def move(self, dx, dy, bounds):
        print("def move()")
        temp_x = self._cx + dx
        temp_y = self._cy + dy

        if self.checkBounds(temp_x, temp_y, self._width, self._height, bounds):
            self._cx = temp_x
            self._cy = temp_y
            print("successful move!")
            return

        print("could not move!")

    def resize(self, dw, dh, bounds):
        print("def resize()")
        temp_w = self._width + dw
        temp_h = self._height + dh

        if temp_w > 0 and temp_h > 0:
            if self.checkBounds(self._cx, self._cy, temp_w, temp_h, bounds):
                self._width = temp_w
                self._height = temp_h
                print("successful resize!")
                return

        print("could not resize")

    def disable(self):
        self._state = False

    def enable(self):
        self._state = True

    def getState(self) -> bool:
        return self._state

    def printCoord(self):
        print('coords: ', self._cx, self._cy)

    def paint(self, painter):
        painter.setBrush(self._color)
        if self._state:
            painter.setPen(QPen(QColor("cyan"), self._line_width, Qt.SolidLine))
        else:
            painter.setPen(QPen(QColor(self._color), 0))

    def fitWindow(self, bounds):
        if self._cx + self._width > bounds.width():
            self._cx = bounds.width() - self._width

        if self._cy + self._height > bounds.height():
            self._cy = bounds.height() - self._height

        if self._cx - self._width < 0:
            self._cx = self._width

        if self._cy - self._height < 0:
            self._cy = self._height

    def setColor(self, color):
        self._color = color

class Circle(PyShape):

    def __init__(self, x, y, r=30, colour="green"):
        print("init Circle")
        super().__init__(x, y, r, r, colour)

    def paint(self, painter):
        super().paint(painter)
        painter.drawEllipse(QPoint(self._cx, self._cy), self._width, self._height)

    def checkPress(self, coords) -> bool:
        if  ((coords.x() - self._cx)**2 + (coords.y() - self._cy)**2) <= self._width**2:
            print('thats i Circle who was hurt!')
            return True
        else:
            return False

class Rect(PyShape):

    def __init__(self, x, y, width=30, height=60, colour="green"):
        print("init Rect")
        super().__init__(x,y,width, height, colour)

        self._top_left = lambda : QPoint(self._cx - self._width, self._cy - self._height)
        self._bot_right = lambda : QPoint(self._cx + self._width, self._cy + self._height)

    def paint(self, painter):
        super().paint(painter)
        p1 = self._top_left()
        p2 = self._bot_right()
        painter.drawRect(QRect(p1, p2))

    def checkPress(self, coords) -> bool:
        if ((self._cx - self._width <= coords.x() <= self._cx + self._width) and \
            (self._cy - self._height <= coords.y() <= self._cy + self._height)):
            print('thats i Rect who was hurt!')
            return True
        else:
            return False

class Square(PyShape):

    def __init__(self, x, y, width=30, colour="green"):
        print("init Rect")
        super().__init__(x,y,width, width, colour)

        self._top_left = lambda : QPoint(self._cx - self._width, self._cy - self._height)
        self._bot_right = lambda : QPoint(self._cx + self._width, self._cy + self._height)

    def paint(self, painter):
        super().paint(painter)
        p1 = self._top_left()
        p2 = self._bot_right()
        painter.drawRect(QRect(p1, p2))

    def checkPress(self, coords) -> bool:
        if ((self._cx - self._width <= coords.x() <= self._cx + self._width) and \
            (self._cy - self._height <= coords.y() <= self._cy + self._height)):
            print('thats i Rect who was hurt!')
            return True
        else:
            return False

class Ellipse(PyShape):
    def __init__(self, x,y,a=30,b=60,colour="green"):
        print("init Ellipse")
        super().__init__(x,y,a,b,colour)

    def paint(self, painter):
        super().paint(painter)
        painter.drawEllipse(QPoint(self._cx, self._cy), self._width, self._height)

    def checkPress(self, coords) -> bool:
        if (((coords.x() - self._cx)/self._width)**2 + ((coords.y() - self._cy)/self._height)**2) <= 1:
            print('thats i Ellipse who was hurt!')
            return True
        else:
            return False
