from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPalette, QBrush, QPixmap, QImage, QFont, QIcon
from PyQt5.QtWidgets import QMainWindow, QApplication


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Файл")
        Dialog.resize(588, 193)
        palette = QPalette()
        palette.setBrush(QPalette.Background, QBrush(QPixmap("images/white_background.jpg")))
        Dialog.setPalette(palette)
        self.label_notification = QtWidgets.QLabel(Dialog)
        self.label_notification.setGeometry(QtCore.QRect(20, 20, 521, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_notification.setFont(font)
        self.label_notification.setObjectName("label_notification")
        self.label_path = QtWidgets.QLabel(Dialog)
        self.label_path.setGeometry(QtCore.QRect(20, 90, 531, 71))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_path.setFont(font)
        self.label_path.setText("")
        self.label_path.setObjectName("label_path")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_notification.setText(_translate("Dialog", "Файл с ответами был сохранён по пути:"))



class Dialog(QMainWindow, Ui_Dialog):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowIcon(QIcon('images/icon.png'))