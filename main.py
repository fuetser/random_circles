from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import Qt
import random
import sys


class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.allow_paint = False
        self.setup_ui()

    def setup_ui(self):
        self.main_layout = QtWidgets.QVBoxLayout(self)
        self.button = QtWidgets.QPushButton("Draw", self)
        self.main_layout.addStretch()
        self.main_layout.addWidget(self.button)
        self.setWindowTitle("Git и желтые окружности")
        self.button.clicked.connect(self.set_paint_active)
        self.resize(600, 600)

    def paintEvent(self, event):
        if self.allow_paint:
            painter = QtGui.QPainter(self)
            color = QtGui.QColor(255, 255, 0)
            size = random.randint(50, 200)
            for _ in range(random.randint(1, 10)):
                color = QtGui.QColor(*random.choices(range(256), k=3))
                painter.setBrush(QtGui.QBrush(color, Qt.SolidPattern))
                painter.drawEllipse(random.randint(10, 350),
                                    random.randint(10, 350), size, size)
            self.allow_paint = False

    def set_paint_active(self):
        self.allow_paint = True
        self.update()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
