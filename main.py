import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QPen
from random import randint


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Ui.ui', self)
        self.pushButton.clicked.connect(self.run)
        self.flag = False


    def run(self):
        self.flag = True
        self.update()

    def paintEvent(self, event):
        if self.flag:
            self.qp = QPainter()
            self.qp.begin(self)
            self.draw(self.qp)
            self.qp.end()

    def draw(self, qp):
        pen = QPen(Qt.yellow, 5)
        self.qp.setPen(pen)
        x = randint(100, 400)
        y = randint(100, 400)
        r = randint(0, 100)
        self.qp.drawEllipse(x,y, r, r)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())