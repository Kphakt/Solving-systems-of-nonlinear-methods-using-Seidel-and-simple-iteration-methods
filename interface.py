import numpy as np
from PyQt6 import QtCore, QtGui, QtWidgets
import math
from methods import Methods

import matplotlib

matplotlib.use('Qt5Agg')

from PyQt6 import QtCore, QtGui, QtWidgets

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT as NavigationToolbar

from matplotlib.figure import Figure
class MplCanvas(FigureCanvasQTAgg):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)

class Ui_MathHelper(object):
    def setupUi(self, MathHelper):
        MathHelper.setObjectName("MathHelper")
        MathHelper.resize(512, 774)
        MathHelper.setStyleSheet("background-color: rgb(255, 255, 255);")
        MathHelper.setFixedSize(512, 774)
        self.centralwidget = QtWidgets.QWidget(parent=MathHelper)
        self.centralwidget.setObjectName("centralwidget")
        self.frame_2 = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(0, 0, 512, 774))
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.frame_2.setFont(font)
        self.frame_2.setStyleSheet("background-color: rgb(190,190,190);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.lineEdit = QtWidgets.QLineEdit(parent=self.frame_2)
        self.lineEdit.setGeometry(QtCore.QRect(128, 536, 256, 32))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("border-radius: 5px;\n"
                                    "background-color: rgb(220,220,220);\n"
                                    "\n"
                                    "")
        self.lineEdit.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=self.frame_2)
        self.lineEdit_2.setGeometry(QtCore.QRect(128, 574, 256, 32))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("border-radius: 5px;\n"
                                      "background-color: rgb(220,220,220);\n"
                                      "\n"
                                      "")
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_2.setObjectName("lineEdit_2")
        MathHelper.setCentralWidget(self.centralwidget)
        self.lineEdit_3 = QtWidgets.QLineEdit(parent=self.frame_2)
        self.lineEdit_3.setGeometry(QtCore.QRect(128, 614, 256, 32))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setStyleSheet("border-radius: 5px;\n"
                                      "background-color: rgb(220,220,220);\n"
                                      "\n"
                                      "")
        self.lineEdit_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(parent=self.frame_2)
        self.lineEdit_4.setGeometry(QtCore.QRect(128, 654, 256, 32))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setStyleSheet("border-radius: 5px;\n"
                                      "background-color: rgb(220,220,220);\n"
                                      "\n"
                                      "")
        self.lineEdit_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.pushButton = QtWidgets.QPushButton(parent=self.frame_2)
        self.pushButton.setGeometry(QtCore.QRect(180, 734, 152, 32))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("border-radius: 5px;\n"
                                      "background-color: rgb(220,220,220);\n"
                                      "\n"
                                      "")
        self.pushButton.setObjectName("pushButton")
        self.lineEdit_6 = QtWidgets.QLineEdit(parent=self.frame_2)
        self.lineEdit_6.setGeometry(QtCore.QRect(128, 694, 256, 32))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.lineEdit_6.setFont(font)
        self.lineEdit_6.setStyleSheet("border-radius: 5px;\n"
                                      "background-color: rgb(220,220,220);\n"
                                      "\n"
                                      "")
        self.lineEdit_6.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.textEdit = QtWidgets.QTextEdit(parent=self.frame_2)
        self.textEdit.setGeometry(QtCore.QRect(8, 272, 496, 256))
        self.textEdit.setStyleSheet("border-radius: 10px;\n"
                                    "background-color: rgb(220,220,220);\n"
                                    "\n"
                                    "")
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        self.widget = QtWidgets.QWidget(parent=self.frame_2)
        self.widget.setGeometry(QtCore.QRect(8, 8, 496, 256))
        self.widget.setStyleSheet("border-radius: 10px;\n"
                                  "background-color: rgb(220,220,220);\n"
                                  "\n"
                                  "")
        self.widget.setObjectName("widget")

        self.retranslateUi(MathHelper)
        QtCore.QMetaObject.connectSlotsByName(MathHelper)
        self.add_functions()

    def retranslateUi(self, MathHelper):
        _translate = QtCore.QCoreApplication.translate
        MathHelper.setWindowTitle(_translate("MathHelper", "MathHelper"))
        self.lineEdit.setText(_translate("MathHelper", "Введите уравнение 1"))
        self.lineEdit_2.setText(_translate("MathHelper", "Введите уравнение 2"))
        self.lineEdit_3.setText(_translate("MathHelper", "Введите количество итераций"))
        self.lineEdit_4.setText(_translate("MathHelper", "Введите приближенные значения"))
        self.pushButton.setText(_translate("MathHelper", "Начать"))
        self.lineEdit_6.setText(_translate("MathHelper", "Введите Epsilon"))


    # (math.sin(y - 0.5) + 1) / 2
    # 1.5 - math.cos(x)
    def add_functions(self):
        self.pushButton.clicked.connect(self.result)

    def result(self):
        self.methods = Methods(lambda x, y: eval(self.lineEdit.text()), lambda x, y: eval(self.lineEdit_2.text()),
                               int(self.lineEdit_3.text()), float(self.lineEdit_4.text().split()[0]),
                               float(self.lineEdit_4.text().split()[1]), float(self.lineEdit_6.text()))
        self.methods.method()
        self.textEdit.setText(self.methods.answer)
        x = np.linspace(-10, 10, 100)
        y = np.linspace(-10, 10, 100)
        y1 = self.lineEdit.text().replace('math', 'np')
        x1 = self.lineEdit_2.text().replace('math', 'np')
        y1 = eval(y1)
        x1 = eval(x1)
        sc = MplCanvas(self, width=1000, height=4, dpi=100)
        sc.axes.plot(x, y1, x1, y)
        sc.axes.plot([-10, 10], [0, 0], color='black')
        sc.axes.plot([0, 0], [-10, 10], color='black')
        toolbar = NavigationToolbar(sc, self)
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(toolbar)
        layout.addWidget(sc)
        self.widget.setLayout(layout)
        self.show()
        layout.deleteLater()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MathHelper = QtWidgets.QMainWindow()
    ui = Ui_MathHelper()
    ui.setupUi(MathHelper)
    MathHelper.show()
    sys.exit(app.exec())
