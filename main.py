# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import sys


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPalette, QBrush, QPixmap, QImage, QFont, QIcon
from PyQt5.QtWidgets import QMainWindow, QApplication


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(779, 600)
        palette = QPalette()
        palette.setBrush(QPalette.Background, QBrush(QPixmap("images/white_background.jpg")))
        MainWindow.setPalette(palette)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Button = QtWidgets.QPushButton(self.centralwidget)
        self.Button.setGeometry(QtCore.QRect(290, 180, 181, 61))
        self.Button.setObjectName("pushButton")
        self.Button_load = QtWidgets.QPushButton(self.centralwidget)
        self.Button_load.setGeometry(QtCore.QRect(290, 280, 181, 61))
        self.Button_load.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 779, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Итоговый проект"))
        self.Button.setText(_translate("MainWindow", "Сделать один прогноз"))
        self.Button_load.setText(_translate("MainWindow", "Загрузить файл"))


class Main(QMainWindow, Ui_MainWindow):
    resized = QtCore.pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowIcon(QIcon('images/icon.png'))
        self.Button.clicked.connect(self.one_predict)
        self.Button_load.clicked.connect(self.file_predict)

    def resizeEvent(self, event):
        self.resized.emit()

        self.Button.move(int(self.width() * 0.286), int(self.height() * 0.36))
        self.Button.setFixedSize(int(self.width() * 0.4276), int(self.height() * 0.095))

        self.Button_load.move(int(self.width() * 0.286), int(self.height() * 0.46))
        self.Button_load.setFixedSize(int(self.width() * 0.4276), int(self.height() * 0.095))

        return super(Main, self).resizeEvent(event)

    def one_predict(self):
        self.close()
        # self.w = Registration(self.topic, self.width(), self.height(), self.isMaximized(), self.nX, self.nY)
        # self.w.show()

    def file_predict(self):
        pass


try:
    if __name__ == '__main__':
        app = QApplication(sys.argv)
        ex = Main()
        ex.show()
        sys.exit(app.exec())
except Exception as e:
    print(e.__class__.__name__)