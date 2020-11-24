import sys


from PyQt5.Qt import QMainWindow, QApplication
from PyQt5 import uic
from random import randint


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(520, 393)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(170, 130, 171, 81))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 520, 20))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Git и случайные окружности"))
        self.pushButton.setText(_translate("MainWindow", "Нарисовать окружность"))


class AppMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(520, 400)

        self.is_painting = False
        self.painter = QtGui.QPainter(self)
        self.pushButton.clicked.connect(self.paint_circle)

    def paintEvent(self, event):
        if self.is_painting:
            self.painter.begin(self)
            self.painter.setBrush(QtGui.QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
            d = randint(10, 150)
            x, y = randint(0, self.width() - d), randint(0, self.height() - d)
            self.painter.drawEllipse(x, y, d, d)
            self.painter.end()
        self.is_painting = False

    def paint_circle(self):
        self.is_painting = True
        self.repaint()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = AppMainWindow()
    main_window.show()
    sys.exit(app.exec())