from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 500)
        MainWindow.setMinimumSize(QtCore.QSize(900, 500))
        MainWindow.setMaximumSize(QtCore.QSize(900, 500))
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 20, 561, 41))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.gridLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.SaveDataButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.SaveDataButton.setMinimumSize(QtCore.QSize(10, 30))
        self.SaveDataButton.setMaximumSize(QtCore.QSize(100, 30))
        self.gridLayoutWidget.setGeometry(QtCore.QRect(30, 10, 800, 30))
        self.SaveDataButton.setObjectName("SaveDataButton")
        self.horizontalLayout.addWidget(self.SaveDataButton)

        self.filePath = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.filePath.setObjectName("filePath")
        self.horizontalLayout.addWidget(self.filePath)

        self.StereoButton = QtWidgets.QPushButton(self.centralwidget)
        self.StereoButton.setMinimumSize(QtCore.QSize(10, 30))
        self.StereoButton.setMaximumSize(QtCore.QSize(100, 30))
        self.StereoButton.setGeometry(QtCore.QRect(25, 50, 561, 30))
        self.StereoButton.setObjectName("StereoButton")

        self.DepthFusionButton = QtWidgets.QPushButton(self.centralwidget)
        self.DepthFusionButton.setMinimumSize(QtCore.QSize(10, 30))
        self.DepthFusionButton.setMaximumSize(QtCore.QSize(100, 30))
        self.DepthFusionButton.setGeometry(QtCore.QRect(250, 50, 561, 30))
        self.DepthFusionButton.setObjectName("DepthFusionButton")

        self.PossionButton = QtWidgets.QPushButton(self.centralwidget)
        self.PossionButton.setMinimumSize(QtCore.QSize(10, 30))
        self.PossionButton.setMaximumSize(QtCore.QSize(100, 30))
        self.PossionButton.setGeometry(QtCore.QRect(480, 50, 561, 30))
        self.PossionButton.setObjectName("PossionButton")

        self.DeluanayButton = QtWidgets.QPushButton(self.centralwidget)
        self.DeluanayButton.setMinimumSize(QtCore.QSize(10, 30))
        self.DeluanayButton.setMaximumSize(QtCore.QSize(100, 30))
        self.DeluanayButton.setGeometry(QtCore.QRect(700, 50, 561, 30))
        self.DeluanayButton.setObjectName("DeluanayButton")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(120, 100, 640, 400))
        self.label.setStyleSheet("QLabel{\n""background-color: rgb(170, 255, 255);          //标签颜色\n""}")
        self.label.setText("")
        self.label.setObjectName("label")

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Dense Reconstruction"))
        self.StereoButton.setText(_translate("MainWindow", "立体匹配"))
        self.DepthFusionButton.setText(_translate("MainWindow", "深度图融合"))
        self.PossionButton.setText(_translate("MainWindow", "泊松重建"))
        self.DeluanayButton.setText(_translate("MainWindow", "三角剖分"))
        self.SaveDataButton.setText(_translate("MainWindow", "保存路径"))

