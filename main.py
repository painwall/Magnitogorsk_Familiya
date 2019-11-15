import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor
from PyQt5 import uic


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.btn_draw.clicked.connect(self.passss)

    def passss(self):
        pass

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.drawFlag(qp)
        qp.end()

    def drawFlag(self, qp):
        qp.setBrush(QColor(255, 0, 0))
        qp.drawRect(30, 30, 120, 30)
        qp.setBrush(QColor(0, 255, 0))
        qp.drawRect(30, 60, 120, 30)
        qp.setBrush(QColor(0, 0, 255))
        qp.drawRect(30, 90, 120, 30)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec_())
