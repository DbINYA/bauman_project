from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPalette, QBrush, QPixmap, QImage, QFont, QIcon
from PyQt5.QtWidgets import QMainWindow, QApplication

from help_functions import preporations


class Ui_ZeroPredict(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Прогноз")
        MainWindow.resize(779, 600)
        palette = QPalette()
        palette.setBrush(QPalette.Background, QBrush(QPixmap("images/white_background.jpg")))
        MainWindow.setPalette(palette)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Button_predict = QtWidgets.QPushButton(self.centralwidget)
        self.Button_predict.setGeometry(QtCore.QRect(290, 390, 191, 41))
        self.Button_predict.setObjectName("Button_predict")
        self.IW = QtWidgets.QLabel(self.centralwidget)
        self.IW.setGeometry(QtCore.QRect(120, 130, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.IW.setFont(font)
        self.IW.setObjectName("IW")
        self.IF = QtWidgets.QLabel(self.centralwidget)
        self.IF.setGeometry(QtCore.QRect(280, 130, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.IF.setFont(font)
        self.IF.setObjectName("IF")
        self.VW = QtWidgets.QLabel(self.centralwidget)
        self.VW.setGeometry(QtCore.QRect(450, 130, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.VW.setFont(font)
        self.VW.setObjectName("VW")
        self.FP = QtWidgets.QLabel(self.centralwidget)
        self.FP.setGeometry(QtCore.QRect(630, 130, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.FP.setFont(font)
        self.FP.setObjectName("FP")
        self.labelIW = QtWidgets.QLineEdit(self.centralwidget)
        self.labelIW.setGeometry(QtCore.QRect(90, 220, 113, 22))
        self.labelIW.setObjectName("labelIW")
        self.labelIF = QtWidgets.QLineEdit(self.centralwidget)
        self.labelIF.setGeometry(QtCore.QRect(240, 220, 113, 22))
        self.labelIF.setObjectName("labelIF")
        self.labelVW = QtWidgets.QLineEdit(self.centralwidget)
        self.labelVW.setGeometry(QtCore.QRect(410, 220, 113, 22))
        self.labelVW.setObjectName("labelVW")
        self.labelFP = QtWidgets.QLineEdit(self.centralwidget)
        self.labelFP.setGeometry(QtCore.QRect(580, 220, 113, 22))
        self.labelFP.setObjectName("labelFP")
        self.labeltext = QtWidgets.QLabel(self.centralwidget)
        self.labeltext.setGeometry(QtCore.QRect(200, 30, 361, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.labeltext.setFont(font)
        self.labeltext.setObjectName("labeltext")
        self.answer = QtWidgets.QLabel(self.centralwidget)
        self.answer.setGeometry(QtCore.QRect(250, 300, 261, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.answer.setFont(font)
        self.answer.setText("")
        self.answer.setObjectName("answer")
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
        self.Button_predict.setText(_translate("MainWindow", "Сделать прогноз"))
        self.IW.setText(_translate("MainWindow", "IW"))
        self.IF.setText(_translate("MainWindow", "IF"))
        self.VW.setText(_translate("MainWindow", "VW"))
        self.FP.setText(_translate("MainWindow", "FP"))
        self.labelIW.setText(_translate("MainWindow", "0"))
        self.labelIF.setText(_translate("MainWindow", "0"))
        self.labelVW.setText(_translate("MainWindow", "0"))
        self.labelFP.setText(_translate("MainWindow", "0"))
        self.labeltext.setText(_translate("MainWindow", "Введите значения признаков"))




class ZeroPredict(QMainWindow, Ui_ZeroPredict):
    resized = QtCore.pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowIcon(QIcon('images/icon.png'))
        self.Button_predict.clicked.connect(self.zeropredict)
        self.IW_data = 0
        self.IF_data = 0
        self.VW_data = 0
        self.FP_data = 0

    def resizeEvent(self, event):
        self.resized.emit()

        self.labeltext.move(int(self.width() * 0.275), int(self.height() * 0.01))
        self.labeltext.setFixedSize(int(self.width() * 0.65), int(self.height() * 0.09))
        font = QtGui.QFont()
        font.setPointSize(16 * 1.3)
        self.labeltext.setFont(font)

        self.IW.move(int(self.width() * 0.15), int(self.height() * 0.2))
        self.IW.setFixedSize(int(self.width() * 0.5), int(self.height() * 0.095))

        self.labelIW.move(int(self.width() * 0.15), int(self.height() * 0.3))
        self.labelIW.setFixedSize(int(self.width() * 0.15), int(self.height() * 0.05))

        self.IF.move(int(self.width() * 0.35), int(self.height() * 0.2))
        self.IF.setFixedSize(int(self.width() * 0.5), int(self.height() * 0.095))

        self.labelIF.move(int(self.width() * 0.35), int(self.height() * 0.3))
        self.labelIF.setFixedSize(int(self.width() * 0.15), int(self.height() * 0.05))

        self.VW.move(int(self.width() * 0.55), int(self.height() * 0.2))
        self.VW.setFixedSize(int(self.width() * 0.5), int(self.height() * 0.095))

        self.labelVW.move(int(self.width() * 0.55), int(self.height() * 0.3))
        self.labelVW.setFixedSize(int(self.width() * 0.15), int(self.height() * 0.05))

        self.FP.move(int(self.width() * 0.75), int(self.height() * 0.2))
        self.FP.setFixedSize(int(self.width() * 0.5), int(self.height() * 0.095))

        self.labelFP.move(int(self.width() * 0.75), int(self.height() * 0.3))
        self.labelFP.setFixedSize(int(self.width() * 0.15), int(self.height() * 0.05))

        self.answer.move(int(self.width() * 0.35), int(self.height() * 0.5))
        self.answer.setFixedSize(int(self.width() * 0.6), int(self.height() * 0.05))

        self.Button_predict.move(int(self.width() * 0.286), int(self.height() * 0.66))
        self.Button_predict.setFixedSize(int(self.width() * 0.4276), int(self.height() * 0.095))

        return super(ZeroPredict, self).resizeEvent(event)

    def zeropredict(self):
        a, b, c, d = self.labelIW.text(), self.labelIF.text(), self.labelVW.text(), self.labelFP.text()
        try:
            self.IW_data = float(a)
            self.IF_data = float(b)
            self.VW_data = float(c)
            self.FP_data = float(d)
            self.labeltext.setText('Введите значения признаков')
            depth, width = preporations([[self.IW_data, self.IF_data, self.VW_data, self.FP_data]])
            self.answer.setText(f'Depth:{depth}, Width:{width}')
        except ValueError:
            self.labeltext.setText('Неверный тип данных')