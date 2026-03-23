import sys

from PySide6 import QtGui
from PySide6.QtCore import QTime, QRect
from PySide6.QtGui import QPainter
from PySide6.QtWidgets import QApplication, QMainWindow
from ui_window import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.label1.setText("Ещё не трогали")
        self.checkBox.setText("URAAA")
        #self.horizontalSlider.sliderMoved.connect(self.tabWidget.setCurrentIndex)
        self.slider = self.horizontalSlider
        self.tab_wid = self.tabWidget

        self.slider.setRange(0, self.tab_wid.count() - 1)
        self.slider.valueChanged.connect(self.tab_wid.setCurrentIndex)
        self.tab_wid.currentChanged.connect(self.slider.setValue)

        self.dial.setRange(0, 60)
        self.dial.valueChanged.connect(self.update_time_from_dial)
        self.dial.valueChanged.connect(self.label1.setNum)

        self.label2.setText("Z..z...")

        self.setWindowTitle("Новае акно")
        self.checkBox.stateChanged.connect(self.toggle_name)

        self.radio = self.radioButton
        self.radio.setText("toggle me for today!")
        self.radio.clicked.connect(self.calendar_update_radio)


        #self.paint = QtGui.QPaintEvent(paintRect)

    def paintEvent(self, event):
        canvas_painter = QPainter(self)
        canvas_painter.drawRect(QRect())

    def calendar_update_radio(self):

        self.calendarWidget.showToday()

    def toggle_name(self):
        if self.checkBox.isChecked():
            self.setWindowTitle("Новое окно")
            self.checkBox.setText("Урааа")
        else:
            self.setWindowTitle("Novoe okno")
            self.checkBox.setText("Yeaaaah")


    def update_time_from_dial(self, value):
        current_time = self.timeEdit.time()
        new_time = QTime(current_time.hour(), current_time.minute(), value)
        self.timeEdit.setTime(new_time)

    def mouseMoveEvent(self, e):
        self.label2.setText("АА МЫШЬ ДЕРГАЕТСЯ")
        #self.tab_wid.hide()
        self.tab_wid.resize(250, 150)
        self.slider.hide()


    def mouseDoubleClickEvent(self, event, /):
        self.label2.setText("ААААА МЫШЬ ТЫЧЕТ")
        #self.grabMouse()
    def mouseReleaseEvent(self, e):
        self.label2.setText("Z...z.?")
        self.tab_wid.resize(381, 271)
        self.slider.show()
        #self.releaseMouse()
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())