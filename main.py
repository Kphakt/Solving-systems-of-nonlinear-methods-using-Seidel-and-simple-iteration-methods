import sys
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QMainWindow
from interface import Ui_MathHelper


class MainWindow(QMainWindow, Ui_MathHelper):
    def __init__(self, parent=None, *args, **kwargs):
        QMainWindow.__init__(self)
        self.setupUi(self)


def main():
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec())


main()
