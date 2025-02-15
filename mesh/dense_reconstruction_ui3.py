from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(781, 438)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 10, 111, 31))
        self.pushButton.setObjectName("pushButton")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(130, 10, 191, 31))
        self.textEdit.setObjectName("textEdit")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(350, 10, 121, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(500, 10, 121, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(650, 10, 121, 31))
        self.pushButton_4.setObjectName("pushButton_4")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(10, 71, 761, 341))
        self.listWidget.setAutoScrollMargin(17)
        self.listWidget.setObjectName("listWidget")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(50, 50, 101, 31))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(250, 50, 521, 31))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(10, 50, 41, 31))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(150, 50, 101, 31))
        self.pushButton_8.setText("")
        self.pushButton_8.setObjectName("pushButton_8")
        self.textEdit2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit2.setEnabled(False)
        self.textEdit2.setGeometry(QtCore.QRect(130, 20, 191, 31))
        self.textEdit2.setObjectName("textEdit2")
        self.textEdit2.hide()  # Hide the QTextEdit widget by default
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Dense Reconstruction"))
        self.pushButton.setText(_translate("MainWindow", "稠密重建数据"))
        self.pushButton_2.setText(_translate("MainWindow", "数据保存路径"))
        self.pushButton_3.setText(_translate("MainWindow", "数据格式转换"))
        self.pushButton_4.setText(_translate("MainWindow", "稠密三维重建"))
        self.pushButton_5.setText(_translate("MainWindow", "Image name"))
        self.pushButton_6.setText(_translate("MainWindow", "Mask figure"))
        self.pushButton_7.setText(_translate("MainWindow", "Num"))

