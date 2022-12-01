import sys


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPalette, QBrush, QPixmap, QImage, QFont, QIcon
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog

from zeropredict import ZeroPredict
from dialogwindow import Dialog
from help_functions import predict_big_data

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
        self.w = ZeroPredict()
        self.w.show()

    def file_predict(self):
        self.fname = QFileDialog.getOpenFileName(self, 'Выбрать файл', '', "(*.csv)")[0]
        pred_path = predict_big_data(self.fname)
        self.dialog = Dialog(pred_path)
        self.dialog.show()
        self.close()

try:
    if __name__ == '__main__':
        app = QApplication(sys.argv)
        ex = Main()
        ex.show()
        sys.exit(app.exec())
except Exception as e:
    print(e.__class__.__name__)